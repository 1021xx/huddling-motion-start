# design.md

출처: Figma 파일 `edqNEfAbK2Q49OfCOl9r4l` (node `191:532`), Figma MCP로 읽음 · 2026-10-25
규칙: 이 문서에 있는 값만 쓴다. 피그마에 없는 값은 "없음"으로 적었다.

> 모드: `primitives` · `semantic` 컬렉션 모두 모드가 **`Value` 하나뿐**이다. Light/Dark 모드 없음 → 아래 값이 곧 기본값.

---

## 1. Color Semantic (`semantic` 컬렉션)

| 변수 | hex | 가리키는 Primitive |
|---|---|---|
| `color-bg` | `#ffffff` | `neutral-0` |
| `color-surface` | `#f7f7f8` | `neutral-50` |
| `color-text` | `#18191b` | `neutral-900` |
| `color-text-muted` | `#75777c` | `neutral-500` |
| `color-primary` | `#3759de` | `brand-500` |
| `color-on-primary` | `#ffffff` | `neutral-0` |
| `color-primary-subtle` | `#edf1ff` | `brand-50` |
| `color-border` | `#e9eaed` | `neutral-200` |
| `color-attention-bg` | `#edf1ff` | `accent-100` |
| `color-attention-text` | `#3759de` | `accent-800` |
| `color-error` | `#b42318` | `error-red` |
| `color-success` | `#247a51` | `success-green` |
| `color-character-bg` | `#e3f2fd` | `sky-50` |

---

## 2. Typography (로컬 텍스트 스타일)

모든 스타일: 폰트 `Pretendard`, 자간 `0%`, 행간 단위 px. 텍스트 스타일에 연결된 변수 없음.

| 스타일 | 폰트 | 크기(px) | 굵기 | 행간(px) | 자간 |
|---|---|---|---|---|---|
| `Text/display` | Pretendard Bold | 28 | 700 | 34 | 0% |
| `Text/title` | Pretendard SemiBold | 24 | 600 | 32 | 0% |
| `Text/compact-title` | Pretendard Bold | 22 | 700 | 28 | 0% |
| `Text/section` | Pretendard Bold | 20 | 700 | 28 | 0% |
| `Text/heading` | Pretendard SemiBold | 18 | 600 | 28 | 0% |
| `Text/body` | Pretendard Regular | 15 | 400 | 24 | 0% |
| `Text/list-title` | Pretendard SemiBold | 15 | 600 | 22 | 0% |
| `Text/label` | Pretendard SemiBold | 14 | 600 | 20 | 0% |
| `Text/caption` | Pretendard Regular | 12 | 400 | 16 | 0% |
| `Text/eyebrow` | Pretendard SemiBold | 11 | 600 | 16 | 0% |

사용 굵기: 400 · 600 · 700 (세 개뿐).

---

## 3. 폰트 로드

피그마 파일에는 폰트 주소나 파일 경로 정보가 **없음**. 아래 경로는 피그마가 아니라 이 프로젝트에 넣어 둔 파일이다.

**A. 로컬 파일 (프로젝트 안: `src/assets/fonts/`)**
- `Pretendard-Regular.otf` (400) · `Pretendard-SemiBold.otf` (600) · `Pretendard-Bold.otf` (700)

경로는 부르는 HTML 파일 기준 상대 경로로 쓴다. `src/parts/*.html`에서는 `../assets/fonts/`.

```css
@font-face { font-family: "Pretendard"; font-weight: 400; src: url("../assets/fonts/Pretendard-Regular.otf") format("opentype"); }
@font-face { font-family: "Pretendard"; font-weight: 600; src: url("../assets/fonts/Pretendard-SemiBold.otf") format("opentype"); }
@font-face { font-family: "Pretendard"; font-weight: 700; src: url("../assets/fonts/Pretendard-Bold.otf") format("opentype"); }
```

**B. 웹폰트 (공식 jsDelivr 배포, 버전 고정)**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
```

영상 렌더링은 오프라인/네트워크 지연에 영향을 받지 않는 **A(로컬 파일)를 권장**한다. 어느 방법이든 첫 프레임을 캡처하기 전에 `document.fonts.ready`를 기다려야 폰트가 바뀌어 보이는 문제가 없다.

---

## 4. Scale (간격 · 모서리 · 크기 · 그림자)

피그마 Variables 그대로 (`semantic` → `primitives`). 모드 `Value` 하나.
parts를 HTML로 만들 때는 피그마 레이어 값(폭 · 여백 · 간격 · 선)을 그대로 쓴다. 영상 레이아웃(장면 배치 · 여백)에는 쓰지 않는다.

### 간격 (scope: Gap)

| 변수 | px | 가리키는 Primitive |
|---|---|---|
| `space-tight` | 4 | `space-1` |
| `space-inline` | 8 | `space-2` |
| `space-small` | 12 | `space-3` |
| `space-content` | 16 | `space-4` |
| `space-page` | 20 | `space-5` |
| `space-section` | 24 | `space-6` |
| `space-large` | 32 | `space-8` |

### 모서리 (scope: Corner radius)

| 변수 | px | 가리키는 Primitive |
|---|---|---|
| `radius-line` | 2 | `geometry-2` |
| `radius-small` | 6 | `geometry-6` |
| `radius-button` | 8 | `radius-8` |
| `radius-art` | 10 | `geometry-10` |
| `radius-card` | 12 | `radius-20` (이름은 20이지만 값은 12, 피그마 그대로) |

- 배지 모서리는 `radius-button`(8)을 함께 쓴다. 전용 변수는 만들지 않음.

### 크기 (scope: Width/Height)

| 변수 | px | 가리키는 Primitive |
|---|---|---|
| `size-tap-min` | 44 | `size-44` |
| `size-control` | 48 | `size-48` |
| `size-tabbar` | 84 | `size-84` |

### 그림자

그림자 **변수는 없음**. 아래는 Effect 스타일(이 파일의 로컬 스타일 아님, Figma MCP가 191:532 안에서 읽은 값 그대로).

| 스타일 | 종류 | 색 (RGBA hex) | x · y | 흐림 | 퍼짐 |
|---|---|---|---|---|---|
| `Shadow/sm` | Drop shadow | `#0000000F` | 0 · 1 | 2 | 0 |
| `Shadow/md` | Drop shadow | `#00000014` | 0 · 4 | 12 | 0 |
| `Shadow/lg` | Drop shadow | `#0000001F` | 0 · 8 | 24 | 0 |

---

## 5. Color Primitives (참고용, `primitives` 컬렉션)

Semantic을 거쳐서 쓰고, Primitive를 직접 쓰지 않는다.

| Primitive | hex |
|---|---|
| `neutral-0` | `#ffffff` |
| `neutral-50` | `#f7f7f8` |
| `neutral-200` | `#e9eaed` |
| `neutral-500` | `#75777c` |
| `neutral-900` | `#18191b` |
| `brand-50` | `#edf1ff` |
| `brand-500` | `#3759de` |
| `accent-100` | `#edf1ff` |
| `accent-800` | `#3759de` |
| `error-red` | `#b42318` |
| `success-green` | `#247a51` |
| `sky-50` | `#e3f2fd` |
| `illustration-*` (25개) | 이름 = hex (예: `illustration-3d5ebc` = `#3d5ebc`). 목록은 부록과 같음 |

참고: `accent-100` = `brand-50`, `accent-800` = `brand-500`는 이름만 다르고 hex는 같다.

숫자 Primitive (4장 Semantic이 가리킴)

| Primitive | px |
|---|---|
| `space-1` · `space-2` · `space-3` · `space-4` · `space-5` · `space-6` · `space-8` | 4 · 8 · 12 · 16 · 20 · 24 · 32 |
| `radius-8` · `radius-20` | 8 · 12 |
| `geometry-2` · `geometry-6` · `geometry-10` | 2 · 6 · 10 |
| `size-44` · `size-48` · `size-84` | 44 · 48 · 84 |

---

## 6. 부품 · 화면 목록

파일 → 피그마 노드 (모두 섹션 "실습 소재" 191:532 안).

### src/parts (HTML 부품)

| 파일 | 피그마 노드 | 설명 |
|---|---|---|
| `asset-card.html` | `AssetCard / private / image` · `/ review` · `/ selling` · `/ private / file` (197:640 · 197:656 · 197:671 · 197:686) | 내 자산 카드 350×74, 상태 4개 (`data-state`) |
| `badge-approved.html` | `badge-approved` (195:635) | 승인 완료 배지 108×32 |
| `brand-icon.html` | `brand-icon` (255:2700) | 검정 바탕 앱 아이콘 98×98 |
| `button-submit.html` | `button-submit` (195:634) | 파란 버튼 350×44, 문구 4개 (`data-state`) |
| `logo.html` | `Logo` (255:2692, variant 4개) | 허들링 클럽 로고, logotype · symbol × black · white |
| `mission-card.html` | `mission-card` (195:642) | 이번 달 미션 카드 350×253, 진행 바 포함 |
| `skill-card-1.html` | `skill-card-1` (195:631) | 스킬 카드 350×88 (회색 아기 펭귄) |
| `skill-card-2.html` | `skill-card-2` (195:632) | 스킬 카드 350×88 (스카프 펭귄) |
| `skill-card-3.html` | `skill-card-3` (195:633) | 스킬 카드 350×88 (회색 아기 펭귄) |
| `stat-card.html` | `stat-card` (195:636) | 이번 달 수익 카드 350×101 |
| `_check/*.png` | 위 부품과 같음 | 확인 이미지: Figma · HTML · 차이 3칸 (@2x) |

### src/screens (화면 이미지, 780×1688 = 390×844 @2x)

| 파일 | 피그마 노드 | 설명 |
|---|---|---|
| `01-home.png` | `01-home` (191:1187) | 홈: 검색 · 칩 · 미션 카드 · 스킬 |
| `02-skills.png` | `02-skills` (191:1215) | 스킬 라이브러리: 칩 · 추천 스킬 목록 |
| `03-mission.png` | `03-mission` (191:1244) | 이번 달 미션: 미션 카드 · 결과물 제출 |
| `04-approved.png` | `04-approved` (191:1258) | 미션 승인 완료: 배지 · 피드백 |
| `05-assets.png` | `05-assets` (191:1276) | 내 자산: 수익 카드 · 자산 목록 |

### src/assets (원본 파일, 감싸기만 하고 고치지 않음)

| 파일 | 피그마 노드 | 설명 |
|---|---|---|
| `buddy-front-1.png` | `Character / buddy-front` | 회색 아기 펭귄 (skill-card-1 · 3, asset-card) |
| `buddy-front-2.png` | `Character / buddy-front` | 스카프 펭귄 (skill-card-2, asset-card) |
| `perdi-flag.png` | `Character / perdi-flag` | 깃발 든 펭귄 (mission-card) |
| `logo-logotype-black.svg` · `logo-logotype-white.svg` | `color=black, type=logotype` (195:630) · `color=white, type=logotype` (255:2693) | 로고타입 149×19 |
| `logo-symbol-black.svg` · `logo-symbol-white.svg` | `color=black, type=symbol` (255:2691) · `color=white, type=symbol` (255:2690) | 심볼 100×100 (white는 brand-icon 안에도 씀) |
| `fonts/Pretendard-*.otf` | 없음 (3장) | 폰트 400 · 600 · 700 |

---

## 부록. 일러스트 색

피그마 `semantic` 컬렉션의 일러스트 전용 변수. parts 안에서 쓰는 곳: mission-card 테두리 `color-illustration-dce2f2` · 진행 바 트랙 `color-illustration-ebeef5`, brand-icon 바탕 `color-illustration-000000`.

### Semantic → Primitive (25개)

| 변수 | hex | 가리키는 Primitive |
|---|---|---|
| `color-illustration-f5f6f8` | `#f5f6f8` | `illustration-f5f6f8` |
| `color-illustration-dce2f2` | `#dce2f2` | `illustration-dce2f2` |
| `color-illustration-e9edfa` | `#e9edfa` | `illustration-e9edfa` |
| `color-illustration-bbc9ee` | `#bbc9ee` | `illustration-bbc9ee` |
| `color-illustration-000000` | `#000000` | `illustration-000000` |
| `color-illustration-c9d3ef` | `#c9d3ef` | `illustration-c9d3ef` |
| `color-illustration-ebeef5` | `#ebeef5` | `illustration-ebeef5` |
| `color-illustration-dde8d2` | `#dde8d2` | `illustration-dde8d2` |
| `color-illustration-b8cba6` | `#b8cba6` | `illustration-b8cba6` |
| `color-illustration-fffffc` | `#fffffc` | `illustration-fffffc` |
| `color-illustration-26352c` | `#26352c` | `illustration-26352c` |
| `color-illustration-ced4c9` | `#ced4c9` | `illustration-ced4c9` |
| `color-illustration-ebf0e4` | `#ebf0e4` | `illustration-ebf0e4` |
| `color-illustration-587840` | `#587840` | `illustration-587840` |
| `color-illustration-bac8ab` | `#bac8ab` | `illustration-bac8ab` |
| `color-illustration-dde5f6` | `#dde5f6` | `illustration-dde5f6` |
| `color-illustration-b1c2e9` | `#b1c2e9` | `illustration-b1c2e9` |
| `color-illustration-feffff` | `#feffff` | `illustration-feffff` |
| `color-illustration-273557` | `#273557` | `illustration-273557` |
| `color-illustration-e9effa` | `#e9effa` | `illustration-e9effa` |
| `color-illustration-6688d6` | `#6688d6` | `illustration-6688d6` |
| `color-illustration-cfd8e8` | `#cfd8e8` | `illustration-cfd8e8` |
| `color-illustration-3d5ebc` | `#3d5ebc` | `illustration-3d5ebc` |
| `color-illustration-d94c22` | `#d94c22` | `illustration-d94c22` |
| `color-illustration-8b8d93` | `#8b8d93` | `illustration-8b8d93` |
