"""Render-source builder for approved storyboard A; no video timeline."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
DEST = Path(__file__).resolve().parent / 'snapboard'

def part(name, state=None):
    source = (ROOT / 'src/parts' / (name + '.html')).read_text()
    css = '\n'.join(re.findall(r'<style>(.*?)</style>', source, re.S))
    css = re.sub(r'@font-face\s*\{.*?\}', '', css, flags=re.S)
    css = re.sub(r'html, body\s*\{.*?\}', '', css, flags=re.S)
    body = re.search(r'<body>(.*?)</body>', source, re.S)[1]
    body = re.sub(r'<script>.*?</script>', '', body, flags=re.S)
    body = body.replace('../assets/', 'assets/')
    if state:
        body = re.sub(r'data-state="[^"]+"', f'data-state="{state}"', body)
    return css, body

frames = [
    dict(id='A1', screen='03-mission.png', title='이번 달 미션에<br>도전해요',
         copy='미션을 확인하고,<br>적용 사례를 준비해요.',
         parts=[('mission-card', None)], ref='R-01~04'),
    dict(id='A2', screen='03-mission.png', title='결과물과 적용 사례를<br>제출해요',
         copy='파일과 활용 내용을 함께.',
         parts=[('mission-card', None), ('button-submit', 'submit')], ref='R-03~04'),
    dict(id='A3', screen='04-approved.png', title='검토 후,<br>내 자산으로',
         copy='승인된 결과물이<br>내 자산에 등록돼요.',
         parts=[('badge-approved', None), ('button-submit', 'view-assets'), ('logo', 'logotype-black')], ref='R-03~04'),
]

base_css = '''
@font-face {font-family:Pretendard; font-weight:400; src:url('assets/fonts/Pretendard-Regular.otf')}
@font-face {font-family:Pretendard; font-weight:600; src:url('assets/fonts/Pretendard-SemiBold.otf')}
@font-face {font-family:Pretendard; font-weight:700; src:url('assets/fonts/Pretendard-Bold.otf')}
html,body {margin:0;width:1920px;height:1080px;overflow:hidden;background:#ffffff}
* {box-sizing:border-box}
#root {position:relative;width:1920px;height:1080px;background:#ffffff;font-family:Pretendard}
.layout {display:grid;grid-template-columns:1fr 1fr;align-items:center;width:100%;height:100%}
.phone-column {display:flex;align-items:center;justify-content:center;height:100%}
.phone {width:390px;height:844px;border-radius:12px;box-shadow:0 4px 12px 0 #00000014;overflow:hidden}
.phone img {display:block;width:390px;height:844px}
.narrative {width:880px;display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.headline {margin:0;color:#18191b;font-size:67.2px;font-weight:600;line-height:89.6px;letter-spacing:0}
.subline {margin:0;color:#18191b;font-size:42px;font-weight:400;line-height:67.2px;letter-spacing:0}
.parts {display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.part-shell {position:relative;flex:none}
.part-scale {position:absolute;left:0;top:0;transform-origin:top left;transform:scale(2)}
'''
sizes = {'mission-card': (350,253), 'button-submit': (350,44), 'badge-approved': (108,32), 'logo': (149,19)}

for frame in frames:
    folder = DEST / frame['id'].lower()
    assets = folder / 'assets'
    (assets / 'fonts').mkdir(parents=True, exist_ok=True)
    for font in (ROOT / 'src/assets/fonts').glob('*.otf'):
        shutil.copy2(font, assets / 'fonts' / font.name)
    for name in [frame['screen'], 'perdi-flag.png', 'logo-logotype-black.svg', 'logo-logotype-white.svg', 'logo-symbol-black.svg', 'logo-symbol-white.svg']:
        source = ROOT / ('src/screens' if name == frame['screen'] else 'src/assets') / name
        shutil.copy2(source, assets / name)
    css = base_css
    pieces = []
    for name, state in frame['parts']:
        pc, pb = part(name, state)
        css += '\n' + pc
        w,h = sizes[name]
        pieces.append(f'<div class="part-shell" style="width:{w*2}px;height:{h*2}px" data-source="src/parts/{name}.html"><div class="part-scale">{pb}</div></div>')
    body = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{frame['id']} · 정착 상태</title><style>{css}</style></head><body>
<div id="root" data-composition-id="{frame['id'].lower()}-still" data-width="1920" data-height="1080" data-duration="0.7" data-no-timeline>
<div class="layout"><div class="phone-column"><div class="phone"><img src="assets/{frame['screen']}" alt="서비스 원본 화면"></div></div>
<div class="narrative"><h1 class="headline">{frame['title']}</h1><p class="subline">{frame['copy']}</p><div class="parts">{''.join(pieces)}</div></div></div></div>
</body></html>'''
    (folder / 'index.html').write_text(body)

# Pose-only illustration of A1 at the mathematical midpoint of its entrance.
# No GSAP/CSS animation or time-seeking video is authored before approval B.
def cubic(a, b, t):
    return 3*(1-t)*(1-t)*t*a + 3*(1-t)*t*t*b + t*t*t

lo, hi = 0.0, 1.0
for _ in range(60):
    u = (lo+hi)/2
    if cubic(0, 0.38, u) < 0.5:
        lo = u
    else:
        hi = u
progress = cubic(0, 0.9, (lo+hi)/2)
folder = DEST / 'a1-entry'
folder.mkdir(parents=True, exist_ok=True)
shutil.copytree(DEST / 'a1/assets', folder / 'assets', dirs_exist_ok=True)
body = (DEST / 'a1/index.html').read_text()
pose = f'.phone {{transform:translateY({16*(1-progress):.8f}px);opacity:{progress:.8f}}} .parts {{opacity:0}}'
body = body.replace('</style>', pose+'</style>')
body = body.replace('a1-still', 'a1-entry-still').replace('A1 · 정착 상태', 'A1 · 등장 중간 포즈')
(folder / 'index.html').write_text(body)
print('Built three still compositions; no video timeline or animation was created.')
