# 서비스 UI 움직임 · 기본 도구

이 문서의 값은 UI 반응용 기본 도구다. 영상 전체의 연출은 [표현의 재량](motion-direction.md), 결과 판정은 [품질 검수](quality-review.md)를 따른다.

성격: **경쾌함** (사용자 선택). 빠르게 반응하고 부드럽게 멈춘다. 반복 바운스와 과장된 흔들림은 기본 패턴에 없다.
토큰은 `docs/design.md`처럼 소문자 kebab-case로 쓰며 CSS에서는 `--`를 붙인다. 아래는 모션 토큰의 최초 정의다.
색·글자·로고는 기존 서비스 자산을 따른다. 장면 순서와 화면 배치는 영상별 비트 시트에서 정한다.

출처와 확인 범위:
- [C: Carbon Design System — Motion](https://carbondesignsystem.com/elements/motion/overview/): 모션 시스템 문서. Duration tokens·Easing·Style 절을 확인했다. 영상 타임코드 없음.
- [R: Remotion Prompts — Apple-Style Device Rise Animation](https://www.remotion.dev/prompts/apple-style-device-rise-animation): Prompt 본문만 확인했다. 아래 관찰은 프롬프트의 지시이며 실제 재생 영상의 측정값이 아니다.
- [S: Skillry — saadpastadev-347341](https://skillry.dev/ai-videos/opus-5-5?category=motion&video=saadpastadev-347341): 영상 접근 불가. 동작·전환·시점·프레임 수를 추정하지 않는다.
- [D: 서비스 디자인 기준](design.md): 기존 공간 토큰의 출처. 적용 대상은 현재 `src/parts`와 `src/screens`다.

R의 동작 지시는 상승하며 감속하고, 기울기·크기를 함께 정착시키며, 카드 등장을 시차로 연결하는 방식이다.
R의 실제 컷·전환·시작 시점은 미확인이다. 영상 미확보 시 사용자 성격을 기준으로 적용을 제안한다.
C의 수치는 그대로 옮기고, Semantic·Pattern의 조합은 경쾌함을 위한 서비스 설계로 구분한다.
새로 받은 참고 파일은 `references/` 안에만 보관한다. 이후 작업에서 확인한 표현 원리와 적용 기준은 [영상 연출 기준](motion-direction.md)에 기록한다.

## 1 Primitives

### Duration — 6단계

| 우리 토큰 | 값 | 출처 위치 · 원 토큰 |
|---|---|---|
| `motion-duration-01` | 70ms | C · Duration tokens · `duration-fast-01` |
| `motion-duration-02` | 110ms | C · Duration tokens · `duration-fast-02` |
| `motion-duration-03` | 150ms | C · Duration tokens · `duration-moderate-01` |
| `motion-duration-04` | 240ms | C · Duration tokens · `duration-moderate-02` |
| `motion-duration-05` | 400ms | C · Duration tokens · `duration-slow-01` |
| `motion-duration-06` | 700ms | C · Duration tokens · `duration-slow-02` |

작은 반응은 짧게, 변화가 큰 동작은 길게 고른다(C · Duration). 긴 값을 모든 요소에 공통 적용하지 않는다.
시간의 기준 단위는 ms다. 프레임 환산은 영상별 fps가 정해진 뒤 하며 원 토큰 값은 보존한다.
이 Primitive 표는 문서에서 채택한 값이며 영상 실측 표가 아니다. 문서 값의 근거는 위 문서명과 절이다.

### 곡선

| 우리 토큰 | 값 | 출처 위치 |
|---|---|---|
| `motion-ease-standard` | `cubic-bezier(0.2, 0, 0.38, 0.9)` | C · Easing · Standard / Productive |
| `motion-ease-enter` | `cubic-bezier(0, 0, 0.38, 0.9)` | C · Easing 요약 · Entrance / Productive |
| `motion-ease-exit` | `cubic-bezier(0.2, 0, 1, 0.9)` | C · Easing · Exit / Productive |
| `motion-ease-emphasis` | `cubic-bezier(0.4, 0.14, 0.3, 1)` | C · Easing · Standard / Expressive |
| `motion-ease-emphasis-enter` | `cubic-bezier(0, 0, 0.3, 1)` | C · Easing 요약 · Entrance / Expressive |
| `motion-ease-emphasis-exit` | `cubic-bezier(0.4, 0.14, 1, 1)` | C · Easing · Exit / Expressive |

등장은 감속, 완전히 사라지는 퇴장은 가속, 화면에 남는 상태 변화는 standard를 쓴다(C · Easing).
곧 다시 불러올 요소의 퇴장은 standard를 쓴다(C · Exit easing의 예외).
R의 `ease-out cubic`은 감속 성격의 참고다. 위 베지어와 동일한 곡선으로 취급하지 않는다.

### 이동량과 시차

| 우리 토큰 | 참조 | 근거 · 적용 구분 |
|---|---|---|
| `motion-distance-enter` | `space-content` = 16px | D · Scale / 간격. 등장 이동량으로의 연결은 서비스 제안 |
| `motion-stagger-item` | `motion-duration-02` | 값의 출처 C · Duration tokens. 반복 항목 간 시작 시차로의 연결은 서비스 제안 |

부품은 감싸는 요소를 움직인다. 내부 자산의 비율·형태는 유지한다. 이동량은 부품의 로컬 좌표 기준이다.

## 2 Semantic

서비스 UI 피드백에는 아래 다섯 역할을 사용한다. 영상 전체의 연출은 별도 영상 연출 기준을 함께 적용한다. 조합은 서비스 제안이며 레퍼런스 영상의 측정 결과가 아니다.

| Semantic | duration 참조 | curve 참조 | 의미 |
|---|---|---|---|
| `motion-feedback` | `motion-duration-01` | `motion-ease-standard` | 입력 직후의 짧은 상태 반응 |
| `motion-enter` | `motion-duration-04` | `motion-ease-enter` | 일반 요소의 등장 |
| `motion-exit` | `motion-duration-03` | `motion-ease-exit` | 요소의 완전한 퇴장 |
| `motion-change` | `motion-duration-03` | `motion-ease-standard` | 진행·상태·내용의 연속 변화 |
| `motion-emphasis` | `motion-duration-05` | `motion-ease-emphasis-enter` | 승인 등 중요한 결과의 등장 |

등장·퇴장은 투명도 변화와 필요할 때의 이동을 함께 쓴다. 강조는 의미 있는 결과에만 쓴다(C · Style의 서비스 적용).
출발과 도착 상태를 이어 주고, 끝에서 튀거나 계속 진동하지 않는다. 중복 트리거는 현재 상태에서 이어 간다.
감소된 모션에서는 이동·확대·회전을 생략하고 정적인 결과로 의미를 전달한다(C · Adaptive interface motion design).

## 3 Pattern

아래는 서비스 UI의 기본 동작이다. 영상 wrapper의 원근·회전·확대·버튼 반응은 [영상 표현 기준](motion-direction.md)에 따라 설계한다. 원본 형태·데이터 보존 규칙은 그대로 적용한다.

대상별 재사용 규칙이다. 파일 이름은 자산 식별자이며 재생 순서를 뜻하지 않는다.

| 대상 | 패턴 · Semantic 연결 |
|---|---|
| `src/parts/button-submit.html` | 입력 반응은 `motion-feedback`. 완료 문구 변경은 `motion-change`. 영상용 눌림 축소율은 목적에 맞게 정하고 VALUES.md에 기록한다. |
| `src/parts/skill-card-{1,2,3}.html` | wrapper에 `motion-enter`와 `motion-distance-enter`. 같은 목록의 시작 시차는 `motion-stagger-item`. 내부 글줄은 함께 움직인다. |
| `src/parts/mission-card.html` | 카드 등장은 `motion-enter`. 진행 바는 실제 이전 값에서 새 값으로 `motion-change`; 수치를 임의로 채우지 않는다. |
| `src/parts/badge-approved.html` | 결과 등장은 `motion-emphasis`. 원본 배지 형태를 유지한다. 영상 wrapper의 강조 방식은 표현 기준에 따라 선택한다. |
| `src/parts/asset-card.html` | 등장은 `motion-enter`. `data-state` 변경은 `motion-change`; 완전 삭제는 `motion-exit`. |
| `src/parts/stat-card.html` | 등장은 `motion-enter`. 값 교체는 `motion-change`; 카운트업은 실제 값의 의미를 왜곡하지 않을 때 영상별로 설계한다. |
| `src/parts/logo.html`, `brand-icon.html` | 원본을 유지하며 wrapper의 기본 도착은 `motion-enter`이며 영상용 위치·확대·원근은 별도로 설계할 수 있다. 형태 변형은 하지 않는다. |
| `src/screens/01-home.png`, `02-skills.png` | 이미지 wrapper에 `motion-enter` / `motion-exit`. 목록별 모션이 필요하면 해당 parts로 재구성한다. |
| `src/screens/03-mission.png`, `04-approved.png`, `05-assets.png` | 이미지 wrapper에 같은 화면 전환 규칙. 결과 강조는 별도 `badge-approved` part에 적용한다. |

화면 교체는 이전 이미지의 퇴장과 다음 이미지의 등장을 연결한다. 동시 시작/겹침 여부는 비트 시트에서 선택한다.
PNG 내부 글줄·버튼을 개별 요소처럼 움직이지 않는다. 연속 요소를 유지할 수 있을 때 이를 전환의 기준으로 삼는다(C · Evaluation checklist).
시차 누적으로 읽기 시작이 늦어지면 항목을 묶어 함께 등장시킨다. 그룹 구성은 영상별로 결정한다.

## 4 머무는 시간

머무름은 등장 완료부터 퇴장 시작까지의 읽는 시간이다. duration과 항목 간 시차는 머무름이 아니다.
C에는 읽기용 hold 값이 없다. R은 영상 전체와 동작 길이를 지시하지만 실제 가독성의 측정 근거는 아니다.
따라서 고정 hold 토큰은 미정이다. `motion-duration-06`을 읽는 시간으로 전용하지 않는다.
비트 시트에는 읽을 내용과 머무름의 목적을 기록한다. UI에서는 사용자가 확인·조작할 시간을 보장한다.
영상의 읽기 시간은 내용과 편집 의도에 맞게 정하고 VALUES.md에 기록한 뒤 실제 결과로 검수한다. 개별 시간값 승인은 요구하지 않는다.

승인된 계산 규칙 `motion-hold-readable`: `장면 종료 − 퇴장 duration − 마지막 등장 완료 시점` (모두 같은 시간 단위).
마지막 장면을 영상 끝까지 유지하면 퇴장 duration을 빼지 않는다. 음수이면 내용을 줄이거나 장면표를 수정한다.
출처: 사용자 승인 “A / 읽는 시간 규칙 허용”. 레퍼런스 실측값이 아닌 서비스 규칙이며, 구간은 승인된 장면표·duration은 위 토큰에서 계산한다.
장면별 계산값과 가독성 검수는 영상 폴더에 기록한다. 이 규칙은 읽기에 충분한 시간을 자동 보장하지 않는다.

## 5 카메라와 영상용 변환

고정 시점, 피사체 wrapper의 원근·회전·확대, 실제 카메라 이동 중 목적에 맞는 방식을 고른다. 서로 다른 구현을 같은 것으로 설명하지 않는다. 이동 중에는 핵심 문구를 읽도록 요구하지 않거나 읽기 좋은 정착 상태를 확보한다.

기존 duration·곡선은 출발점이다. 필요한 새 값은 영상별 VALUES.md에 기록한다. [브랜드 고정 규칙](brand-rules.md)이나 명시적 사용자 조건을 바꾸는 경우에만 해당 변경을 확인한다.

## 6 영상 품질

[표현의 재량](motion-direction.md)과 [품질 검수](quality-review.md)를 함께 적용한다. UI 토큰 준수와 모션 개수로 디자인의 완성도를 대신 평가하지 않는다.
