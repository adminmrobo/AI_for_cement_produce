> **AI를 활용한 시멘트 공정 최적화 · ch08 (8주) 공정 시계열 데이터의 시차 구조와 전처리** — [강의 전체 목차](https://adminmrobo.github.io/AI_for_cement_produce/)
> **▶ 바로 보기:** https://adminmrobo.github.io/AI_for_cement_produce/ch08_timeseries_lag_preprocessing/

# 온도를 바꿨는데, 품질은 왜 나중에 달라질까?

시멘트도 AI도 처음인 학생을 위한 비전공자판 인터랙티브 해설입니다. 박사 · 조수(하루) · 초파리 연구원 · 주판봇이 진행합니다.

글 · 안상선 ((주)M-Robo 대표) · Ahn Sangsun

## 사다리 3칸

1. **시계 맞추기** — 1분 온도 · 5분 전력 · 15분 품질을 행 번호가 아니라 시각으로 붙인다. 빈칸을 0으로 채우면 평균 69.28점이 4.31점이 된다.
2. **숨은 37분** — 온도를 0~60분 옮기며 품질과의 상관을 잰다. 정상 운전 줄에서 0분 0.133 → 37분 0.985(최고), 31~42분 모두 0.95 이상 → "약 30~45분"으로 읽는다.
3. **운전 상태** — 정지 2번(130분)·재가동(105분)과, 재가동 뒤 37분까지 남는 "지연의 그림자" 품질 5줄. 확인 카드 B.

**대결:** 같은 시각 온도 vs 37분 전 온도 — 일차함수 하나로 뒤 20% 기간 MAE 3.33점 vs 0.27점.

## 원자료와 다르게 쓴 곳 (저자 확인 필요)

- 실습 가이드 셀 6은 품질 줄만 고른 표에서 `shift(37)`을 해 1줄 = 15분, 곧 555분 전 온도와 짝을 짓는다(37분 상관 0.048). 이 페이지와 `docs/practice-guide_v1.1_fixed.md`는 1분 표에서 옮긴 뒤 품질 줄을 고른다(0.998, 정상 운전만 0.985).
- 확인 카드 B·C: 슬라이드는 B(시간·운전 상태) → C(검증), 강의 계획표는 10주 C · 12주 B. 이 페이지는 슬라이드를 따랐다.

## 파일 구성

```
ch08_timeseries_lag_preprocessing/
├── index.html                       이 장 목록 페이지
├── process_lag.html                 해설 페이지 (단일 파일, 실습 데이터 내장)
├── practice_guide.html              실습 가이드 페이지 (셀 복사 버튼 · 내려받기 · Colab 열기)
├── practice_guide.ipynb             실습 노트북 (Colab에서 바로 열림, 데이터는 주소로 읽음)
├── data/cement-practice-data.csv    실습 데이터 (가상, 4,320줄)
├── img/                             표지와 본문 그림 자리 (그림 받으면 넣기)
└── docs/
    ├── IMG_process_lag.md            Genspark 그림 지시문 (표지 + 7장)
    ├── practice-guide_v1.1_fixed.md  실습 가이드 수정본 (셀 6·13)
    └── practice-guide_v1.0_original.md
```
