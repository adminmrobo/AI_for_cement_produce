# 표지 지시문 — 00 목차 「AI를 활용한 시멘트 공정 최적화」

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_index (= cover_series) · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | 목차 — 낮의 연구실 전경. 시멘트 공장 위층의 밝은 강의 연구실, 창밖으로 낮의 사일로·컨베이어 (멀리 작게) |
| 주제 은유 | 작업대 위 시소 모형 셋(재료비↔강도 · 연료↔덜 구워진 정도 · 폐자원 연료↔생산량)과 벽의 개념 지도(동그라미와 선만)를 가로지르는 초록 경계선 한 줄 — "데이터로 의사결정 경계선을 찾는다" |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 벽 개념 지도의 초록 경계선을 가리킴 / 조수: 오른쪽 옆에서 빈 점수판(줄무늬, 글자 없음)을 듦 / 초파리: 왼쪽에서 오른쪽을 보며 의자 위에서 첫 시소를 돋보기로 들여다봄(의심) / 주판봇: 오른쪽에서 왼쪽을 보며 나무 주판을 들고 개념 지도를 올려다봄(확신) |
| 대체 글 (alt) | 밝은 낮의 연구실에서 네 캐릭터가 작업대 위 시소 모형 셋과 벽 개념 지도의 초록 경계선을 바라보는 강좌 목차 표지 |
| 앞 표지와 다른 점 | ch08(밤의 가마 제어실·컨베이어)·ch09(밤의 모니터 그래프)와 겹치지 않게 **낮**, 가마 클로즈업 대신 멀리 보이는 사일로, 주제 소품은 시소 모형 셋. 초파리 돋보기 포즈는 ch08과 같으므로 의자 위·시소 쪽으로 바꿈 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions` @ 86d04ac — 박사·조수·초파리 설정샷 k02~k04, 주판봇 v2 기본 표정 E13).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright daytime classroom laboratory on the upper floor of a cement plant; through a wide window behind, tall pale-grey cement silos and a long conveyor stand under a clear blue sky, small and far away; inside, a long white workbench with three small wooden seesaw models in a row, each seesaw balancing a different pair of objects: a small sack of grey powder against a sturdy grey test cube, a tiny blue flame against a glowing clinker pebble, a small rubber tire piece against a stack of tiny cement bags; on the white wall a large concept map made only of circles and connecting lines (no writing), with a single thin green line running across it like a boundary.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center pointing up at the green boundary line on the concept map;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the right side holding a small blank scoreboard with empty striped rows, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, small (about 0.41 of the scientist's height), on the left facing right, standing on a stool and leaning toward the first seesaw with a magnifying glass, one eye narrowed, doubtful;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, looking up at the concept map, confident.
Visual metaphor of the topic: three balanced seesaws (cheaper on one side, quality on the other) and one green boundary line on the wall map — finding the line where saving cost still keeps quality; no numbers anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the three seesaws and the green boundary line.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no night, no dark room, no neon glow, no white round robot head, no gold coins, no microscope.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

## 받은 뒤 처리 (스킬 18-15)

1. 16:9·가로 1600 이상·글자 없음·네 캐릭터 외형 확인
2. `img/cover_index.webp`(1600×900, 220 KB 이하)와 `img/cover_index_960.webp`(960×540, 110 KB 이하)로 변환
3. `index.html`의 `header#cover`에서 대체 표지(`.lineup`)를 18-14-5 `<picture>` 블록으로 바꾸고 `fallback` 클래스를 뺌
4. `cover_manifest.json`의 `cover_index` 항목을 `path`·`size`·`status: "ok"`로 고침
