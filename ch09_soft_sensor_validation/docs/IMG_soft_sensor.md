# 그림 명세 — 시험 결과를 기다리지 않고 품질을 알 수 있을까?

| 항목 | 내용 |
|---|---|
| 페이지 | `soft_sensor.html` |
| 그림 수 | 표지 1장 + 본문 7장 (본문 16:7, 가로 1600 · WebP) |
| 넣는 법 | 받은 그림을 `img/` 폴더에 아래 파일 이름 그대로 넣으면 "그림 자리"에 바로 나옴 (한 장 200KB 안팎, 페이지 전체 600KB 이하 권장) |
| 순서 | ① 표지를 먼저 받아 그림체를 확인 → ② 나머지는 표지를 참고 그림으로 함께 올려 3~5장씩 요청 |
| 참고 이미지 | 네 캐릭터 기본 그림 (`adminmrobo/fruitfly-lab-expressions`) |
| 공통 금지 | 그림 안 글자·숫자·화학식·로고·상표, 실존 인물 얼굴, 흰 둥근 로봇 머리, 금화 |

**고칠 때 (같은 대화에서):** `Same characters, same art style and composition. Change only: {고칠 점}. Still no text.`

## 저장 이름 체크리스트

| ✓ | 파일 | 들어가는 곳 |
|---|---|---|
| ☐ | `COVER.webp` · `COVER_og.webp` | 표지 · 공유 미리보기 |
| ☐ | `K00_quality_forecast.webp` | 「왜」 섹션 단계 카드 아래 |
| ☐ | `K01_problem_card.webp` | ① 칸 첫 문단 아래 |
| ☐ | `K02_forest_vote.webp` | ② 칸 첫 문단 아래 |
| ☐ | `K03_split_calendar.webp` | ③ 칸 첫 문단 아래 |
| ☐ | `G04_lab_tests.webp` | 시멘트 이야기 ④ 상자 안 |
| ☐ | `G05_strength_test.webp` | 시멘트 이야기 ⑤ 상자 안 |
| ☐ | `G06_raw_change.webp` | 시멘트 이야기 ⑥ 상자 안 |

## 그림별 지시문

### COVER — 표지 (먼저 받아서 그림체 확인)

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/COVER.webp` (1600 × 900, 16:9) · 공유 미리보기용 `img/COVER_og.webp` (1200 × 630으로 잘라서) |
| 들어가는 곳 | 페이지 맨 위 표지. 파일이 없으면 캐릭터 그림으로 대신 보임 |
| 대체 글 (alt) | 관제실 화면에 실제 품질 선과 AI 예측 점선이 나란히 흐르고, 네 캐릭터가 달력의 과거 칸과 미래 칸 사이에 선을 긋는 표지 |

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 표지 그림 1장을 만들어 줘.
- 비율 16:9, 1600 × 900 이상
- 첨부한 참고 이미지의 네 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고를 넣지 말 것 (제목 「시험 결과를 기다리지 않고 품질을 알 수 있을까?」은 웹페이지가 따로 씀)
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:9 cover illustration for an educational web page about a cement plant and AI.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Night-time cement plant control room, purple ambient light with warm orange kiln glow through the window.
Scene: A big control room screen shows a solid green line (actual) and a dotted orange line (prediction) running side by side; a tall wall calendar is divided by a bright vertical line into a past side and a future side.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, pointing at the screen like a teacher;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, reporting with a clipboard;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), drawing the vertical line on the calendar;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, showing a chart on its own screen proudly.
Leave calm empty space in the lower-left corner for a small label chip.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### K00_quality_forecast — 소프트센서는 품질 예보

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/K00_quality_forecast.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 「왜」 섹션 단계 카드 아래 |
| 대체 글 (alt) | 날씨 예보관처럼 공장 그래프 앞에 선 조수가 품질을 예보하고, 뒤에서 초파리 연구원이 실측 결과지를 들고 오는 장면 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: A TV-studio style weather forecast set inside a cement plant control room. Instead of a map, the big screen shows a smooth green line with a dotted orange forecast line continuing it, and a sunny icon above a cement bag. A small lab building is visible through the window.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, standing like a TV weather forecaster in front of a big screen with a sun icon and a cement bag icon;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), walking in from the side carrying a lab result clipboard (blank).
Visual idea to make obvious at a glance: predicting a not-yet-measured value from information known now, then checking against the real measurement
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### K01_problem_card — 학습표 한 줄 = 문제 카드 한 장

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/K01_problem_card.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ① 칸 첫 문단 아래 |
| 대체 글 (alt) | 품질 측정 순간마다 한 장씩 만든 문제 카드 묶음. 앞면에는 과거 센서 아이콘, 뒷면에는 정답 게이지가 있고 조수가 카드를 넘기는 장면 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: A desk with a tall stack of flash cards. The front of each card shows three small icons (thermometer, oxygen bubble, a short wave line) drawn on a timeline arrow pointing to the past. The back of a flipped card shows a big check mark and a quality gauge needle. A clock on the desk shows the past side shaded green and the future side shaded red.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, flipping through a stack of flash cards;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, trying to peek at the back of a card, being caught.
Visual idea to make obvious at a glance: each quality measurement becomes one question card: front = past sensor info, back = answer
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### K02_forest_vote — 랜덤포레스트 — 나무들의 평균

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/K02_forest_vote.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ② 칸 첫 문단 아래 |
| 대체 글 (alt) | 숲 속 나무 여러 그루가 각자 조금씩 다른 게이지 팻말을 들고, 주판봇이 그 평균을 계산하는 장면 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: A small cartoon forest of about seven trees with friendly faces; each tree holds up a little sign showing a gauge with a slightly different needle position. In the center the robot combines them into one big gauge whose needle sits in the middle of all of them.
Characters:
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, standing in the center with an abacus, averaging the trees' answers;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, watching amazed.
Visual idea to make obvious at a glance: many slightly different trees vote and their average is steadier than any single tree
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### K03_split_calendar — 섞어서 나누기 vs 과거로 배우고 미래로 시험

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/K03_split_calendar.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ③ 칸 첫 문단 아래 |
| 대체 글 (alt) | 왼쪽 달력은 파랑·주황 스티커가 뒤섞이고, 오른쪽 달력은 앞쪽 파랑, 회색 띠, 뒤쪽 주황으로 깔끔하게 나뉜 그림 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: Two big calendars side by side. LEFT calendar: blue and orange stickers scattered randomly across all days. RIGHT calendar: the first days all blue stickers, then a narrow grey empty band, then the last days all orange stickers.
Characters:
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), on the right side, drawing a firm vertical line on the calendar with a marker;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, on the left side, shaking calendar squares in a bowl like a lottery.
Visual idea to make obvious at a glance: random shuffling mixes yesterday and tomorrow; time-ordered split keeps the future unseen with a gap in between
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G04_lab_tests — 시험실의 다섯 가지 측정

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G04_lab_tests.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ④ 상자 안 |
| 대체 글 (alt) | 시멘트 시험실 책상 위에 성분 분석기, 분말도 측정기, 응결 시험 바늘, 압축강도 시험기가 차례로 놓이고 앞쪽엔 작은 시계, 끝엔 큰 달력이 떠 있는 그림 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: A long cement laboratory bench with five stations from left to right: an X-ray analyzer box with a small sample cup, a simple glass titration setup, an air-permeability fineness tester with a small tube, a setting-time needle apparatus over a ring of paste, and a big compression testing machine. Above the first stations float small stopwatches; above the last station floats a large calendar.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, walking along the bench explaining each instrument.
Visual idea to make obvious at a glance: some lab results come quickly, the strength result takes weeks
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G05_strength_test — 28일 압축강도 시험의 네 단계

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G05_strength_test.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ⑤ 상자 안 |
| 대체 글 (alt) | 모르타르 섞기, 길쭉한 틀에 넣기, 물속 양생, 눌러서 부수기의 네 칸 만화 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: A four-panel comic in one wide image (panels left to right, no text): 1) mixing grey mortar in a bowl with sand, 2) pressing mortar into a long rectangular three-bar steel mould, 3) bars resting in a water tank with a calendar behind, 4) a compression machine pressing a bar until it cracks.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, appearing in each panel doing the step.
Visual idea to make obvious at a glance: mix, mould, cure under water, crush
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G06_raw_change — 원료·연료·센서가 바뀌면 다시 배운다

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G06_raw_change.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ⑥ 상자 안 |
| 대체 글 (alt) | 석회석 광산의 줄무늬 지층, 석탄과 폐타이어 연료 더미, 온도계를 바꾸는 주판봇, 다시 배우기 버튼을 누르는 조수가 한 장면에 모인 그림 |


**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지 본문에 넣을 가로 그림 1장을 만들어 줘.
- 비율 16:7 (가로로 긴 그림), 가로 1600px 이상
- 첨부한 참고 이미지의 캐릭터를 같은 그림체·같은 외형으로 (참고 이미지: fruitfly-lab-expressions 기본 그림)
- 그림 안에 글자·숫자·로고·화학식을 넣지 말 것
- 시멘트를 처음 배우는 학생이 한눈에 이해할 수 있게 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:7 educational illustration for a web lesson.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy, friendly, slightly humorous mood; clear readable shapes; soft purple lab light with warm orange accents.
Scene: Left: a limestone quarry wall with clearly different colored rock layers. Center: a fuel pile mixing coal lumps and old tires. Right: the control room monitor with a circular refresh arrow.
Characters:
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, replacing a thermometer sensor with a wrench;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, pressing a big refresh button on a monitor showing the soft sensor graph.
Visual idea to make obvious at a glance: when the plant changes, the model must be re-checked and retrained
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```
