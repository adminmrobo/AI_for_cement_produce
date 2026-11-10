# 그림 명세 — 온도를 바꿨는데, 품질은 왜 나중에 달라질까?

| 항목 | 내용 |
|---|---|
| 페이지 | `process_lag.html` |
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
| ☐ | `H00_late_report.webp` | 「왜」 섹션 세 가지 비용 아래 |
| ☐ | `H01_three_clocks.webp` | ① 칸 첫 문단 아래 |
| ☐ | `H02_slide_overlay.webp` | ② 칸 첫 문단 아래 |
| ☐ | `H03_delay_shadow.webp` | ③ 칸 첫 문단 아래 |
| ☐ | `G01_kiln_journey.webp` | 시멘트 이야기 ① 상자 안 |
| ☐ | `G02_37min_28days.webp` | 시멘트 이야기 ② 상자 안 |
| ☐ | `G03_kiln_restart.webp` | 시멘트 이야기 ③ 상자 안 |

## 그림별 지시문

### COVER — 표지 (먼저 받아서 그림체 확인)

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/COVER.webp` (1600 × 900, 16:9) · 공유 미리보기용 `img/COVER_og.webp` (1200 × 630으로 잘라서) |
| 들어가는 곳 | 페이지 맨 위 표지. 파일이 없으면 캐릭터 그림으로 대신 보임 |
| 대체 글 (alt) | 밤의 시멘트 공장 관제실에서 네 캐릭터가 시계 세 개와 늦게 도착하는 품질 성적표를 바라보는 표지 |

**Genspark에 붙여 넣기 ↓**
```
교육용 웹페이지의 표지 그림 1장을 만들어 줘.
- 비율 16:9, 1600 × 900 이상
- 첨부한 참고 이미지의 네 캐릭터를 같은 그림체·같은 외형으로
- 그림 안에 글자·숫자·로고를 넣지 말 것 (제목 「온도를 바꿨는데, 품질은 왜 나중에 달라질까?」은 웹페이지가 따로 씀)
아래 영어 프롬프트를 그대로 써 줘.

Wide 16:9 cover illustration for an educational web page about a cement plant and AI.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Night-time cement plant control room, purple ambient light with warm orange kiln glow through the window.
Scene: Three wall clocks of different sizes above a control desk; through the window a glowing rotating kiln; a quality report card is travelling slowly on a conveyor toward the room.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, thinking with a hand on chin;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, surprised, looking at the clocks;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), holding a magnifying glass toward the conveyor;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, calculating on its abacus.
Leave calm empty space in the lower-left corner for a small label chip.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### H00_late_report — 손잡이를 돌린 순간과 결과가 도착하는 순간

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/H00_late_report.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 「왜」 섹션 세 가지 비용 아래 |
| 대체 글 (alt) | 가마 앞에서 조수가 온도 손잡이를 올리는데, 품질 성적표를 든 초파리 연구원이 아직 멀리 컨베이어 끝에서 걸어오는 장면 |


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
Scene: Left: a long rotating cement kiln glowing orange and a control panel. A long conveyor belt runs from the kiln to the far right where a small lab building stands. A large sand-timer hovers above the belt in the middle.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, turning a big glowing temperature dial on a kiln control panel with excitement;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), far away at the end of a long conveyor belt, walking slowly toward her carrying a quality report card (blank paper).
Visual idea to make obvious at a glance: the action (dial turned) happens now on the left, while the result (report card) is still far away on the right: cause and effect are separated by travel time
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### H01_three_clocks — 기록 속도가 다른 세 개의 시계

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/H01_three_clocks.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ① 칸 첫 문단 아래 |
| 대체 글 (alt) | 빠르게 째깍거리는 작은 시계, 중간 시계, 느린 큰 시계 세 개가 벽에 걸려 있고 각 시계 아래로 점의 간격이 다른 기록 종이가 나오는 장면 |


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
Scene: A wall with three wall clocks of different sizes: a small fast clock with a green rim, a medium clock with a blue rim, a big slow clock with an orange rim. Under each clock a paper tape comes out: the green tape has many dense dots, the blue tape fewer dots, the orange tape only a few big dots. The three tapes have very different lengths.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, looking up at three clocks with a puzzled face, holding three paper strips;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, trying to staple the three paper strips together side by side, carelessly.
Visual idea to make obvious at a glance: three recorders tick at different speeds, so row 2 of each tape is not the same moment
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### H02_slide_overlay — 온도 필름을 옆으로 밀어 품질 물결과 겹쳐 보기

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/H02_slide_overlay.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ② 칸 첫 문단 아래 |
| 대체 글 (alt) | 투명한 필름에 그린 초록 물결을 조수가 옆으로 밀어, 아래 종이의 주황 점 물결과 겹쳐 맞추는 장면 |


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
Scene: On a light table lies a paper with an orange wavy line made of dots (quality). On top, a transparent film with a green smooth wavy line (temperature) is being slid sideways. A ruler along the top edge has tick marks (no numbers). At the current position the green wave and orange dots overlap perfectly and a small sparkle appears.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, sliding a transparent plastic sheet to the right with both hands;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), peering through a magnifying glass at where the two waves line up;
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, nodding with a pointer.
Visual idea to make obvious at a glance: shifting one signal in time until it lines up with the other
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### H03_delay_shadow — 재가동이 끝나도 품질에는 그림자가 남는다

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/H03_delay_shadow.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | ③ 칸 첫 문단 아래 |
| 대체 글 (alt) | 꺼졌다 다시 켜진 가마 뒤로 긴 그림자가 컨베이어를 따라 시험실까지 늘어진 장면. 초파리 연구원이 그림자 끝을 가리킨다 |


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
Scene: A cement kiln that has just been restarted (flame lit again, a small green RUN lamp on). Behind it, along the conveyor belt toward the quality lab, stretches a long grey shadow like an evening shadow. Quality sample cups sitting on the belt inside the shadow look pale and weak; cups beyond the shadow look healthy and bright.
Characters:
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), pointing at the far end of the long shadow with a serious face;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, cheerfully pointing at the restarted kiln as if everything is fine.
Visual idea to make obvious at a glance: even after the sensors say normal, products made during startup are still travelling down the line for a while
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G01_kiln_journey — 원료의 여행 — 칸마다 시간이 걸린다

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G01_kiln_journey.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ① 상자 안 |
| 대체 글 (alt) | 원료 가루가 예열탑을 지나 기울어진 회전 가마 속을 굴러 내려가 클링커가 되고, 단계마다 모래시계가 떠 있는 공장 단면 그림 |


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
Scene: Cutaway factory: LEFT a tall preheater tower with powder falling down, CENTER a long inclined rotating kiln with flame at the low end and powder tumbling down inside becoming grey round lumps (clinker), RIGHT a cooler and a ball mill, far right a small lab with a test tube rack. Small hourglasses float above each stage.
Characters:
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, riding along on a raw-material cart like a tourist, holding a small hourglass.
Visual idea to make obvious at a glance: material travels through stages and each stage takes time
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G02_37min_28days — 37분(공정 반응)과 28일(강도 시험 대기)

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G02_37min_28days.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ② 상자 안 |
| 대체 글 (alt) | 왼쪽에는 주방 타이머와 가마, 오른쪽에는 칸이 많은 달력과 물통 속 시험체가 놓인 대비 그림 |


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
Scene: Split scene. LEFT half: a kiln and a kitchen timer with a short ring (short wait). RIGHT half: a big wall calendar with many squares and a water curing tank holding rows of small grey rectangular test bars, and a compression press machine waiting.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, standing in the middle, pointing left and right with both hands;
  a girl researcher with long pink hair in two round buns and a navy streak, blue eyes, lavender hoodie under a white lab coat, jeans, on the right, peeking into a water tank full of small mortar bars.
Visual idea to make obvious at a glance: a short process delay versus a long month-long strength test wait
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

### G03_kiln_restart — 재가동은 천천히 — 내화벽돌과 코팅

| 항목 | 내용 |
|---|---|
| 파일 이름 | `img/G03_kiln_restart.webp` (가로 1600, 16:7 · WebP 품질 80 안팎) |
| 들어가는 곳 | 시멘트 이야기 ③ 상자 안 |
| 대체 글 (alt) | 내화벽돌로 안을 덮은 가마 단면에서 재가동 버너가 켜지고, 온도계 바늘이 천천히 올라가며, 박사가 운전 기록장에 적는 장면 |


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
Scene: Cutaway of a kiln shell showing a lining of heat-resistant bricks with a thin crusty coating layer. The burner is relit with a small flame. A big analog thermometer needle rises slowly. Some bricks show tiny cracks warning what happens if heated too fast.
Characters:
  a chibi scientist with thin teal rectangular glasses, black hair with one white streak and a short tied-back ponytail, white lab coat over a black vest and tie, writing in an operation log book;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, impatiently pressing a big button, being held back by the fly;
  an anthropomorphic fruit fly researcher with a black body, big red compound eyes, a blue helmet with a gold stripe and pink and blue cables behind it, white lab coat over a black vest, black gloves and clear wings, small (about one third of the scientist's height), holding the robot's arm, shaking head.
Visual idea to make obvious at a glance: restarting must be slow to protect the bricks; the first output after restart is unstable
Composition: one clear focal point in the center, simple uncluttered background, all faces and hands away from the edges.
No text, no letters, no numbers, no logos, no chemical formulas written anywhere, no weapons, no cigarettes, no alcohol, no blood, no real brands, no real company names, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```
