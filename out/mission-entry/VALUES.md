# 값과 자산의 근거 — 스냅보드 v1

## 출력·시각 값

| 사용값 | 근거 |
|---|---|
| 캔버스 1920×1080, 후속 영상 30fps | docs/video.md 머리말 |
| 영상 headline 67.2px / 89.6px, 600 | docs/video.md 3장 · video-headline → video-title |
| 영상 body 42px / 67.2px, 400 | docs/video.md 3장 · video-body |
| Pretendard, 자간 0 | docs/design.md 2~3장, 로컬 원본 OTF |
| 영상 바탕 #ffffff, 기본 글자 #18191b | video-bg / video-text → docs/design.md 1장 |
| 폰 390×844, 원본 PNG 780×1688 | docs/design.md 6장, video-phone-ratio. 원본을 논리 크기로 균일 표시 |
| 폰 radius 12, shadow 0·4·12·0 #00000014 | docs/video.md 4장 → radius-card / Shadow/md → design.md 4장 |
| 부품 내부의 모든 값 | 각 src/parts HTML을 파싱해 CSS·마크업 그대로 삽입. 파일·폰트 경로만 출력 폴더로 치환 |
| 부품 wrapper의 고정 표시 배율 2 | screens 원본의 물리/논리 픽셀 비율 780/390 = 2. 원본 부품을 같은 비율로 표시하며 동적 스케일 아님 |
| 카드 700×506, 제출 버튼 700×88 | 원본 mission-card 350×253, button-submit 350×44에 위 표시 배율 적용 |
| 배지 216×64, 로고 298×38 | 원본 badge-approved 108×32, logo의 logotype 149×19에 같은 표시 배율 적용 |

## 배치 계산

폰 맥락과 부품 설명의 두 열은 이 영상의 구도다. src/screens/03-mission.png의 카드·제출 버튼이 같은 왼쪽 선에 놓이는 관계를 우측 설명에도 유지한다.
각 열은 캔버스 폭 / 2 = 960px. 폰은 첫 열 안에서 중앙 정렬하여 x=(960−390)/2=285px, y=(1080−844)/2=118px.
우측 설명 묶음의 왼쪽 선은 다음 열의 시작 x=960px. 폭은 열 폭에서 src 화면의 물리 좌우 여백(40px씩)을 제외한 880px이며 콘텐츠는 왼쪽 정렬한다.
우측 묶음의 세로 위치는 실제 콘텐츠 높이를 측정한 뒤 캔버스에서 중앙 정렬한다. 화면마다 제목·카드 높이가 다르므로 세로 위치도 달라진다.
우측 원본 카드·버튼·배지·로고도 같은 왼쪽 선을 사용한다. 묶음 간 간격 24px은 mission-card.html의 내부 gap 12px를 위 표시 배율로 환산한 값이다.
폰 PNG와 우측 HTML 부품은 별도의 설명 영역이다. 화면 이미지 위에 중복 UI를 겹치지 않는다.
A1의 apply-case 버튼은 원본 mission-card 안에 이미 있으므로 이를 재사용한다. 같은 버튼을 별도로 그리지 않는다.
A2의 apply-case와 submit은 각각 원본 카드와 기존 별도 제출 버튼이며 새 상태를 만들지 않는다.
이미지·부품의 작은 글자는 제품 맥락이다. 읽어야 할 요약은 별도 영상 글자로 제공하며 최소 크기는 video.md 1장을 따른다.

## 승인된 시간 계산 — 움직이는 미리보기에 구현

전체 15초는 사용자 BRIEF. A1 [0,5), A2 [5,10), A3 [10,15)는 승인 A의 장면표 분할이다.
duration과 curve는 motion.md 1~2장, 읽는 시간 계산은 승인된 motion.md 4장의 motion-hold-readable을 따른다.

| 장면 | 등장 계획 (구간 안 상대 시간) | 읽는 시간 계산 |
|---|---|---|
| A1 | 폰 motion-enter 완료 240ms → 카드 전체가 motion-enter 240ms. 내부 apply-case 버튼도 카드와 함께 등장. 마지막 완료 480ms | 5000−150−480 = 4370ms |
| A2 | 같은 폰 정착 상태 유지. 카드와 submit을 motion-stagger-item으로 시작. 240ms + 110ms 뒤 마지막 완료 350ms | 5000−150−350 = 4500ms |
| A3 | 승인 화면 교체 motion-change 완료 150ms → 배지 motion-emphasis 400ms, 버튼은 110ms 뒤·240ms, 로고는 다시 110ms 뒤·240ms. 마지막 완료 610ms | 마지막 장면은 퇴장 없음: 5000−610 = 4390ms |

위 계산은 연속 시간 기준이다. 실제 렌더는 문서의 출력 fps에서 샘플링하고 ms 토큰 원값은 바꾸지 않는다.
A1 카드 내부 버튼은 독립적으로 움직이지 않는다. R-04의 부품 간 시차는 A2의 카드·별도 제출 버튼과 A3의 배지·버튼에서 검증한다. 정적 룩은 바뀌지 않는다.
아직 읽기 속도의 합격 판정이 아니다. 스냅보드에서 글자와 구도를, 실제 영상에서 읽는 시간·타이밍을 확인한다.
영상 헤드라인·보조 글자는 각 구간 시작부터 읽을 수 있게 두고, 폰/카드와 같은 등장 지연을 추가하지 않는다.

## 스냅보드 포즈

각 still의 data-duration=0.7s는 snapshot 도구용 정지 캔버스 메타데이터다. motion-duration-06의 단위 환산이며 영상의 장면·머무름 시간으로 사용하지 않는다.
모든 정지 캔버스는 data-no-timeline이며 타임라인·CSS 애니메이션이 없다. 이미지 파일명의 0s는 정지 캔버스의 캡처 위치이지 본 영상의 타임코드가 아니다.
A1-entry는 motion-enter의 중간 시간(240ms / 2)에 해당하는 포즈만 계산했다. motion-ease-enter의 cubic-bezier를 역산하여 폰 투명도와 16px 이동량의 남은 거리에 적용한다.
0·1은 투명도/보간의 양 끝값, 2는 중간 포즈의 분할 수, 60회 이분 탐색과 소수 출력 정밀도는 수치 계산용이며 새로운 모션 강도 값이 아니다.
A1-entry의 부품은 폰 정착 전이므로 투명 상태다. 실제 등장 순서·감속 검증을 대신하지 않는다.

## 빌드와 추적

`build-snapboard.py` → `snapboard/{a1,a2,a3,a1-entry}/index.html` → Hyperframes snapshot → `snapboard/images/`.
원본 HTML·PNG·OTF·SVG는 수정하지 않았다. Figma 내보내기 작업과 무관한 로컬 산출물이다.

## 움직이는 미리보기

`build-video.py`는 승인된 still 소스를 재사용해 `video/index.html`과 `video/compositions/{a1,a2,a3}.html`을 만든다.
각 장면의 슬롯은 5초, 루트는 15초다. `video/package.json`의 최종 render 명령은 30fps로 고정했다. 아직 해당 명령은 실행하지 않았다.
GSAP 3.14.2는 scaffold의 버전 그대로이며 `video/assets/gsap.min.js`에 로컬 저장했다. 런타임 버전은 모션 값이 아니다.
각 cubic-bezier 토큰을 수치 함수로 계산해 사용한다. 비슷한 이름의 내장 ease로 대체하지 않는다.
CSS의 부품 표시 배율과 GSAP의 등장 이동은 서로 다른 wrapper에 둔다. 부품 크기와 제목의 정렬은 부품 등장 전에도 유지한다.
motion sidecar는 개별 ID로 등장 순서와 프레임 안 배치를 검증한다. `data-hold`는 승인된 읽는 구간의 의도된 정지를 나타낸다.
미리보기: http://127.0.0.1:3002/#project/video · 로컬 관리형 서버, 렌더 요청 전까지 검토용으로 유지.
