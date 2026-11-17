# AI를 활용한 시멘트 공정 최적화

시멘트 공장의 데이터로 품질을 미리 맞히고, 그 답을 믿어도 되는지 따지고, 단가를 붙여 가장 알맞은 운전을 찾는 강의의 주차별 인터랙티브 해설 페이지입니다. 박사·조수(하루)·초파리 연구원·주판봇이 진행합니다.

**▶ 바로 보기:** https://adminmrobo.github.io/AI_for_cement_produce/

글 · 안상선 ((주)M-Robo 대표) · Ahn Sangsun

## 첫 화면 — 주차별 공장 부지

첫 화면(`index.html`)은 흰 배경 위에 **15개 공장 부지**를 3 × 5(또는 4 × 4) 격자로 놓은 3D 지도입니다. 한 주에 공장 하나이고, 건물 모양은 [시멘트 공장 World](https://adminmrobo.github.io/smart_factory_world/cement/)의 3D 공장에서 가져왔습니다. 부지를 누르면 그 주차의 주제와 해설 페이지 링크가 뜹니다. 4 × 4 배치에서는 16번째 부지가 공장 정문(공장 World 전체 보기)입니다.

| 주차 | 공장 | 주차 | 공장 | 주차 | 공장 |
|---|---|---|---|---|---|
| 1 | 사일로·출하 | 6 | 원료·배합장(주판봇) | 11 | 관제실(위험) |
| 2 | 관제실 | 7 | 평가동(중간) | 12 | 굴뚝·대체연료 |
| 3 | 원료·배합장 | 8 | 가마(소성) | 13 | AI 에이전트 차고 |
| 4 | 품질 시험실 | 9 | 냉각기·소프트센서 | 14 | 관제실(보고) |
| 5 | 시멘트 분쇄기 | 10 | 예열탑·버너 | 15 | 평가동(기말) |

새 장을 올리면 `index.html` 아래쪽 스크립트의 `PLOTS` 목록에서 그 주차의 `st`를 `'open'`으로 바꾸고 `url`·`go`를 넣습니다.

## 강의 계획

| 주차 | 강의 주제 | 부제 | 주요 내용 | 해설 페이지 |
|---|---|---|---|---|
| 1주 | 제조 데이터 분석 개론 — 비용과 품질의 상충 구조 | 이 과목의 질문 | 상충 관계의 정식화 · 세 모듈 개관 · 데이터셋 소개 · 분석 환경 첫 실행 | [3D 공장](https://adminmrobo.github.io/smart_factory_world/cement/) |
| 2주 | 분석 환경 구축과 생성형 AI 활용 기초 | 도구 준비와 에러 대처 | 클라우드 실행 환경의 구조 · 오류 유형별 대처 절차 · 생성형 AI를 이용한 디버깅 | 준비 중 |
| 3주 | 지도학습 회귀 모델의 이해와 적용 | 첫 예측 모델 | 입력·출력 변수 정의 · 부스팅 트리 회귀 · 성능 지표(RMSE, R²) 해석 | 준비 중 |
| 4주 | 데이터 분할·과적합과 모델 검증 방법론 | 이걸 믿어도 되나 | 학습·검증·시험 분할 · 과적합 · 데이터 누수 · 그룹 단위 분할과 성능 재평가 · 실습: 예시 데이터(생선 시장)로 머신러닝 기초 분류 모델 — 2종·3종·전체 | [실습자료](https://adminmrobo.github.io/AI_for_cement_produce/#practice) |
| 5주 | 설명가능 AI를 활용한 변수 중요도 분석 | 무엇이 강도를 정하나 | SHAP 기여도 분해 · 파생 변수 생성 · 중요도와 인과의 구분 · 확인 카드 A · 실습: 4주에 이어 예시 데이터 분류 모델 | [ch05](https://adminmrobo.github.io/AI_for_cement_produce/ch05_explainable_ai_importance/) |
| 6주 | 비용함수 설계와 제약조건 하 최적화 | 값을 붙이면 답이 달라진다 | 목적함수 정의 · 단가 반영 원가 산출 · 목표 성능 제약 하 최소 원가 탐색 | [ch06](https://adminmrobo.github.io/AI_for_cement_produce/ch06_cost_function_optimization/) |
| 7주 | **중간 평가 — 실습 결과 분석 보고서** | — | 과제 안내 및 배점 설명 · Take home 제출 | — |
| 8주 | 공정 시계열 데이터의 시차 구조와 전처리 | 결과가 늦게 나오는 문제 | 표본 주기 불일치 · 공정 지연(약 37분) · 시차 탐색 · 비정상 운전 구간 식별 | [ch08](https://adminmrobo.github.io/AI_for_cement_produce/ch08_timeseries_lag_preprocessing/) |
| 9주 | 소프트센서 구현과 시계열 검증 설계 | 품질 예측 모델 만들기 | 시차 변수 생성 · 정지 구간 제외 · 시간 순서 분할 대 무작위 분할 비교 | [ch09](https://adminmrobo.github.io/AI_for_cement_produce/ch09_soft_sensor_validation/) |
| 10주 | 공정 변수 요인 분석과 경제성 평가 | 연료를 얼마나 줄일 수 있나 | 요인 기여도 순위 · 연료 절감 시나리오 예측 · 비용 환산 · 산업 평균 대조 · 확인 카드 C | 준비 중 |
| 11주 | 위험 기반 의사결정과 최적 운전점 도출 | 경계선 찾기 | 불량 발생 확률 추정 · 기대손실 산출 · 절감액-손실 균형점 · 허용 위험별 권고안 | 준비 중 |
| 12주 | 대체연료 적용의 다목적 상충 분석 | 폐자원 연료 | 대체율 구간별 생산량·품질 비교 · 공개 배출 데이터 수집 및 시각화 · 확인 카드 B | 준비 중 |
| 13주 | AI 모델 계열별 특성과 산업 적용 타당성 평가 | 기술 총괄 | 합성곱 신경망 · 이상 탐지 · 시계열 딥러닝 · 강화학습 · 상용 자동운전 패키지 · 도입 판단 체크리스트 | 준비 중 |
| 14주 | 대규모 언어모델을 활용한 분석 보고 자동화 | 생성형 AI 활용과 마무리 | 프롬프트 구성 · 보고서 초안 생성 · 사실 검증 절차 · 기말 과제 구성 점검 | 준비 중 |
| 15주 | **기말 평가 — 실습 결과 분석 보고서** | — | 과제 안내 및 배점 설명 · Take home 제출 | — |

## 4·5주 실습자료 — 예시 데이터로 배우는 머신러닝 기초 모델

예시 데이터(생선 시장)로 생선의 무게·길이·높이·두께를 보고 종류를 맞히는 분류 모델을 만듭니다. 4주와 5주에 걸쳐 ① → ② → ③ 순서로 진행합니다.

| 순서 | 실습 | 무엇을 맞히나 | Colab |
|---|---|---|---|
| ① | 분류 모델 — 2종류 | 두 종류 중 어느 쪽인지 (이진 분류) | [열기](https://colab.research.google.com/drive/1ZbHg_-juEGpRCSn1_u2SgljcfdwS11UI?usp=sharing) |
| ② | 분류 모델 — 3종류 | 세 종류 중 어느 것인지 (다중 분류) | [열기](https://colab.research.google.com/drive/1bwRHW-kncC3VBbYRpwGpthNgjCn3QHEg?usp=sharing) |
| ③ | 분류 모델 — 전체 | 데이터에 있는 모든 생선 종류 | [열기](https://colab.research.google.com/drive/1ceeu8Oe4-OVSWGjlo2m6-4-xfif0dHYE?usp=sharing) |

- 실습 데이터: `fish_market_full.csv` (수업 제공) — Colab에서 데이터를 올리라는 칸이 나오면 이 파일을 선택합니다.
- Colab 링크를 열고 [파일] → [드라이브에 사본 저장]으로 내 사본을 만든 뒤 실행합니다.

## 폴더 구성

| 폴더 | 내용 | 옛 저장소 |
|---|---|---|
| `ch05_explainable_ai_importance/` | ch05 「시멘트 품질, AI로 미리 본다」 — 해설 페이지, 실습 데이터(`data/`), 그림(`img/`), 그림 명세(`docs/`) | `ai_for_cement_produce_07` |
| `ch06_cost_function_optimization/` | ch06 「무엇이 강도를 정하고, 얼마에 만들 것인가」 — 해설 페이지, 그림(`img/`), 그림 명세(`docs/`) | `ai_for_cement_produce_08` |
| `ch08_timeseries_lag_preprocessing/` | ch08 「온도를 바꿨는데, 품질은 왜 나중에 달라질까?」 — 비전공자판 해설, 실습 데이터(`data/`), 실습 가이드 수정본·그림 명세(`docs/`), **8·9주 통합 실습 노트북**(`cement_time_lag_softsensor_lab.ipynb`·`.py`, 데이터 `data/cement_sensor_1min.csv`·`cement_quality_15min.csv`) | — |
| `ch09_soft_sensor_validation/` | ch09 「시험 결과를 기다리지 않고 품질을 알 수 있을까?」 — 비전공자판 해설, 그림 명세(`docs/`) | — |

수업 전체의 공장 지도는 별도 저장소 [smart_factory_world](https://github.com/adminmrobo/smart_factory_world)의 [시멘트 공장 World](https://adminmrobo.github.io/smart_factory_world/cement/)입니다 — 3D 공장에서 가마의 37분 지연, 정지·재가동, 소프트센서 예측(ch08·ch09)을 재생합니다.

각 장 폴더 안의 `README.md`에 그 장의 목차와 구성이 있습니다. 새 장은 `chNN_영문이름/` 폴더로 추가하고, 맨 위 `index.html`의 강의 계획 표에서 해당 주차의 "준비 중"을 링크로 바꿉니다.

## 게시

Settings → Pages → Branch `main` / `/(root)`로 두면 https://adminmrobo.github.io/AI_for_cement_produce/ 에서 열립니다.

## 저작권

캐릭터 이름·설정·그림 © 안상선. 허락 없이 사용할 수 없습니다. 캐릭터 원본: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions). 시멘트 기초 설명은 삼표그룹 블로그 「건축재료학개론 – 시멘트편」(2022)이 다루는 주제를 따라 일반 교과서 지식으로 풀어 썼습니다. 실습 데이터·단가는 교육용 가상값입니다.
