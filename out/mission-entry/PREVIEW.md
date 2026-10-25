# HyperFrames 미리보기

[미션 참여 · 15초 열기](http://127.0.0.1:3002/#project/video)

사용자 요청: `HyperFrames Studio에서 미리 보고, 괜찮으면 "렌더링하자"`.
현재 스냅보드 구도로 움직이는 미리보기를 구현했다. 최종 렌더·공유·업로드는 하지 않았다.

- 프로젝트: `out/mission-entry/video/`.
- 주 소스: `video/index.html`, `video/compositions/a1.html`, `a2.html`, `a3.html`.
- 루트 길이: BRIEF의 15초. 출력 크기와 fps는 docs/video.md 기준.
- 미리보기 서버: HyperFrames 관리형 background 세션, 정상 실행 및 HTTP 200 확인.
- 사용자 검토 후 `렌더링하자`라는 요청이 오면 최종 MP4를 제작한다.

## 검사

전체 HyperFrames check 최종 결과 `ok:true`, browserSkipped:false. lint·runtime·layout·motion 오류 없음.
계획한 개별 ID별 모션을 300개 시점에서 검사했다. 각 장면·등장·전환의 정지 프레임도 직접 확인했다.
최종 보고서: `video/.hyperframes/artifacts/checks/a91fe0a9-d079-4988-877a-4d0414f7b7ef.json`.
검증 프레임: `preview-frames/` — 0.12, 2.5, 5.12, 7.5, 10.1, 12.5초.
원본 parts 내부 작은 UI 글자에 대한 크기 경고와, 변환 전 크기를 사용하는 대비 경고는 검토했다. 핵심 문구는 별도 영상 글자로 제공한다. 자세한 재계산 근거는 SNAPBOARD.md 및 snapboard/static-check-summary.json.
미리보기 통과는 인코딩한 MP4의 검증을 뜻하지 않는다. 그 검수는 렌더 요청 후 수행한다.
