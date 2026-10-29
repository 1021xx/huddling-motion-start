# 로컬 개발 환경

- 프로젝트: C:\Users\AgencyPro_105\Desktop\huddling-motion-start
- 기존 영상: out/mission-entry/video
- 미리보기: http://localhost:3002/#project/video
- 루트의 Start-Preview.cmd를 더블클릭하면 미리보기가 시작됩니다.
- 프로젝트 전용 Node 24는 .hyperframes/bin/node.exe에 있습니다.
- FFmpeg와 FFprobe는 영상 폴더의 .hyperframes/bin에 있습니다.
- HyperFrames는 저장소에 고정된 0.8.198을 사용합니다.

PowerShell에서 CLI를 사용할 때:

```powershell
$env:Path = 'C:\Users\AgencyPro_105\Desktop\huddling-motion-start\.hyperframes\bin;' + $env:Path
Set-Location 'C:\Users\AgencyPro_105\Desktop\huddling-motion-start\out\mission-entry\video'
npm run check
```

초기 검사: 브라우저 검사는 실행됨. 기존 a1.html에서 색 대비 오류 2건(4.48:1, 기준 4.5:1) 및 작은 글자 등의 경고가 있음. 영상 소스는 설정 과정에서 변경하지 않았습니다.
