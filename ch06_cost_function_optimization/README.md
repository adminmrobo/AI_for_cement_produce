> **AI를 활용한 시멘트 공정 최적화 · ch06 (6주) 비용함수 설계와 제약조건 하 최적화** — [강의 전체 목차](https://adminmrobo.github.io/AI_for_cement_produce/)  
> **▶ 바로 보기:** https://adminmrobo.github.io/AI_for_cement_produce/ch06_cost_function_optimization/

# 시멘트 공정 AI 해설

**AI를 활용한 시멘트 공정 최적화** 강의의 개념을 브라우저에서 직접 계산하며 익히는 인터랙티브 해설 페이지입니다.
박사 · 조수(하루) · 초파리 연구원 · 주판봇이 진행합니다.

글 · 안상선 ((주)M-Robo 대표) · Ahn Sangsun

## v1.1 쉬운 풀어쓰기판 (2026-11-09)

시멘트도 AI 모델도 처음 보는 수강생을 위해 본문을 풀어 썼습니다.

- **0 들어가기 전에** — 시멘트 말 다섯 개와 AI 말 다섯 개를 다시 잡는 준비 칸
- **여기서 잠깐!** — 시멘트 이야기(배합 네 재료·클링커 4형제·분쇄기·산화물 분석·가마 온도·슬래그 수급과 혼합 시멘트 등)와 AI 이야기
- **조수(하루)의 수식 이야기** — 섀플리 값(떡볶이 가게)·포화·상호작용·LSF·보그 계산·교란변수·원가 식·안전 마진 1.65×RMSE·차분 진화를 숫자 예시와 이야기로 풀이
- 각 칸 앞뒤의 캐릭터 대화, "스스로 확인" 문제, 용어 한 장 정리
- 본문 삽화 5장 자리(`img/F11~F15`) — 그림 지시문은 `docs/IMG_easy_cement_strength_cost.md`

## 페이지

| 페이지 | 내용 |
|---|---|
| [무엇이 강도를 정하고, 얼마에 만들 것인가](cement_strength_cost.html) | 1부 AI에게 '왜'를 묻기(설명가능 AI · SHAP) · 2부 목표 강도를 지키며 가장 싼 배합 찾기(제약 원가 최적화) |

`index.html`이 이 장의 목록 페이지입니다.

### 사다리 5칸

1. **몫 나누기** — 배치 하나의 예측 강도를 변수별 몫(MPa)으로 나누는 워터폴. 정확한 SHAP을 페이지 안에서 계산한다(부분집합 64개 × 배경 160배치).
2. **전체 보기** — 비스웜·의존도 플롯으로 순위, 분말도 포화(약 3,800 cm²/g), C3S×슬래그 상호작용을 본다.
3. **새 변수** — 산화물 분석값을 LSF·SM·AM·보그 광물로 바꾸는 계산기와 관리 범위 게이지.
4. **중요 ≠ 원인** — 원료 품질(교란변수)이 만든 거꾸로 된 상관 실험, 확인 카드 A로 바꿔도 되는 변수 고르기.
5. **원가 최적화** — 원/톤 목적함수, 목표 강도 + 안전 마진(1.65 × RMSE) 제약, 격자 탐색, 파레토 경계, 슬래그 단가 분기점(55,500원), 외삽 체험.

**대결:** 예측을 목표(42.5 MPa)에 딱 맞춘 배합 vs 마진 2.9 MPa를 둔 배합 — 1,000배치를 모의 생산해 미달 배치 수를 비교한다.

## 페이지 안의 다른 기능

- 용어 밑줄 말풍선(핵심 → 전체 → 끄기), 확인 퀴즈 11문항, 읽은 곳 표시
- **지식 색인** — 개념·방법·주장·질문 검색과 관계 미니 그래프
- **온톨로지·서지 꾸러미** — `kg.json`, `kg.jsonld`, `kg.ttl`, `nodes.csv`, `edges.csv`, `references.csl.json`, `references.bib`, `references.ris`, `provenance.csv` 등을 ZIP 하나로 내려받기

## 파일 구성

```
ch06_cost_function_optimization/
├── index.html                      이 장 목록 페이지
├── cement_strength_cost.html       해설 페이지 (단일 파일, 외부 라이브러리 없음)
├── README.md
├── img/                            본문 삽화(F11~F15)와 시멘트 이야기 그림(Y02~Y08)
└── docs/
    ├── IMG_cement_strength_cost.md        이미지 제작 명세서
    ├── COVER_cement_strength_cost.md      글 표지 지시문
    ├── IMG_easy_cement_strength_cost.md   쉬운 풀어쓰기판 삽화 지시문
    └── IMG_zam_cement_strength_cost.md    시멘트 이야기 상자 그림 지시문
```

## 게시

이 장은 통합 저장소 [AI_for_cement_produce](https://github.com/adminmrobo/AI_for_cement_produce)의 `ch06_cost_function_optimization/` 폴더로 게시됩니다. 주소: https://adminmrobo.github.io/AI_for_cement_produce/ch06_cost_function_optimization/ (옛 저장소 `ai_for_cement_produce_08`에서 옮김, 2026-11-10)

페이지는 서버 없이 파일을 더블클릭해도 열립니다. 외부 요청은 글꼴(Google Fonts) 하나뿐이고, 브라우저 저장소를 쓰지 않습니다.

## 표지 그림 넣기

`docs/COVER_cement_strength_cost.md`의 지시문으로 표지(16:9)를 만든 뒤, 해설 페이지의 `<!-- lab-cover -->` … `<!-- /lab-cover -->` 사이 `data-img="cover_cs"` 자리에 넣습니다. 그림이 없어도 캐릭터 그림과 대체 표지로 페이지는 완성 상태입니다.

## 읽기 전에

- 실습 데이터·단가·결과는 모두 **교육용 가상값**입니다. "강의 실습 결과"라고 적힌 숫자는 강의 노트북 결과를 그대로 옮긴 것입니다.
- 페이지 안 그래프의 강도 식은 같은 성질(포화·상호작용·교란)을 갖도록 만든 **설명용 모형**이라 숫자가 강의 결과와 조금 다릅니다(예: 최적 원가 55,035원/t, 강의 54,793원/t).
- KS L 5201 1종 28일 42.5 MPa는 강의 자료 기준값이며, 적용 전 최신 규격을 확인하세요.
- 교육용 해설이며 실제 공정 운전 지침이 아닙니다.

## 참고문헌

- 안상선 (2026). 「AI를 활용한 시멘트 공정 최적화」 강의 교안.
- Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS 30*. https://arxiv.org/abs/1705.07874
- Shapley, L. S. (1953). A Value for n-Person Games. *Contributions to the Theory of Games II*.
- Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *KDD '16*. https://doi.org/10.1145/2939672.2939785
- Storn, R., & Price, K. (1997). Differential Evolution. *Journal of Global Optimization*, 11. https://doi.org/10.1023/A:1008202821328
- Bogue, R. H. (1929). Calculation of the Compounds in Portland Cement. (게재 정보 확인 필요)

## 인용

> 안상선 (2026). 무엇이 강도를 정하고, 얼마에 만들 것인가. AI를 활용한 시멘트 공정 최적화 해설, v1.0.

## 저작권

- 캐릭터(박사, 조수 하루, 초파리 연구원, 주판봇)의 이름·설정·그림 © 안상선. 허락 없이 사용할 수 없습니다. 그림 출처: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) @ ea5da3f
- 페이지 본문과 코드의 라이선스: _(저자가 정해 채울 것)_
- 제작 도구: [ai-lab-explainer](https://github.com/adminmrobo/ahnboat_lab_explainer)
