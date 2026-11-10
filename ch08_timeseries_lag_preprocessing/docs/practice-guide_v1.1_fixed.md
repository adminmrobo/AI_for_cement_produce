# 실습 가이드 v1.1 — 시멘트 공정 시계열 데이터로 시차 찾기 · 소프트센서 만들기

> 이 가이드는 강의 슬라이드의 실습 슬라이드(21~23번, 45~47번)를 따라가는 용도입니다.
> Google Colab에서 셀 단위로 복사·실행하면 됩니다. 코드는 **함수(def)도, 반복문(for)도 없이** 한 줄 한 줄이 순서대로 진행됩니다.
> 모든 데이터는 **교육용 가상 데이터**입니다. 실제 공장 수치가 아니며, 결과 값도 실행 환경마다 조금씩 다를 수 있습니다.

---

## 1. 준비물

| 항목 | 설명 |
|---|---|
| `cement-practice-data.csv` | 이 폴더에 있는 실습 데이터 파일. 이름이 달라도 괜찮습니다 — 아래 코드는 업로드한 파일 이름을 자동으로 찾습니다 |
| Google Colab | colab.research.google.com 접속 후 새 노트북 생성 |

### 데이터에 무엇이 들어 있나 (변수 사전)

| 변수 | 뜻 | 단위 | 기록 주기 |
|---|---|---|---|
| `time` | 측정 시각 | — | 1분 |
| `kiln_temp` | 킬른(가마) 온도 | °C | 1분 |
| `o2_pct` | 가스 중 산소량 | % | 1분 |
| `mill_kwh` | 분쇄 전력 | kWh/t | 5분 (그 외 비어 있음) |
| `operation_state` | 운전 상태 | RUN / STOP / STARTUP | 1분 |
| `quality_index` | 교육용 조기 품질지표 | 점 | 15분 (그 외 비어 있음) |

**중요한 두 가지 구분**

- `quality_index`가 비어 있는 행은 **측정하지 않은 것**이지 품질이 나쁜 것이 아닙니다.
- 이 데이터의 숨은 설정: 안정 운전(RUN)에서 온도의 변화가 품질 신호에 반영되기까지 **약 37분**의 지연이 있습니다. 실제 공장이 아니라 시뮬레이션 가정입니다 — 실습에서 이 값을 *데이터로 찾아보는 것*이 목표입니다.

---

## 2. 시작: 라이브러리 설치와 데이터 업로드

**셀 1 — 라이브러리**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
```

**셀 2 — CSV 업로드**

Colab 좌측의 📎(클립보드) 아이콘을 눌러 `cement-practice-data.csv`를 올립니다.
아래 코드는 **어떤 파일 이름으로 올려도** 자동으로 찾습니다.

```python
from google.colab import files

uploaded = files.upload()
# 업로드된 파일 목록에서 .csv 이름을 찾습니다
csv_name = [f for f in uploaded if f.lower().endswith(".csv")][0]
print("불러올 파일:", csv_name)

df = pd.read_csv(csv_name)
print(df.shape)
df.head()
```

> 💡 로컬(컴퓨터)에서 jupyter로 돌리는 경우라면 `files.upload()` 대신
> `df = pd.read_csv("내_파일명.csv")`로 바꾸면 됩니다.

---

## 3. 시간 열 정리 (슬라이드 22번과 연결)

**셀 3 — 문자열을 진짜 시각으로**

```python
df["time"] = pd.to_datetime(df["time"])
df = df.sort_values("time").reset_index(drop=True)
print(df[["time", "kiln_temp", "operation_state"]].head())
print("시작:", df["time"].min(), " 종료:", df["time"].max())
```

**셀 4 — 기록 간격 확인**

```python
gaps = df["time"].diff().dropna()
print(gaps.value_counts().head())   # 대부분 1분이어야 합니다
```

> ⚠️ 여기서 간격이 1분이 아니면, 뒤에 나올 `shift(37)`은 37분이 아닙니다.
> 먼저 이 셀을 확인하는 습관이 중요합니다.

**셀 5 — 온도 추이 보기**

```python
part = df.iloc[500:900]
plt.figure(figsize=(12, 3.5))
plt.plot(part["time"], part["kiln_temp"], color="#028090")
plt.title("Kiln temperature (first hours)")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 4. 시차 탐색: 37분을 찾아보자 (슬라이드 13~16번과 연결)

품질 관측은 15분 간격이라, 여러 후보 시차를 직접 비교해 봅니다.
반복문 없이 **후보별로 한 줄씩** 계산합니다.

**셀 6 — 후보 시차별 상관계수**

```python
q = df[df["quality_index"].notna()]          # 품질이 있는 줄의 "위치"만 기억 (표는 1분 간격 그대로)

# 1분 표(df)에서 먼저 옮긴 뒤 → 품질 줄 위치만 골라 상관 계산 (반복문 없이)
# (v1.0은 q에서 shift해서 1줄 = 15분이 되어 shift(37) = 555분이었음)
r0   = df["kiln_temp"].shift(0)[q.index].corr(q["quality_index"])
r15  = df["kiln_temp"].shift(15)[q.index].corr(q["quality_index"])
r20  = df["kiln_temp"].shift(20)[q.index].corr(q["quality_index"])
r30  = df["kiln_temp"].shift(30)[q.index].corr(q["quality_index"])
r37  = df["kiln_temp"].shift(37)[q.index].corr(q["quality_index"])
r45  = df["kiln_temp"].shift(45)[q.index].corr(q["quality_index"])
r50  = df["kiln_temp"].shift(50)[q.index].corr(q["quality_index"])
r60  = df["kiln_temp"].shift(60)[q.index].corr(q["quality_index"])

lag_table = pd.DataFrame({
    "lag_min": [0, 15, 20, 30, 37, 45, 50, 60],
    "correlation": [r0, r15, r20, r30, r37, r45, r50, r60],
}).round(3)
lag_table
```

> 📌 **읽을 포인트:** 어느 시차에서 상관계수가 가장 높은가?
> 15분 간격의 품질 관측만으로는 꼭 37분이라는 숫자가 딱 떨어지지 않을 수 있습니다.
> “약 30~45분 구간” 정도로 읽는 것이 정직한 해석입니다.
>
> ✅ 참고(v1.1 재실행): 0분 0.133 · 15분 0.619 · 20분 0.790 · 30분 0.972 · **37분 0.998** · 45분 0.973 · 50분 0.941 · 60분 0.865.
> 정지·재가동 영향을 뺀 정상 운전 줄만 쓰면 37분 0.985로 여전히 가장 높습니다(셀 10 참고).

**셀 7 — 시차 곡선 그리기**

```python
plt.figure(figsize=(9, 4))
plt.plot(lag_table["lag_min"], lag_table["correlation"], marker="o", color="#028090")
best = lag_table.loc[lag_table["correlation"].idxmax(), "lag_min"]
plt.axvline(best, linestyle="--", color="#D98E22", label=f"Best candidate: {int(best)} min")
plt.title("Lag search (educational simulation)")
plt.xlabel("Lag (minutes)")
plt.ylabel("Correlation with quality_index")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 5. 운전 상태 점검 (슬라이드 17~20번과 연결)

**셀 8 — 상태별 분포와 온도 변화**

```python
print(df["operation_state"].value_counts())

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(df["time"], df["kiln_temp"], color="#028090", linewidth=1)
stop_mask = df["operation_state"] == "STOP"
ax.fill_between(df["time"], 850, 950, where=stop_mask, color="#B9C4C4", alpha=0.7, label="STOP")
startup_mask = df["operation_state"] == "STARTUP"
ax.fill_between(df["time"], 850, 1500, where=startup_mask, color="#FBF1DF", alpha=0.9, label="STARTUP")
ax.set(title="Kiln temperature with operation states", xlabel="Time", ylabel="Temperature (C)")
ax.legend()
plt.tight_layout()
plt.show()
```

> 🔍 정지(STOP) 구간에서는 온도가 900°C 부근으로 떨어집니다.
> 이 값을 “품질 0점”처럼 다루면 안 됩니다 — **생산하지 않은 시간**입니다.

---

## 6. 시차 변수 만들기 (슬라이드 29~30번과 연결)

**셀 9 — 과거 값 열 생성**

```python
s = df.sort_values("time").reset_index(drop=True).copy()
s["temp_lag37"] = s["kiln_temp"].shift(37)
s["o2_lag37"] = s["o2_pct"].shift(37)
s["state_lag37"] = s["operation_state"].shift(37)
s["temp_mean10_lag37"] = s["kiln_temp"].shift(37).rolling(10).mean()
s.tail()
```

> ⚠️ `shift(37)`은 **1분 간격 전제**입니다. 셀 4에서 간격을 확인했기 때문에 여기에서 쓸 수 있습니다.

**셀 10 — 학습용 표 만들기 (RUN만, 현재와 37분 전 모두 RUN)**

```python
train_rows = s.dropna(subset=["quality_index"]).copy()
train_rows = train_rows[(train_rows["operation_state"] == "RUN") &
                        (train_rows["state_lag37"] == "RUN")]
features = ["temp_lag37", "o2_lag37", "temp_mean10_lag37"]
train_rows = train_rows.dropna(subset=features + ["quality_index"])
X = train_rows[features]
y = train_rows["quality_index"]
print("학습용 행 수:", len(X))
X.head()
```

> 💡 품질 시각이 RUN이어도, 37분 전 센서가 STOP이었다면 그 행은 제외합니다.
> 제외 건수가 궁금하면 `len(s.dropna(subset=['quality_index'])) - len(X)`로 확인할 수 있습니다.

---

## 7. 소프트센서 학습 + 두 가지 분할 비교 (슬라이드 33~47번과 연결)

**셀 11 — 공통 모델 설정**

```python
model_kw = dict(n_estimators=120, min_samples_leaf=4, random_state=42, n_jobs=-1)
```

**셀 12 — 실험 A: 무작위 분할 (비교용)**

```python
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
model_a = RandomForestRegressor(**model_kw)
model_a.fit(Xr_tr, yr_tr)
pred_a = model_a.predict(Xr_te)
mae_a = mean_absolute_error(yr_te, pred_a)
print("Random split MAE:", round(mae_a, 3))
```

**셀 13 — 실험 B: 시간 순서 분할 + 60분 gap (현장형)**

```python
cut = int(len(train_rows) * 0.8)
start_test_time = train_rows["time"].iloc[cut]   # 위치로 찾기 (v1.0의 .loc[cut]은 이름표로 찾아 3/2 03:30을 집었음)
train_end_time = start_test_time - pd.Timedelta(minutes=60)

train_mask = train_rows["time"] < train_end_time
test_mask = train_rows["time"] >= start_test_time

Xt_tr = train_rows.loc[train_mask, features]
yt_tr = train_rows.loc[train_mask, "quality_index"]
Xt_te = train_rows.loc[test_mask, features]
yt_te = train_rows.loc[test_mask, "quality_index"]

model_b = RandomForestRegressor(**model_kw)
model_b.fit(Xt_tr, yt_tr)
pred_b = model_b.predict(Xt_te)
mae_b = mean_absolute_error(yt_te, pred_b)
print("Chronological + gap MAE:", round(mae_b, 3))
print("Training ends before:", train_end_time)
print("Test starts at:", start_test_time)
```

**셀 14 — 결과 비교표**

```python
report = pd.DataFrame({
    "split_method": ["Random shuffle", "Chronological + 60min gap"],
    "test_mae": [round(mae_a, 3), round(mae_b, 3)],
    "test_count": [len(yr_te), len(yt_te)],
})
report
```

**셀 15 — 미래 기간의 실제 vs 예측 그래프**

```python
plt.figure(figsize=(12, 4))
plt.plot(train_rows.loc[test_mask, "time"], yt_te, color="#028090", linewidth=2, label="Actual")
plt.plot(train_rows.loc[test_mask, "time"], pred_b, color="#D98E22", linewidth=1.5, alpha=0.85, label="Predicted")
plt.title("Future-period soft sensor validation")
plt.xlabel("Time")
plt.ylabel("Quality index (points)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 8. 결과를 어떻게 말할 것인가

- 두 MAE 중 어느 쪽이 더 크든, **“시간순 검증이 현장에 더 가까운 평가”**라는 문장은 변하지 않습니다.
- 무작위 분할 점수가 더 나쁠 수도 있고, 비슷할 수도 있습니다. 핵심은 점수의 크기가 아니라 **평가 설계가 실제 운용을 흉내 내는지**입니다.
- 이 품질지표는 교육용 가상 지표입니다. 실제 시멘트 강도 합격 판정에 사용해서는 안 됩니다.
- 시험실의 확정값과 주기적인 실측 비교가 여전히 최종 기준입니다.

---

## 9. AI에게 노트북을 만들어 달라고 할 때 쓰는 프롬프트 예시

코드를 직접 쓰기보다 AI 보조 도구(Colab의 코드 생성, 챗봇 등)에 부탁하고 싶다면, 아래처럼 **한 번에 한 단계씩** 요청하세요.

### 프롬프트 ① — 데이터 불러오기

> pandas로 CSV 파일을 불러와 줘. 파일명은 내가 업로드한 .csv 파일 중 첫 번째를 자동 검색해서 사용해 줘. time 열은 문자열인데 날짜·시각 타입으로 변환하고, time 기준으로 오름차순 정렬해 줘. 그리고 time.diff()로 인접 행 간격 분포를 출력해서 기록 주기가 정말 1분인지 확인해 줘. 함수 정의나 for 반복문 없이, 순서대로 실행되는 평탄한 코드만 써 줘.

### 프롬프트 ② — 시차 탐색

> quality_index가 비어 있지 않은 행만 골라, kiln_temp를 각각 0, 15, 20, 30, 37, 45, 50, 60분만큼 shift한 뒤 quality_index와의 상관계수를 한 줄씩 계산해 줘. 결과를 lag_min과 correlation 두 열의 표로 만들고, 그 표를 선 그래프로 그려 줘. 축 이름은 영어로, 가장 높은 시차 위치에 세로 점선을 넣어 줘. for문을 쓰지 말고 각 후보를 개별 줄로 작성해 줘.

### 프롬프트 ③ — 상태 필터링

> operation_state가 RUN이고, 동시에 37분 전 상태(state_lag37)도 RUN인 행만 남기는 코드를 써 줘. temp_lag37, o2_lag37, temp_mean10_lag37(37분 전 값 기준 최근 10분 이동평균) 세 개의 입력 변수와 quality_index 목표 변수를 준비하고, 결측이 있는 행은 제거해 줘. 제거 전후 행 수를 출력해서 몇 행이 빠졌는지 보여 줘.

### 프롬프트 ④ — 모델 두 개 비교

> 같은 RandomForestRegressor 설정(n_estimators=120, min_samples_leaf=4, random_state=42)으로 두 모델을 만들어 줘. 첫 번째는 train_test_split(test_size=0.2, shuffle=True)로 나누고, 두 번째는 시간순으로 앞 80%를 학습, 뒤 20%를 시험으로 쓰고 학습 끝과 시험 시작 사이에 60분 gap을 비워 줘. 둘 다 test MAE를 계산하고, 방법·MAE·시험 행 수를 담은 비교표를 출력해 줘. 마지막에 시험 기간의 실제값과 두 번째 모델 예측값을 시간축 그래프로 함께 그려 줘. 범례는 Actual / Predicted로 영어 표기.

### 프롬프트 사용 팁

- **한 프롬프트 = 한 셀.** 결과가 이상하면 그 셀만 다시 요청하세요.
- “for문 없이”, “def 없이”를 매번 붙여 주세요 — 초보자가 읽어야 하는 코드이므로 조건입니다.
- AI가 만든 코드를 실행하기 전에 **출력(print) 부분을 먼저 읽어 보세요.** 어떤 값을 확인하려고 하는지 알면 오류가 나도 스스로 고칠 확률이 높아집니다.

---

---

## v1.1 고친 곳 (2026-11-10, 저자 확인 필요)

| 셀 | v1.0 | v1.1 | 결과 차이 |
|---|---|---|---|
| 6 | 품질 줄만 고른 표 `q`에서 `shift(L)` → 1줄 = 15분이라 `shift(37)` = 555분 | 1분 표 `df`에서 `shift(L)` 한 뒤 품질 줄 위치(`q.index`)만 골라 상관 | 37분 상관 0.048 → 0.998 |
| 13 | `train_rows.loc[cut, "time"]` — 이름표 210 = 3월 2일 03:30 | `train_rows["time"].iloc[cut]` — 210번째 줄 = 3월 4일 08:15 | 학습 6줄 · 시험 253줄 · MAE 2.348 → 학습 206줄 · 시험 53줄 · MAE 0.262 |

재실행 참고값(scikit-learn, 같은 설정): 무작위 분할 MAE 0.314(시험 53줄), 시간순 + 60분 gap MAE 0.262(시험 53줄), 학습용 행 263개(제외 6개).

*교육용 가상 데이터 · v1.1 — 강의 슬라이드와 함께 배포*
