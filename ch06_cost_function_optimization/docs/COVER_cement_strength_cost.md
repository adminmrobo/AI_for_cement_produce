# 표지 지시문 — 무엇이 강도를 정하고, 얼마에 만들 것인가

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_cs · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | D 현장 — 밤의 시멘트 공장 관제실 (창밖에 예열탑·킬른 실루엣, 연구실 보라 조명이 한쪽에서 스며듦) |
| 주제 은유 | 가운데 탁자 위 커다란 놋쇠 저울: 한쪽 접시엔 회색 압축강도 시험체(정육면체), 다른 쪽엔 큰 나무 주판. 저울 위 공중에 폭포처럼 계단진 빛 막대(초록·빨강, 글자 없음) |
| 네 캐릭터 포즈 | 박사: 저울 뒤 가운데, 턱에 손 (생각) / 조수: 오른쪽 옆, 태블릿(빈 화면) 들고 저울 눈금을 확인 / 초파리: 왼쪽에서 오른쪽을 보며 시험체 쪽을 손가락으로 가리킴 / 주판봇: 오른쪽에서 왼쪽을 보며 주판알 하나를 반짝 튕겨 보임 |
| 대체 글 (alt) | 밤의 시멘트 공장 관제실에서 네 캐릭터가 강도 시험체와 나무 주판이 올라간 저울을 사이에 두고 마주한 표지 |
| 앞 표지와 다른 점 | 시멘트 강의 시리즈 첫 표지 — 이후 표지는 저울 대신 다른 소품(킬른, 분쇄기 등)을 중심에 둔다 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것 (화면·눈금은 빈 줄무늬로)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night mood, purple light, soft magenta and green fluorescent accents.
Scene: a night control room of a cement plant rendered as part of the same night lab world, large window showing the silhouette of a preheater tower and a long rotary kiln glowing softly, purple lab light spilling in from the left, monitors with blank teal screens.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center with a hand on his chin, thinking;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, on the right side holding a tablet with a blank screen and checking the scale;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, pointing at the concrete cube with one eye narrowed;
  JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, on the right facing left, proudly holding up a wooden abacus and flicking one shiny bead.
Visual metaphor of the topic: a large brass balance scale on the central table, one pan holding a grey concrete compression test cube, the other pan holding a big wooden abacus; above the scale a floating staircase of glowing bars in green and red like a waterfall chart, with no text.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple; the light falls on the scale.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** SKILL 18-15 — 비율·글자·네 캐릭터 외형 확인 → WebP 1600×900(220 KB 이하) → HTML의 `<!-- lab-cover -->` 블록 안 `data-img="cover_cs"` 자리에만 넣는다.
