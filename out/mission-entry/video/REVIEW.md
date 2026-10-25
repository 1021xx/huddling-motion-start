# 렌더 전 검수

사용자가 미리보기 확인 후 `렌더링하자`라고 요청했다. 승인된 A · 따라가기 구도를 유지해 로컬 최종 MP4를 생성한다.

- 채택: 미션 확인 → 제출 → 검토 후 승인. 다른 후보 B/C는 제작하지 않음.
- 최신 소스는 미리보기에서 부여한 data-hf-id를 포함하며 재생성 스크립트로 덮어쓰지 않음.
- 최종 렌더 전 check: `ok:true`, browserSkipped:false, lint·runtime·layout·motion·contrast 오류 0건. 모션 300시점 검사.
- 보고서: `.hyperframes/artifacts/checks/2c56d604-dac9-43bf-92a5-a71197faf0d2.json`.
- 검토한 이미지: `../render-review/review-beats.jpg`, `review-phone.jpg`, `review-seam-01.jpg`, `review-seam-02.jpg`.
- 장면과 전환에서 제목·부품 겹침이나 잘림이 없음을 확인했다. 핵심 설명은 별도 영상 문구로 읽는다.
- 남긴 경고: 원본 부품의 작은 UI 글자와 변환 전 font-size 기반 대비 분류. 원본 유지·2배 실제 표시·별도 핵심 문구에 대한 기존 검토 근거는 `../SNAPBOARD.md`, `../VALUES.md`와 `../snapboard/static-check-summary.json` 참고.
- 가장 약한 부분: 작은 재생 화면에서는 원본 UI의 세부 문구가 읽히기 어렵다. 별도 핵심 요약은 유지하고, 원본 UI는 맥락으로 사용한다.
- 무음 기준 BRIEF를 유지한다. 음성을 추가하거나 음향을 감상했다고 주장하지 않는다.

이 기록은 렌더 전 검수다. 인코딩 결과의 길이·프레임·시각 확인은 생성 완료 후 별도로 기록한다.

## 최종 MP4 검수 완료

PASS | 최종 MP4 표본 검수 | 문서 밖 숫자: 0개 | src 밖 UI: 0개 | 레퍼런스: 4/4(100%, 기존 브라우저 동작 검사 포함) | ../encoded-review/frame-01~06.png

- 결과: `../mission-entry.mp4`, H.264, 1920×1080, 30fps, 450프레임, 정확히 15초, 802665bytes. 무음 BRIEF에 따라 오디오 스트림 없음.
- 렌더: HyperFrames 0.8.198, delivery 옵션, screenshot capture·hardware GPU, 약 26.4초 소요.
- ffprobe로 포맷·길이·프레임 수를 확인했다. ffmpeg로 프레임 3·75·225·303·375·449를 디코딩했다.
- critic이 실제 디코딩 표본 6장을 확인했다. 미리보기와 구도·자산·문구가 일치하며 중대한 잘림·누락·인코딩 깨짐 없음. 마지막 프레임의 로고·승인 결과 유지 확인.
- 450프레임 전부를 눈으로 보거나 전체 MP4를 연속 재생한 검수는 아니다. 동작은 기존 브라우저 300시점 검사와 디코딩 표본을 함께 근거로 삼았다.
- 기존 경고는 위 기록대로 유지한다. 새 중대 문제 없음. 외부 업로드·게시하지 않았다.
