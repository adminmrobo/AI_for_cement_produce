# 「무엇이 강도를 정하고, 얼마에 만들 것인가」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | cement_strength_cost.html |
| 모드 / 주 앵커 | 교과서 모드 / D 생활·현장: 시멘트 공장 (관제실·분쇄기·킬른) |
| 시즌 | 기본 |
| 대결 | 마진 0 vs 마진 2.9 배합의 1,000배치 미달 수 → 결과 F, 차이 55 vs 480 (42.5%p) |
| 새로 그릴 그림 | P1 2장 · P2 3장 · P3 2장 |
| 재사용 | 표정 18장 (캐릭터 팩 96px, 페이지에 base64로 들어 있음) |
| 그림이 없을 때 | 페이지는 캐릭터 팩 그림 + CSS 대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: 16비트 RPG 픽셀아트, 굵은 외곽선, 2~3단계 명암 (캐릭터 팩 18-3)
- 고정 외형: 캐릭터 팩 18-4 그대로
- 장소: 밤의 시멘트 공장. 관제실(모니터), 분쇄기(볼밀), 회전 킬른, 압축강도 시험기. 연구실 보라 조명을 한쪽에 남긴다
- 장소 영어 묘사: *night control room of a cement plant rendered as part of the same night lab world, purple lab light spilling in from one side*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_cs | L | 1920×1080 | 새로 (COVER_cement_strength_cost.md) | P1 | 맨 위 글 표지 | CSS 대체 표지 + 캐릭터 넷 |
| 1 | sc_cs_hero | E | 1200×800 | 새로 | P1 | 히어로 무대(향후 배경) | 표지 자르기 |
| 2 | cut_cs_lv4 | G | 960×540 | 새로 | P2 | ④칸 컷: 원료 좋은 날 온도를 낮추는 운전원 | 없음(컷 생략) |
| 3 | cut_cs_lv5 | G | 960×540 | 새로 | P2 | ⑤칸 컷: 데이터 지도 밖으로 날아간 별 | 없음 |
| 4 | sc_cs_outro | E | 1200×800 | 새로 | P2 | 아웃트로 무대 | 픽셀 캐릭터 줄 |
| 5 | thumb_cs | I | 600×400 | 새로 (표지 3:2 자르기) | P3 | 목차 카드 | 색 카드 |
| 6 | og_cs | K | 1200×630 | 새로 (표지 자르기) | P3 | 공유 미리보기 | 없음 |
| — | doc_think·front·judge·magic, asst_smile·firm·report·spark, fly_clip·point·arms·magnify·coffee, robo_smile·coin·calc·sigh·happy | A~D | 96 | 재사용 | — | 말풍선·대결·아웃트로 | 기본 표정 |
| — | 그래프·시뮬레이션 | — | — | 코드 | — | Canvas | — |

## 3. 새로 그릴 그림 상세

### 3-1. `sc_cs_hero` — 저울 앞의 네 사람
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 구도 | 가운데 저울(시험체 vs 나무 주판), 왼쪽 초파리(오른쪽 봄), 오른쪽 주판봇(왼쪽 봄), 뒤 가운데 박사, 오른쪽 옆 조수. 중요한 것은 위쪽 62% 안 |
| 피할 것 | 승패 암시, 글자, 실존 브랜드 |
| 대체 글 | 네 캐릭터가 시멘트 시험체와 나무 주판을 단 저울을 바라보는 공장 관제실 장면 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, night control room of a cement plant rendered as part of the same night lab world, a brass balance scale in the center with a grey concrete test cube on one pan and wooden abacus beads on the other, chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak and a small ponytail, white lab coat over black vest and tie, standing at the back center with a hand on his chin, anthropomorphic fruit fly researcher with big red compound eyes and a blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, on the left facing right pointing at the cube, JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, on the right facing left holding a wooden abacus, girl researcher with long pink hair in two round buns and a navy streak, white lab coat over lavender hoodie, jeans, at the side holding a blank tablet, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins
```

### 3-2. `cut_cs_lv4` — 보이지 않는 원인
| 항목 | 내용 |
|---|---|
| 판 · 크기 | G · 960×540 |
| 구도 | 왼쪽: 반짝이는 좋은 원료 더미 앞에서 온도 다이얼을 살짝 내리는 손(얼굴 없는 작업자 NPC). 오른쪽: 그 뒤 커튼 그림자 속 큰 손이 다이얼과 강도 시험체를 실로 함께 움직임. 초파리가 돋보기로 실을 발견 |
| 대체 글 | 숨은 원인이 킬른 온도와 강도를 함께 움직이는 모습을 초파리 연구원이 돋보기로 찾아내는 컷 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, 16:9 illustration panel, inside a cement plant control room, a faceless small worker turning a temperature dial slightly down next to a pile of glowing high-quality raw material, behind a curtain a large shadowy hand holds thin strings attached to both the dial and a grey concrete test cube, anthropomorphic fruit fly researcher with big red compound eyes, blue helmet with a gold stripe, white lab coat over a black vest, black gloves, looking through a magnifying glass at the strings, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `cut_cs_lv5` — 지도 밖의 별
| 항목 | 내용 |
|---|---|
| 판 · 크기 | G · 960×540 |
| 구도 | 바닥에 청록 점이 띠 모양으로 깔린 큰 지도. 한 개의 빨간 별이 띠 밖 어둠 속에서 반짝, 주판봇이 그쪽으로 손을 뻗고 조수가 지도 가장자리 점선을 가리킴 |
| 대체 글 | 학습 데이터 띠 밖에서 빛나는 최적점 별에 주판봇이 손을 뻗고 조수가 경계선을 가리키는 컷 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, 16:9 illustration panel, a huge floor map covered with a diagonal band of small teal dots and a dashed boundary line, one red star glowing outside the band in the dark, JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, reaching toward the red star, girl researcher with long pink hair in two round buns and a navy streak, white lab coat over lavender hoodie, jeans, pointing at the dashed boundary, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins
```

### 3-4. `sc_cs_outro` — 결과 후 (F 승)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 구도 | 초파리가 앞에서 팔짱(자신만만), 주판봇은 옆에서 한숨 쉬지만 주판알 몇 개를 조수에게 건넴(인정하는 몸짓), 박사가 두 손에 보랏빛 불꽃, 조수가 웃으며 시험체를 든다. 뒤로 킬른 불빛 |
| 피할 것 | 조롱, 글자 |
| 대체 글 | 대결 뒤 초파리 연구원이 팔짱을 끼고, 주판봇이 주판알을 건네며 결과를 인정하는 아웃트로 장면 |

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, cement plant control room at night with a glowing kiln through the window, anthropomorphic fruit fly researcher with big red compound eyes, blue helmet with a gold stripe and cables, white lab coat over a black vest, black gloves, in front with arms crossed and a confident look, JUPANBOT (AbaBot), the boxy beige retro CRT-monitor robot with a dark green screen face with mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, sighing but handing a few abacus beads to the girl researcher with a good-sport gesture, girl researcher with long pink hair in two round buns and a navy streak, white lab coat over lavender hoodie, jeans, smiling and holding a concrete test cube, chibi scientist with thin teal rectangular glasses, black hair with one white streak, white lab coat over black vest and tie, purple sparks in both hands at the back, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no white round robot head, no yellow or golden eyes, no floating robot, no gold coins
```

## 4. 일관성 지침
- 참고 이미지: 캐릭터 팩 기본 그림 4장 함께 첨부
- 같은 세션에서 연달아 생성, 표정만 바꿀 때: *same character, same size and position, only change the facial expression and pose to ...*
- 투명 배경이 안 되면 *solid flat #00ff00 background*

## 5. 매니페스트
```json
{
  "page": "cement_strength_cost",
  "anchor": "D:cement-plant",
  "season": "default",
  "duel": {"result": "F", "gap": 0.425},
  "images": [
    {"key":"cover_cs","plate":"L","size":[1920,1080],"status":"new","priority":"P1","slot":"cover","fallback":"css-pixel-four","alt":"밤의 시멘트 공장 관제실에서 네 캐릭터가 강도 시험체와 나무 주판이 올라간 저울을 사이에 두고 마주한 표지"},
    {"key":"sc_cs_hero","plate":"E","size":[1200,800],"status":"new","priority":"P1","slot":"hero-stage","fallback":"cover_cs"},
    {"key":"cut_cs_lv4","plate":"G","size":[960,540],"status":"new","priority":"P2","slot":"lv4"},
    {"key":"cut_cs_lv5","plate":"G","size":[960,540],"status":"new","priority":"P2","slot":"lv5"},
    {"key":"sc_cs_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"pixel-row"},
    {"key":"thumb_cs","plate":"I","size":[600,400],"status":"new","priority":"P3","slot":"index-card","fallback":"cover_cs-crop"},
    {"key":"og_cs","plate":"K","size":[1200,630],"status":"new","priority":"P3","slot":"og"}
  ]
}
```
