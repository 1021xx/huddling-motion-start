# 영상 룩

출력: **16:9 · 1920×1080 · 30fps** (사용자 지정).
선택: **밝은 배경 · 단정한 헤드라인 · 밝은 엔드 카드** (사용자 확정).
색·폰트·원본 스타일의 유일한 출처는 [design.md](design.md)다. 영상용 별칭은 아래에서 정의한다.
토큰은 짧은 영어 kebab-case로 쓰며 CSS에서는 `--`를 붙인다.
이 문서는 시각적 룩만 정의한다. 장면 순서·흐름·구성은 레퍼런스가 정하고, 움직임은 [motion.md](motion.md)를 따른다.

## 1 텍스트 최소 크기

| 토큰 | 값 | 근거 |
|---|---|---|
| `video-text-scale` | 2.8 | 사용자 지정 모션용 텍스트 배율 |
| `video-text-min` | 30.8px | `Text/eyebrow` 11px × `video-text-scale` |

영상에 별도로 작성하는 텍스트는 원본 Figma 스타일 크기와 px 행간에 같은 배율을 적용한다.
소수 값을 유지하며 굵기와 자간은 원본 그대로 쓴다. 최소 크기는 최종 출력 좌표에서의 font-size 기준이다.
텍스트 wrapper의 축소나 카메라 변환 뒤에도 이 최소 크기를 지킨다.
서비스 UI를 보여 주는 screens·parts 내부 글자는 원본을 유지한다. 읽어야 할 핵심 문구는 별도 영상 텍스트로 작성해 최소 크기를 적용한다.

## 2 배경

| 토큰 | 참조 | 용도 |
|---|---|---|
| `video-bg` | `color-bg` | 밝은 영상 바탕 |
| `video-surface` | `color-surface` | 보조 면 |
| `video-accent` | `color-primary` | 강조 색 |
| `video-tint` | `color-primary-subtle` | 은은한 강조 면 |
| `video-border` | `color-border` | 경계 색 |
| `video-end-bg` | `color-bg` | 밝은 엔드 카드 바탕 |
| `video-end-text` | `color-text` | 엔드 카드 글자 |

색 값은 `design.md`의 Semantic에서 해석한다. 새로운 hex·그라데이션·반투명 색을 만들지 않는다.
엔드 카드도 동일한 색·글자 체계를 쓴다.

## 3 글자

폰트 `video-font` = **Pretendard**. `src/assets/fonts/Pretendard-*.otf`를 쓰고 `document.fonts.ready` 이후 캡처한다.
굵기는 원본의 400·600·700, 자간은 원본의 0%를 유지한다(`design.md` · Typography / 폰트 로드).

| 토큰 | 원본 스타일 | 크기(px) | 행간(px) | 굵기 |
|---|---|---|---|---|
| `video-display` | `Text/display` | 78.4 | 95.2 | 700 |
| `video-title` | `Text/title` | 67.2 | 89.6 | 600 |
| `video-compact` | `Text/compact-title` | 61.6 | 78.4 | 700 |
| `video-section` | `Text/section` | 56 | 78.4 | 700 |
| `video-heading` | `Text/heading` | 50.4 | 78.4 | 600 |
| `video-body` | `Text/body` | 42 | 67.2 | 400 |
| `video-list` | `Text/list-title` | 42 | 61.6 | 600 |
| `video-label` | `Text/label` | 39.2 | 56 | 600 |
| `video-caption` | `Text/caption` | 33.6 | 44.8 | 400 |
| `video-eyebrow` | `Text/eyebrow` | 30.8 | 44.8 | 600 |

모든 행의 계산: 원본 font-size·line-height × `video-text-scale`.

| 역할 토큰 | 참조 | 의미 |
|---|---|---|
| `video-headline` | `video-title` | 단정한 헤드라인: 원본 SemiBold 유지 |
| `video-text` | `color-text` | 기본 글자 색 |
| `video-muted` | `color-text-muted` | 보조 글자 색 |
| `video-on-accent` | `color-on-primary` | 강조 면 위 글자 색 |

글자 외곽선·장식 폰트·추가 굵기는 도입하지 않는다. 로고는 글자로 다시 조판하지 않고 원본 SVG를 쓴다.

## 4 폰 프레임

기본 룩은 서비스 화면을 담는 단순한 프레임이다. 특정 기기의 하드웨어·노치·버튼·카메라 구멍은 추가하지 않는다.

| 토큰 | 참조 | 의미 |
|---|---|---|
| `video-phone-bg` | `color-bg` | 화면 컨테이너 바탕 |
| `video-phone-radius` | `radius-card` | 단순 프레임의 모서리 |
| `video-phone-shadow` | `Shadow/md` | `design.md`의 기존 Effect 값 그대로 |
| `video-phone-ratio` | 390:844 | `design.md` · src/screens의 원본 논리 화면 비율 |

프레임 별칭은 영상용 선택이며 Figma에 기기 프레임 컴포넌트가 있다는 뜻은 아니다.
`src/screens/*.png`는 780×1688 원본을 사용한다. 가로·세로를 같은 비율로 확대하며 화면 전체 비율을 보존한다.
화면 이미지를 늘이거나 내부 글자만 확대하지 않는다. 2.8배는 별도 모션 텍스트 배율이며 폰 전체 배율이 아니다.

## 5 parts

`src/parts/*.html`을 재사용한다. 내부 크기·간격·선·모서리·글자·그림자는 `design.md`와 원본 HTML을 유지한다.
영상에 맞춘 확대는 wrapper에 균일하게 적용한다. 원본 parts 파일의 font-size에 2.8을 일괄 곱하지 않는다.

| 대상 | 룩 기준 |
|---|---|
| `skill-card-1.html`, `skill-card-2.html`, `skill-card-3.html` | 카드와 원본 캐릭터를 함께 유지 |
| `mission-card.html` | 원본 카드·진행 바·일러스트 유지 |
| `asset-card.html` | 기존 `data-state`의 색·형태 유지 |
| `stat-card.html` | 원본 수치·라벨 스타일 유지 |
| `button-submit.html` | 기존 `data-state`와 원본 버튼 스타일 유지 |
| `badge-approved.html` | 원본 배지의 크기 비율·글자 스타일 유지 |
| `logo.html` | 밝은 바탕에는 기존 `logotype-black` / `symbol-black` 원본 사용 |
| `brand-icon.html` | 원본 바탕과 흰 심볼을 함께 유지 |

`src/assets/`의 캐릭터·로고는 감싸서 쓰며 색을 바꾸거나 다시 그리지 않는다.
`src/parts/_check/*.png`는 검수용 비교 이미지이므로 영상 자산으로 사용하지 않는다.
