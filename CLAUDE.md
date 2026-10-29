# 모션 하네스

서비스 영상 제작 요청은 [make-video](skills/make-video/SKILL.md)를 읽고 시작한다. 단순 문서 확인·수정 요청으로 영상을 제작하지 않는다.

## 세 가지 기준

1. [브랜드·원본 고정 규칙](docs/brand-rules.md): 브랜드 정체성·실제 UI·서비스 사실·사용자 조건을 보호한다. 상세 원본은 design.md와 src/에 있다.
2. [영상 표현의 재량](docs/motion-direction.md): 구도·크기·여백·카메라·원근·타이포·곡선·편집을 목적에 맞게 설계한다. motion.md/video.md는 기본 도구, motion-examples.md는 재현용 예시다. 문서에 없는 연출 숫자만으로 중단하지 않는다.
3. [디자인·모션 품질 검수](docs/quality-review.md): 브랜드·사실, 정적 디자인, 움직임·편집, 기술을 따로 판단한다. 기술 통과나 참고 효과 개수로 미적 품질을 대신하지 않는다.

사용자의 최신 지시가 우선한다. 서비스 원본과 영상용 표현을 구분한다. 특정 시안의 장면 순서·좌표·효과를 모든 영상에 반복하지 않는다.

## 역할

- [art-director](agents/art-director.md): 실제 참고 표현의 관찰과 서비스용 룩 설계.
- [director](agents/director.md): 전달 내용·시선·장면 연결·읽기 시간을 설계.
- [builder](agents/builder.md): 실제 자산으로 구도와 움직임 구현.
- [critic](agents/critic.md): 별도 품질 축으로 근거를 확인하고 수정 방향 제시.

역할 문서를 작업 전에 읽는다. 필요한 역할 검수를 위임할 수 있으며, 같은 세션에서는 역할을 구분해 수행한다. 수치는 docs에 중복 복사하지 말고 영상별 VALUES.md에 선택 근거를 남긴다.

## 실행 경계

영상별 BRIEF·REFERENCE·STORYBOARD·APPROVALS·스냅보드·VALUES·REVIEW·렌더는 out/<영상이름>/에 격리한다. 참고 파일은 references/<영상이름>/에 보관한다. 기존 결과를 덮어쓰지 않는다. 이어서 작업할 때 기존 BRIEF와 피드백부터 확인한다.

장면표·스냅보드 승인 절차는 make-video를 따른다. 이미 받은 사용자 지시를 재질문하지 않고 승인 기록을 지어내지 않는다. 영상 제작은 외부 업로드·게시 권한을 포함하지 않는다.
