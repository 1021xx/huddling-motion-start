"""Build the approved A storyboard as seekable HyperFrames source."""
from pathlib import Path
import json
import re
import shutil
from html.parser import HTMLParser

BASE = Path(__file__).resolve().parent
VIDEO = BASE / 'video'
(VIDEO / 'compositions').mkdir(exist_ok=True)
assets = VIDEO / 'assets'
shutil.copytree(BASE / 'snapboard/a1/assets', assets, dirs_exist_ok=True)
shutil.copy2(BASE / 'snapboard/a3/assets/04-approved.png', assets / '04-approved.png')

# GSAP eases evaluate the exact public cubic-bezier token, without substituting
# a similar built-in ease. Iterations below control numerical precision only.
ease_helper = '''
function bezier(x1,y1,x2,y2) {
  const value=(a,b,t)=>3*(1-t)*(1-t)*t*a+3*(1-t)*t*t*b+t*t*t;
  return p=>{
    if(p<=0) return 0; if(p>=1) return 1;
    let lo=0,hi=1;
    for(let i=0;i<60;i++){let u=(lo+hi)/2;if(value(x1,x2,u)<p)lo=u;else hi=u;}
    return value(y1,y2,(lo+hi)/2);
  };
}
const enter=bezier(0,0,0.38,0.9);
const exit=bezier(0.2,0,1,0.9);
const emphasis=bezier(0,0,0.3,1);
const change=bezier(0.2,0,0.38,0.9);
'''

for scene in ['a1','a2','a3']:
    source=(BASE / f'snapboard/{scene}/index.html').read_text()
    css=re.search(r'<style>(.*?)</style>',source,re.S)[1]
    css=re.sub(r'html,body\s*\{.*?\}', '', css, flags=re.S)
    css=re.sub(r'#root\s*\{.*?\}', '#root {position:absolute;inset:0;font-family:Pretendard}',css,flags=re.S)
    body=re.search(r'<body>(.*?)</body>',source,re.S)[1].strip()
    body=re.sub(r'^<div id="root"[^>]*>','',body).strip()
    body=body.rsplit('</div>',1)[0]
    ids=set(re.findall(r'id="([^"]+)"',body))
    for original in sorted(ids,key=len,reverse=True):
        body=body.replace(f'id="{original}"',f'id="{scene}-{original}"')
        css=re.sub(r'#'+re.escape(original)+r'(?![\w-])','#'+scene+'-'+original,css)
    body=body.replace('<div class="phone-column">',f'<div id="{scene}-phone-clip" class="phone-column clip" data-start="0" data-duration="5" data-track-index="0">')
    body=body.replace('<div class="phone">',f'<div id="{scene}-phone-motion" class="phone">')
    body=body.replace('<div class="narrative">',f'<div id="{scene}-narrative" class="narrative clip" data-start="0" data-duration="5" data-track-index="1" data-hold="reading">')
    body=body.replace('<h1 class="headline">',f'<h1 id="{scene}-headline" class="headline" data-var-text="{scene}-headline">')
    body=body.replace('<p class="subline">',f'<p id="{scene}-subline" class="subline" data-var-text="{scene}-subline">')
    css+='\n.phone-column,.narrative,.part-shell{position:relative!important}\n.phone{position:relative}\n.phone img{position:absolute;left:0;top:0}\n.part-motion,.part-timing{position:absolute;inset:0}\n'

    parts = ([('card',.24,.24)] if scene=='a1' else
             [('card',0,.24),('button',.11,.24)] if scene=='a2' else
             [('badge',.15,.4),('button',.26,.24),('logo',.37,.24)])
    # Put the seeked motion on a child, leaving the source's uniform scale on
    # its own untouched inner wrapper.
    class MotionWrapper(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.output=[]
            self.divs=[]
            self.part_index=0
        def handle_starttag(self,tag,attrs):
            shell=tag=='div' and dict(attrs).get('class')=='part-shell'
            if tag=='div': self.divs.append(shell)
            markup=self.get_starttag_text()
            if shell:
                label,start,duration=parts[self.part_index]
                self.part_index+=1
                markup=markup.replace('<div ',f'<div id="{scene}-{label}-shell" ',1)
                markup+=(f'<div id="{scene}-{label}-clip" class="part-timing clip" data-start="{start}" '
                         f'data-duration="{5-start:.2f}" data-track-index="{self.part_index+1}">'
                         f'<div id="{scene}-{label}-motion" class="part-motion">')
            self.output.append(markup)
        def handle_endtag(self,tag):
            if tag=='div' and self.divs.pop(): self.output.append('</div></div>')
            self.output.append(f'</{tag}>')
        def handle_data(self,data): self.output.append(data)
        def handle_entityref(self,name): self.output.append(f'&{name};')
        def handle_charref(self,name): self.output.append(f'&#{name};')
        def handle_comment(self,data): self.output.append(f'<!--{data}-->')
    parser=MotionWrapper()
    parser.feed(body)
    body=''.join(parser.output)

    timeline= ease_helper+'\nconst tl=gsap.timeline({paused:true});\n'
    if scene=='a1':
        timeline+=f'tl.fromTo("#{scene}-phone-motion",{{y:16,opacity:0}},{{y:0,opacity:1,duration:0.24,ease:enter}},0);\n'
    if scene=='a3':
        body=body.replace('<img src="assets/04-approved.png" alt="서비스 원본 화면">',
            '<img src="assets/03-mission.png" alt="미션 화면">'
            '<div id="a3-screen-change" class="screen-change"><img src="assets/04-approved.png" alt="승인 화면"></div>')
        css+='\n.screen-change{position:absolute;inset:0}\n'
        timeline+='tl.fromTo("#a3-screen-change",{opacity:0},{opacity:1,duration:0.15,ease:change},0);\n'
    for label,start,duration in parts:
        curve='emphasis' if label=='badge' else 'enter'
        timeline+=(f'tl.fromTo("#{scene}-{label}-motion",{{y:-16,opacity:0}},'
                   f'{{y:0,opacity:1,duration:{duration},ease:{curve}}},{start});\n')
    if scene!='a3':
        timeline+=f'tl.to("#{scene}-narrative",{{opacity:0,duration:0.15,ease:exit}},4.85);\n'
    timeline+=f'window.__timelines["{scene}"]=tl;\n'
    (VIDEO/f'compositions/{scene}.html').write_text(
        f'<template>\n<style>{css}</style>\n<div id="root" data-composition-id="{scene}" data-width="1920" data-height="1080">{body}</div>\n<script>{timeline}</script>\n</template>')

hosts='\n'.join(f'<div id="{s}" class="clip" data-composition-id="{s}" data-composition-src="compositions/{s}.html" data-start="{i*5}" data-duration="5" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>' for i,s in enumerate(['a1','a2','a3']))
(VIDEO/'index.html').write_text(f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>미션 참여 · 15초</title>
<script src="assets/gsap.min.js"></script>
<style>html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#ffffff}}#root{{position:relative;width:1920px;height:1080px}}.clip{{position:absolute;inset:0}}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1920" data-height="1080">{hosts}</div>
<script>window.__timelines=window.__timelines||{{}};window.__timelines.main=gsap.timeline({{paused:true}});</script></body></html>''')
(VIDEO/'index.motion.json').write_text(json.dumps({'duration':15,'assertions':[
    {'kind':'appearsBy','selector':'#a1-phone-motion','bySec':.24},
    {'kind':'before','a':'#a1-phone-motion','b':'#a1-card-motion'},
    {'kind':'before','a':'#a2-card-motion','b':'#a2-button-motion'},
    {'kind':'before','a':'#a3-badge-motion','b':'#a3-button-motion'},
    {'kind':'before','a':'#a3-button-motion','b':'#a3-logo-motion'},
    *[{'kind':'staysInFrame','selector':f'#{s}-phone-motion'} for s in ['a1','a2','a3']],
    *[{'kind':'staysInFrame','selector':f'#{s}-headline'} for s in ['a1','a2','a3']],
    *[{'kind':'staysInFrame','selector':'#'+s+'-'+p+'-shell'} for s,ps in [('a1',['card']),('a2',['card','button']),('a3',['badge','button','logo'])] for p in ps]
    ]},ensure_ascii=False,indent=2))
print('Built the approved 15-second preview. No MP4 rendered.')
