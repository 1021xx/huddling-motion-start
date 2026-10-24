# design.md

출처: Figma 파일 `edqNEfAbK2Q49OfCOl9r4l` (node `191:532`), Figma MCP로 읽음 · 2026-10-22
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

### 일러스트 전용 Semantic

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

피그마 파일에는 폰트 주소나 파일 경로 정보가 **없음**. 아래 경로는 피그마가 아니라 이 맥에서 확인한 값이다.

**A. 로컬 파일 (이 맥에 설치 확인됨: `/Library/Fonts/`)**
- `Pretendard-Regular.otf` (400) · `Pretendard-SemiBold.otf` (600) · `Pretendard-Bold.otf` (700)
- `PretendardVariable.ttf`도 있음

렌더러가 이 맥의 시스템 폰트를 쓰면 `font-family: "Pretendard"`만으로도 잡힌다. 다른 기기에서 렌더하거나 결과를 확실히 고정하려면 쓰는 굵기만 프로젝트 안으로 복사해서 상대 경로로 부른다.

```css
@font-face { font-family: "Pretendard"; font-weight: 400; src: url("fonts/Pretendard-Regular.otf") format("opentype"); }
@font-face { font-family: "Pretendard"; font-weight: 600; src: url("fonts/Pretendard-SemiBold.otf") format("opentype"); }
@font-face { font-family: "Pretendard"; font-weight: 700; src: url("fonts/Pretendard-Bold.otf") format("opentype"); }
```

**B. 웹폰트 (공식 jsDelivr 배포, 버전 고정)**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
```

영상 렌더링은 오프라인/네트워크 지연에 영향을 받지 않는 **A(로컬 파일)를 권장**한다. 어느 방법이든 첫 프레임을 캡처하기 전에 `document.fonts.ready`를 기다려야 폰트가 바뀌어 보이는 문제가 없다.

---

## 4. 컴포넌트 내부 치수

parts를 HTML로 만들 때는 피그마 레이어 값(폭 · 여백 · 간격 · 선)을 그대로 쓴다. 영상 레이아웃(장면 배치 · 여백)에는 쓰지 않는다.

- 배지 모서리는 `radius-button`(8)을 함께 쓴다. 전용 변수는 만들지 않음.

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
| `illustration-*` (25개) | 이름 = hex (예: `illustration-3d5ebc` = `#3d5ebc`). 목록은 1장의 일러스트 표와 같음 |

참고: `accent-100` = `brand-50`, `accent-800` = `brand-500`는 이름만 다르고 hex는 같다.
