# 시멘트 이야기 그림 명세 — 무엇이 강도를 정하고, 얼마에 만들 것인가

| 항목 | 내용 |
|---|---|
| 페이지 | `cement_strength_cost.html` |
| 대상 | 본문의 "여기서 잠깐! · 시멘트 이야기" 상자마다 그림 1장 |
| 새로 그릴 그림 | 7장 (16:7, 가로 1600 · WebP) |
| 이미 있는 그림을 상자 안으로 옮긴 것 | ①(F11) |
| 넣는 법 | 받은 그림을 `img/` 폴더에 표의 파일 이름 그대로 넣으면 상자 안 "그림 자리"에 바로 나옴 |
| 참고 이미지 | 네 캐릭터 기본 그림(`adminmrobo/fruitfly-lab-expressions`) + 이번 판의 F06(클링커 4형제 꼬마들)을 Genspark에 함께 올리기 |
| 공통 금지 | 그림 안 글자·숫자·화학식·로고·상표, 실존 인물 얼굴, 흰 둥근 로봇 머리, 금화 |

**그리는 원칙** — 이 그림들은 장식이 아니라 상자 글의 '설명 그림'이다. 각 항목의 **꼭 보여야 할 것**이 한눈에 읽혀야 하고, 학생이 글을 읽기 전에 그림만 봐도 무슨 이야기인지 짐작할 수 있어야 한다. 한 그림 안에서 왼쪽 → 오른쪽 순서로 이야기가 흐르게 한다.

**고칠 때 (같은 대화에서):** `Same characters, same art style and composition. Change only: {고칠 점}. Still no text.`

## 그림 목록

| 상자 | 파일 | 그림 |
|---|---|---|
| ② | `Y02_bogue_lego.webp` | 보그 계산 — 산화물 블록으로 광물을 거꾸로 세기 |
| ③ | `Y03_28day_press_thumb.webp` | 28일 강도와 42.5 MPa |
| ④ | `Y04_six_variables_stairs.webp` | 워터폴 여섯 변수 — 시멘트 쪽 얼굴들 |
| ⑤ | `Y05_ball_mill_power.webp` | 분쇄기 — 쇠공이 구르는 거대한 원통 |
| ⑥ | `Y06_xrf_report.webp` | 산화물 성적표 — 분석기에서 매일 나오는 숫자 |
| ⑦ | `Y07_kiln_temp_dial.webp` | 가마 온도 — 너무 낮아도, 너무 높아도 |
| ⑧ | `Y08_slag_supply_blend.webp` | 슬래그 수급과 혼합 시멘트 |

## 그림별 지시문

### 시멘트 이야기 ② · Y02_bogue_lego — 보그 계산 — 산화물 블록으로 광물을 거꾸로 세기

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y02_bogue_lego.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ② 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 색깔별 블록 더미와 그 블록으로 만든 클링커 4형제 모형 사이에 거꾸로 향하는 화살표가 그려진 그림 |


**꼭 보여야 할 것**
- 왼쪽: 색깔별 블록 더미 4개(빨강 칼슘·파랑 규소·노랑 알루미늄·초록 철) + 길이만 다른 색 막대 성적표
- 오른쪽: 블록으로 만든 클링커 4형제 모형 — C₃S는 빨강 셋+파랑 하나 비율로 보이게
- 모형에서 블록 더미 쪽으로 '거꾸로' 향하는 큰 곡선 화살표
- 펼쳐진 조립 설명서(블록 그림만)
- 글자·숫자·화학식 금지

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "보그 계산 — 산화물 블록으로 광물을 거꾸로 세기".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A tabletop scene. LEFT: four piles of toy-like building bricks sorted by color — a big red pile (calcium), a medium blue pile (silicon), a small yellow pile (aluminum), a small green pile (iron) — next to a paper report sheet showing only four colored horizontal bars of different lengths (no numbers). RIGHT: four finished brick models standing on display stands, each in the shape of the four clinker mascots: the sturdy dark-grey one built mostly of red with some blue bricks (three red per one blue), the olive one built of red and blue (two red per one blue), a small purple one built of red and yellow, and the reddish-brown one built of red, yellow and green. A large curved arrow goes from the finished models BACK to the brick piles, showing reverse counting, and an instruction booklet lies open with simple brick diagrams.
The small clinker mineral mascots, when they appear, are the four clinker mineral mascots from the earlier picture: small gem-like bodies with simple faces — a sturdy dark-grey confident one (main player), a sleepy olive-green one holding a sprout pot (slow one), a tiny hyper purple one with steam puffs (quick-tempered youngest), a reddish-brown one holding a paint brush (iron one).
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, in the middle holding a pencil, drawing an arrow backward from the models to the brick piles;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, at the left sorting colored bricks into piles.
The one idea a student must get at a glance: Bogue calculation: knowing how many bricks of each color you have, count backward how many of each model could have been built.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ③ · Y03_28day_press_thumb — 28일 강도와 42.5 MPa

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y03_28day_press_thumb.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ③ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 압축 시험기가 28일 키운 시편을 누르고, 주판봇 손가락 끝 위에 사람 여섯이 서 있는 그림 |
| 메모 | F/07판 Z08과 비슷하되 더 단순하게 |

**꼭 보여야 할 것**
- 왼쪽: 압축 시험기가 시편을 눌러 금이 가고, 다이얼 바늘이 빨간 표시를 막 넘음
- 뒤쪽: 4줄×7칸 달력이 모두 체크됨(28일) + 다 자란 화분
- 오른쪽: 주판봇 손가락 끝 작은 네모(1 cm²) 위에 사람 여섯 — 약 430 kg
- 숫자 없음

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "28일 강도와 42.5 MPa".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: LEFT: a compression testing press squeezing a small grey cement cube between two steel plates; small cracks and crumbs; a round dial gauge whose needle has just passed a thin red mark. Behind it, a wall calendar with four rows of seven squares, all checked off with tick marks, and a small grown tree in a pot beside the calendar. RIGHT: a close-up of the robot's fingertip shown as a tiny square tile with six tiny cheerful cartoon people standing on it, plus a dotted square outline around the fingertip to show 'this small area'.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, operating a compression press on the left, watching the dial;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, on the right holding up one grey robot finger on which six tiny cartoon people stand, sweating but smiling.
The one idea a student must get at a glance: 28 days of growing, then press: the minimum line means a fingertip-sized area holds about six adults.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ④ · Y04_six_variables_stairs — 워터폴 여섯 변수 — 시멘트 쪽 얼굴들

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y04_six_variables_stairs.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ④ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 기준 바닥에서 출발해 분말도·C₃S 계단은 올라가고 슬래그·유리석회 계단은 내려가며, 석고와 가마 불꽃 캐릭터를 지나 도착 발판에 이르는 계단 그림 |


**꼭 보여야 할 것**
- 왼쪽 바닥(기준값)에서 출발해 오르내리는 돌계단 — 워터폴 그래프 모양
- 계단마다 변수 캐릭터: 분쇄기(분말도)↑ · C₃S↑ · 슬래그 더미(거북이 등껍질)↓ · 외톨이 석회(유리석회)↓ · 작은 산 위의 석고(SO₃) 평평 · 가마 불꽃(온도) 물음표
- 오른쪽 끝 빛나는 도착 발판(예측값)
- 글자·숫자 없음

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "워터폴 여섯 변수 — 시멘트 쪽 얼굴들".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A staircase that goes up and down across the picture like a waterfall chart made of stone steps. On each step stands one small character representing a variable: (1) a grinding mill wearing a tiny cape, pouring very fine powder — step goes UP; (2) the sturdy dark-grey C3S mascot flexing — step goes UP; (3) a cream slag sand-pile mascot carrying a tortoise shell — step goes DOWN; (4) a lonely small off-white lime ball looking undercooked — step goes DOWN; (5) a small white gypsum rock mascot standing on top of a tiny hill — a level step; (6) a small flame mascot from the kiln — a tricky step with a tiny question mark floating over it. The staircase starts from a flat ground level on the left (the base value) and ends at a glowing finish platform on the right (the prediction).
The small clinker mineral mascots, when they appear, are the four clinker mineral mascots from the earlier picture: small gem-like bodies with simple faces — a sturdy dark-grey confident one (main player), a sleepy olive-green one holding a sprout pot (slow one), a tiny hyper purple one with steam puffs (quick-tempered youngest), a reddish-brown one holding a paint brush (iron one).
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, at the bottom left with a clipboard, introducing the six like a host;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, at the far right top holding an abacus, at the final step.
The one idea a student must get at a glance: each variable is a step up or down from the base level to the final prediction; these are the six faces from the cement world.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ⑤ · Y05_ball_mill_power — 분쇄기 — 쇠공이 구르는 거대한 원통

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y05_ball_mill_power.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ⑤ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 쇠공이 구르는 볼 밀 절단면에서 클링커가 가루가 되고, 슬래그 덩어리는 불꽃이 튀며, 위의 전기 계량기가 빠르게 돌고 주판봇이 긴 고지서를 든 그림 |


**꼭 보여야 할 것**
- 가로로 누운 회전 원통(볼 밀)의 절단면, 안에서 쇠공 수십 개가 구르며 클링커 구슬을 부숨
- 왼쪽으로 구슬이 들어가고 오른쪽으로 고운 가루가 나와 사일로로
- 크림색 슬래그 덩어리는 부딪칠 때 불꽃이 튐 — 더 단단해서 갈기 어려움
- 위쪽 굵은 전선과 빠르게 도는 전기 계량기, 주판봇의 긴 전기 요금 고지서
- 글자·숫자 없음

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "분쇄기 — 쇠공이 구르는 거대한 원통".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A large cutaway of a horizontal rotating steel drum (ball mill) lying on its side across the center. Inside, dozens of shiny steel balls tumble and cascade as the drum turns, smashing dark-grey clinker marbles that enter on the left into fine grey powder that flows out on the right into a silo. A few cream slag chunks inside make bright sparks when hit, to show they are harder to grind. Above the mill, thick power cables lead to a large electricity meter with a fast-spinning disc and lightning-bolt icons. Sound effect stars and wave lines show the loud noise.
Characters:
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, at the right holding a long paper electricity bill that unrolls to the floor, eyes worried;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), at the left peeking through an inspection hatch on the drum, ears covered from the noise.
The one idea a student must get at a glance: grinding is where the plant spends the most electricity; slag is harder to grind, so finer powder and more slag both cost power.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ⑥ · Y06_xrf_report — 산화물 성적표 — 분석기에서 매일 나오는 숫자

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y06_xrf_report.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ⑥ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 가루를 눌러 만든 시편을 분석기에 넣으면 색 막대 성적표가 나오고, 옆의 더 큰 분석기는 시간이 더 걸리는 모습을 보여 주는 실험실 그림 |
| 메모 | 장비 상표 금지 |

**꼭 보여야 할 것**
- 왼쪽: 가루를 동전처럼 눌러 만든 납작한 시편과 작은 프레스
- 가운데: 상자형 분석기(XRF, 상표 없음) 화면에 색 막대 6개 — 성분 비율만 보여 줌
- 오른쪽: 더 크고 복잡한 분석기(XRD) 화면에 봉우리 있는 곡선 + 모래시계·커피잔(시간이 더 걸림)
- 뒤쪽 게시판에 매일 붙는 성적표들
- 상표·글자·숫자 금지

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "산화물 성적표 — 분석기에서 매일 나오는 숫자".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A tidy quality-control lab bench. LEFT: a small hydraulic press that has just pressed grey powder into a flat round pellet like a coin. CENTER: a compact boxy analysis machine (X-ray fluorescence analyzer, generic design, no brand) with a drawer open, and a screen showing six colored bars of different lengths (red, blue, yellow, green, white, purple) — no labels, no numbers. RIGHT: a second, larger and more complex machine (X-ray diffraction, generic design) with a screen showing a wiggly line with a few peaks, and beside it a small hourglass and a coffee cup to show it takes longer. Behind, a corkboard with daily sheets pinned in a row like a calendar strip.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, at the left holding a flat round pressed powder pellet with tweezers, about to put it into a machine;
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, at the right pointing at the screen of a second, bigger machine.
The one idea a student must get at a glance: every day a quick machine tells how much of each element is in the powder; minerals themselves need a slower machine, so the plant converts the daily numbers into ratios.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ⑦ · Y07_kiln_temp_dial — 가마 온도 — 너무 낮아도, 너무 높아도

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y07_kiln_temp_dial.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ⑦ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 가마 온도를 큰 손잡이로 표현하고, 낮으면 덜 익은 석회, 알맞으면 건강한 클링커, 높으면 연료비가 날아가고 벽돌이 부서지는 세 구역 그림 |
| 메모 | 돈·동전 그림 대신 빈 지갑과 연료 방울로 비용 표현 |

**꼭 보여야 할 것**
- 왼쪽(너무 낮음, 파랑): 덜 익은 밥알·외톨이 석회, 약한 불, 푸석한 클링커
- 가운데(알맞음, 금빛): 건강한 검회색 클링커와 기뻐하는 C₃S
- 오른쪽(너무 높음, 빨강): 연료통이 빠르게 비며 연료 방울이 튀고 빈 지갑이 떠 있음, 가마 안 내화벽돌이 부서짐
- 박사가 배의 키 같은 큰 온도 손잡이를 신중히 잡고 있음
- 뒤쪽: 품질이 다른 원료 더미 두 개를 보는 운전원 — 원료 따라 온도를 맞춤(교란의 씨앗)

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "가마 온도 — 너무 낮아도, 너무 높아도".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A three-zone scene laid out like a dial from left to right. LEFT ZONE (too low, bluish): a rice cooker with half-raw rice and lonely white lime balls, and a weak little flame — the clinker marbles look pale and crumbly. CENTER ZONE (just right, warm golden): healthy dark-grey clinker marbles glowing, the sturdy C3S mascot happy. RIGHT ZONE (too high, red-hot): a fuel tank draining fast with many fuel droplets flying out and an empty open wallet floating beside it, and the kiln's inner firebricks cracking and crumbling. Behind the doctor, two raw-material piles of different quality (one bright and even, one dull and uneven) with an operator silhouette glancing at them, to show the operator adjusts the temperature by the raw material of the day.
The small clinker mineral mascots, when they appear, are the four clinker mineral mascots from the earlier picture: small gem-like bodies with simple faces — a sturdy dark-grey confident one (main player), a sleepy olive-green one holding a sprout pot (slow one), a tiny hyper purple one with steam puffs (quick-tempered youngest), a reddish-brown one holding a paint brush (iron one).
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, at the center holding a big round temperature knob like a ship's wheel, thinking carefully;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), at the right looking through a small blue-glass viewing window at the flame inside the kiln.
The one idea a student must get at a glance: kiln temperature is a careful knob: too low gives raw lime, too high burns money and bricks; operators set it by the day's raw material.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### 시멘트 이야기 ⑧ · Y08_slag_supply_blend — 슬래그 수급과 혼합 시멘트

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/Y08_slag_supply_blend.webp` (가로 1600, 16:7) |
| 들어가는 곳 | 시멘트 이야기 ⑧ 상자 안, 제목 바로 아래 |
| 대체 글 (alt) | 제철소의 슬래그 관 하나를 시멘트 공장 세 곳이 나눠 쓰려 하고 값 화살표가 오르며, 혼합 시멘트 포대 위 탄소 구름이 보통 포대보다 작은 그림 |


**꼭 보여야 할 것**
- 왼쪽 위 제철소에서 나오는 슬래그 관 하나를 시멘트 공장 세 곳이 함께 끌어가려는 모습(수량 한정·경쟁)
- 관 옆 표지판에 위로 향한 큰 화살표(값 상승, 숫자 없음)
- 오른쪽 위 석탄 화력발전소에서 고운 재(플라이애시)가 다른 공장으로 감
- 오른쪽 아래: 보통 포대 위 큰 회색 구름 vs 혼합 포대(잎 아이콘) 위 작은 구름 — 탄소 감소
- 주판봇이 오르는 화살표를 보며 땀 흘림

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 '여기서 잠깐' 설명 상자에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것 (기호 ✔ ? 화살표는 괜찮음)
- 시멘트를 처음 배우는 학생이 그림만 보고도 이야기를 짐작할 수 있게, 왼쪽에서 오른쪽으로 읽히게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 explanatory educational illustration for a web lesson box titled (do not write it in the image) "슬래그 수급과 혼합 시멘트".
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright, friendly, slightly humorous; clear readable shapes; story reads from left to right.
Scene: A bird's-eye miniature landscape. At the top left a steel plant with a blast furnace; one single pipe of cream slag granules runs from it and splits toward three different cement plants, each with a hopper, and the three plants' little workers are reaching for the slag at the same time (competition). A signpost near the pipe shows a big upward arrow (price rising, no numbers). At the top right a coal power plant with a chimney sends a second small stream of very fine light-grey ash (fly ash) into one cement plant. In the lower right, two cement bags side by side: an ordinary grey bag with a large dark CO2-like cloud above it, and a cream blended bag with a much smaller cloud and a green leaf icon.
Characters:
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, at the bottom center watching a price arrow sign rising, sweating;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, at the right holding a cream slag-blend bag with a green leaf icon.
The one idea a student must get at a glance: slag only comes as fast as steel is made, so when many plants want it the price rises; blended cements cut carbon.
Composition: keep every important element large and clearly separated; simple background; nothing important touching the edges; leave a little calm space at the top.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```
