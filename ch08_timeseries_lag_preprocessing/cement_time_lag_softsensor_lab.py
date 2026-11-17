# %% [markdown]
# # 온도를 바꿨는데, 품질은 왜 나중에 달라질까?
# ### AI를 활용한 시멘트 공정 최적화 — 따라 하는 실습
#
# **오늘 할 일 한 줄 요약**
# 킬른(가마) 온도를 바꾸면 품질은 **몇 분 뒤에** 반응합니다.
# 그 숨은 시간(약 37분)을 데이터에서 찾고, 그 시간을 맞춘 AI로 품질을 미리 추정해 봅니다.
#
# | 순서 | 하는 일 | 결과물 |
# |---|---|---|
# | PART 1 | 시계 맞추기 (정렬 · 기록 간격 · 빈칸 · 시간 결합) | 시간축 그래프 |
# | PART 2 | 숨은 지연 찾기 (시차별 상관 · 정지 구간) | 시차 곡선, 정지 구간 메모 |
# | PART 3 | 소프트센서 만들기 (37분 전 값으로 품질 예측) | 학습표 |
# | PART 4 | 미래처럼 시험하기 (무작위 분할 vs 시간순 분할) | MAE 비교표, 실제·예측 그래프 |
#
# **실행 방법**
# - 맨 위 셀부터 차례대로 ▶(실행) 버튼을 누르거나 `Shift + Enter`를 누릅니다.
# - 셀을 건너뛰면 뒤에서 오류가 납니다. 오류가 나면 **[런타임] → [모두 실행]** 을 누르세요.
# - 회색 글씨 `#` 뒤의 문장은 설명(주석)이라 실행되지 않습니다.
#
# **꼭 알아 둘 단어 5개**
# - **시계열**: 시간 순서대로 쌓인 측정값. 숫자 + 언제의 값인지가 한 쌍입니다.
# - **시차(Lag)**: 지금 값과 비교하는 '과거 시점'까지의 간격. "37분 전 온도"의 37분.
# - **상관계수**: 두 값이 함께 움직이는 정도(−1 ~ +1). +1에 가까울수록 같이 오르내립니다.
# - **소프트센서**: 직접 재기 느린 값(품질)을 다른 센서값으로 추정하는 AI.
# - **MAE**: 예측이 평균 몇 점 틀렸는지. **작을수록 좋습니다.**
#
# > ※ 모든 데이터와 '37분 지연'은 교육용 가상 사례입니다.
# > ※ 그래프 글자는 Colab에서 한글이 깨지지 않도록 영어로 적었습니다.

# %% [markdown]
# ---
# ## 0단계. 준비하기
# ### 셀 1 — 도구(라이브러리) 불러오기
# 요리 전에 칼·도마를 꺼내 두는 단계입니다. 아무것도 출력되지 않으면 정상입니다.

# %%
# pandas : 엑셀처럼 표를 다루는 도구 (pd 라는 짧은 이름으로 부름)
import pandas as pd
# numpy : 숫자 계산 도구 (np)
import numpy as np
# matplotlib : 그래프 그리는 도구 (plt)
import matplotlib.pyplot as plt
# 랜덤포레스트 : 여러 판단나무가 낸 답을 평균해 예측하는 AI 모델
from sklearn.ensemble import RandomForestRegressor
# train_test_split : 데이터를 '공부용'과 '시험용'으로 무작위로 나눠 주는 도구
from sklearn.model_selection import train_test_split
# mean_absolute_error : MAE(평균 몇 점 틀렸나)를 계산하는 도구
from sklearn.metrics import mean_absolute_error
# files : 내 컴퓨터의 파일을 Colab에 올리고 내려받는 도구
from google.colab import files

# 표를 출력할 때 열이 잘리지 않게, 소수점은 둘째 자리까지 보이게 설정
pd.set_option('display.max_columns', 20)
pd.set_option('display.precision', 2)
# 그래프 기본 크기와 글자 크기
plt.rcParams['figure.figsize'] = (12, 4)
plt.rcParams['font.size'] = 11
print('✅ 준비 완료')

# %% [markdown]
# ### 셀 2 — 데이터 파일 올리기
# 실행하면 **[파일 선택]** 버튼이 나옵니다. 아래 두 파일을 `Ctrl`(맥은 `Command`)을 누른 채 **함께** 골라 올리세요.
# - `cement_sensor_1min.csv` : 1분마다 기록되는 센서 데이터
# - `cement_quality_15min.csv` : 15분마다 들어오는 품질 검사 결과
#
# ⚠ 같은 파일을 두 번 올리면 이름이 `cement_sensor_1min (1).csv` 처럼 바뀝니다.
# 그러면 **[런타임] → [런타임 연결 해제 및 삭제]** 후 다시 시작하는 것이 가장 쉽습니다.

# %%
# 파일 선택 창 열기 → 올린 파일은 Colab의 현재 폴더에 같은 이름으로 저장됩니다.
uploaded = files.upload()
print('업로드된 파일:', list(uploaded.keys()))

# CSV 파일을 읽어 표(데이터프레임)로 만듭니다.
sensor = pd.read_csv('cement_sensor_1min.csv')
quality = pd.read_csv('cement_quality_15min.csv')
print('✅ 센서 데이터  :', sensor.shape[0], '행,', sensor.shape[1], '열')
print('✅ 품질 데이터  :', quality.shape[0], '행,', quality.shape[1], '열')

# %% [markdown]
# ### 셀 3 — 데이터 첫 모습 보기
# **센서 데이터 (1분마다)**
#
# | 열 이름 | 뜻 | 단위 |
# |---|---|---|
# | time | 측정 시각 | 1분 간격 |
# | kiln_temp | 킬른(가마) 온도 | °C |
# | o2_pct | 킬른 배기가스의 산소 농도 | % |
# | mill_power_kw | 분쇄기 전력 (5분마다만 기록) | kW |
# | operation_state | 운전 상태: RUN 안정 운전 / STOP 정지 / STARTUP 기동 / MAINTENANCE 정비 | - |
#
# **품질 데이터 (15분마다)**
#
# | 열 이름 | 뜻 |
# |---|---|
# | sample_time | 시료를 채취·측정한 시각 |
# | result_time | 시험 결과가 시스템에 등록된 시각 (채취보다 늦음) |
# | quality_index | 조기 품질지표(점수). 28일 압축강도와는 다른 값 |

# %%
# head(8) : 위에서 8줄만 보기 / display : 표를 보기 좋게 출력 (Colab 기본 기능)
display(sensor.head(8))
display(quality.head(8))

# 👀 확인할 것: time 열을 보면 시각이 뒤죽박죽입니다.
#    → '행 순서'만 믿고 분석하면 안 되는 이유! 다음 셀에서 줄을 세웁니다.

# %% [markdown]
# ---
# ## PART 1. 공정의 시계 맞추기
# ### 셀 4 — 시간 글자를 '진짜 시각'으로 바꾸고, 시간순으로 줄 세우기
# 지금 `time` 은 `'2026-11-02 10:00'` 이라는 **글자**일 뿐이라 "몇 분 차이인지" 계산할 수 없습니다.
# `pd.to_datetime` 으로 진짜 시각으로 바꾸고, `sort_values` 로 빠른 시각부터 줄을 세웁니다.

# %%
# 글자 → 날짜·시각
sensor['time'] = pd.to_datetime(sensor['time'])
quality['sample_time'] = pd.to_datetime(quality['sample_time'])
quality['result_time'] = pd.to_datetime(quality['result_time'])

# 시간순 정렬 + 줄 번호를 0, 1, 2 … 로 새로 매기기
sensor = sensor.sort_values('time').reset_index(drop=True)
quality = quality.sort_values('sample_time').reset_index(drop=True)

display(sensor.head())
print('센서 기간:', sensor['time'].min(), '~', sensor['time'].max())
print('품질 기간:', quality['sample_time'].min(), '~', quality['sample_time'].max())

# 👀 확인할 것: 이제 time 이 00:00, 00:01, 00:02 … 순서로 정리되었습니다.
# ⚠ 정렬을 빼먹으면 뒤에서 만드는 '37분 전 값'이 엉뚱한 시점의 값이 됩니다.

# %% [markdown]
# ### 셀 5 — 몇 분마다 기록했을까? (표본 주기)
# 센서는 1분, 분쇄 전력은 5분, 품질은 15분 — **서로 다른 속도의 시계**입니다.
# `diff()` 는 바로 앞 줄과의 시간 차이, `value_counts()` 는 같은 값이 몇 번 나오는지 셉니다.

# %%
print('▶ 센서 기록 간격 (간격 : 횟수)')
print(sensor['time'].diff().value_counts().head(3))
print()
print('▶ 품질 기록 간격 (간격 : 횟수)')
print(quality['sample_time'].diff().value_counts().head(3))
print()

# 분쇄 전력: 값이 있는 칸 / 빈칸 세기
n_power = sensor['mill_power_kw'].notna().sum()
n_power_blank = sensor['mill_power_kw'].isna().sum()
print('▶ 분쇄 전력 값이 있는 행:', n_power, '/ 빈 행:', n_power_blank)

# 센서가 빠짐없이 1분 간격인가? (True 여야 shift(37) = 정확히 37분 전)
one_min_ok = (sensor['time'].diff().dropna() == pd.Timedelta('1min')).all()
print('▶ 센서가 빠짐없이 1분 간격인가?', one_min_ok)

# 💡 해석
print()
print('💡 해석: 센서는 1분, 품질은 대부분 15분마다 기록됩니다.')
print('   분쇄 전력의 빈칸은 고장이나 0 kW가 아니라 "기록하지 않은 시각"일 뿐입니다.')
print('   품질 간격에 15분보다 긴 값이 섞여 있다면 → 정지 중이라 시료가 없던 시간입니다.')

# %% [markdown]
# ### 셀 6 — 빈칸(결측값)은 0점이 아니다
# 품질지표가 빈칸이라는 것은 "품질이 나빴다"가 아니라 **"측정하지 않았다"** 는 뜻입니다.
# 0점으로 채우면 AI는 **없던 문제**를 배우게 됩니다. → 그대로 비워 둡니다.

# %%
n_q_missing = quality['quality_index'].isna().sum()
print('▶ 품질지표가 빈 행:', n_q_missing, '개 (전체', len(quality), '개 중)')
display(quality[quality['quality_index'].isna()].head())

# 시료 채취 → 결과 등록까지 걸린 시간(분)
quality['report_delay_min'] = (quality['result_time'] - quality['sample_time']).dt.total_seconds() / 60
print('▶ 결과 등록까지 걸린 시간: 최소', quality['report_delay_min'].min(), '분, 평균', round(quality['report_delay_min'].mean(), 1), '분, 최대', quality['report_delay_min'].max(), '분')

print()
print('💡 해석: 결과는 채취 후 약 1시간 뒤에 등록됩니다.')
print('   그래서 센서와 품질을 붙일 때는 "결과 등록 시각"이 아니라 "시료 채취 시각(sample_time)"을 기준으로 합니다.')

# %% [markdown]
# ### 셀 7 — 시간 간격 맞추기 (리샘플링) 세 가지 방법
# | 방법 | 코드 | 언제 쓰나 |
# |---|---|---|
# | ① 평균 | `resample('5min').mean()` | 흔들리는 센서를 부드럽게 볼 때 |
# | ② 직전값 유지 | `ffill()` | 마지막으로 확인된 값을 다음 기록까지 그대로 쓸 때 |
# | ③ 그대로 | (아무것도 안 함) | 성급하게 빈칸을 채우지 않을 때 |
#
# **원칙**: 예측에 쓰는 값은 **그 시점에 이미 알고 있던 값**만 씁니다.

# %%
# 시각을 줄 이름(인덱스)으로 둔 복사본 → 시간 기준 계산이 쉬워집니다.
s = sensor.set_index('time')

# ① 1분 온도를 5분씩 묶어 평균
temp_5min_mean = s['kiln_temp'].resample('5min').mean()
# ② 분쇄 전력 빈칸을 바로 앞의 값으로 채우기
power_ffill = s['mill_power_kw'].ffill()
# ③ 원래 그대로
power_raw = s['mill_power_kw']

# ②와 ③을 나란히 비교 (처음 12분)
display(pd.DataFrame({'③ raw (as recorded)': power_raw, '② ffill (last value)': power_ffill}).head(12))

# 그래프: 2시간만 확대해서 1분 원자료와 5분 평균 비교
win = slice('2026-11-03 10:00', '2026-11-03 12:00')
plt.plot(s.loc[win, 'kiln_temp'], color='lightgray', label='1-min raw')
plt.plot(temp_5min_mean.loc[win], color='tab:red', marker='o', label='5-min mean')
plt.title('Resampling: 1-min Kiln Temperature vs 5-min Mean')
plt.xlabel('Time')
plt.ylabel('Kiln Temperature (°C)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 📈 그래프 읽는 법
#  - 회색 선(1분 원자료)은 들쭉날쭉, 빨간 점선(5분 평균)은 부드럽습니다.
#  - 평균을 내면 잡음은 줄지만, 갑자기 바뀐 순간은 조금 늦게 나타납니다.

# %% [markdown]
# ### 셀 8 — 📊 결과물 ① : 1분 센서와 15분 품질을 같은 시간축에 그리기
# 하루(11월 3일)만 잘라 위에는 온도, 아래에는 품질을 그립니다.
# **눈으로 먼저** 봅니다: 온도가 오르내린 뒤 품질이 **조금 늦게** 따라 움직이나요?

# %%
day = slice('2026-11-03 00:00', '2026-11-03 23:59')
q = quality.set_index('sample_time')

fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
ax[0].plot(s.loc[day, 'kiln_temp'], color='tab:red', label='Kiln temperature (every 1 min)')
ax[0].set_title('Sensor and Quality on the Same Time Axis (Nov 3)')
ax[0].set_ylabel('Kiln Temp (°C)')
ax[0].legend(loc='upper left')
ax[0].grid(alpha=0.3)
ax[1].plot(q.loc[day, 'quality_index'], color='tab:blue', marker='o', markersize=3, label='Quality index (every 15 min)')
ax[1].set_ylabel('Quality Index (score)')
ax[1].set_xlabel('Time')
ax[1].legend(loc='upper left')
ax[1].grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 📈 그래프 읽는 법
#  - 위(빨강): 1분마다 찍혀 촘촘한 선 / 아래(파랑): 15분마다 찍힌 점
#  - 온도의 큰 봉우리·골짜기를 하나 골라, 품질에서 비슷한 모양이 '오른쪽(나중)'에 나타나는지 찾아보세요.
#  - 정확히 몇 분 늦는지는 눈으로 알기 어렵습니다 → PART 2에서 숫자로 찾습니다.

# %% [markdown]
# ### 셀 9 — 줄 번호로 붙이면 안 되는 이유
# - ✕ **잘못된 결합**: 품질 1번째 줄 + 센서 1번째 줄 → 서로 **다른 시각**끼리 붙습니다.
# - ✓ **올바른 결합**: **시각을 기준으로** 같은(또는 바로 앞) 시각의 센서값을 찾아 붙입니다.

# %%
# ✕ 줄 번호끼리 옆으로 붙이기
wrong = pd.concat([quality[['sample_time', 'quality_index']].head(3), sensor[['time', 'kiln_temp']].head(3)], axis=1)
print('✕ 줄 번호로 붙인 결과 → sample_time 과 time 이 서로 다릅니다')
display(wrong)

# ✓ 시각 기준으로 붙이기
# merge_asof(..., direction='backward') : 품질 시각과 같거나 '그 앞'의 가장 가까운 센서 값을 찾아옵니다.
right = pd.merge_asof(quality[['sample_time', 'quality_index']], sensor[['time', 'kiln_temp']], left_on='sample_time', right_on='time', direction='backward')
print('✓ 시각 기준으로 붙인 결과 → 두 시각이 일치합니다')
display(right.head(3))

# 🤔 생각해 보기: 품질은 37분 늦게 반응한다면, 10:37 품질에는 몇 시 온도를 붙여야 할까?
#    (답: 10:00 온도. '37분 전'은 언제나 과거 방향입니다.)

# %% [markdown]
# ---
# ## PART 2. 숨은 37분을 데이터에서 찾는다
# ### 셀 10 — 운전 상태 확인과 📝 정지 구간 메모
# 설비가 멈춘 시간(STOP), 다시 켜는 시간(STARTUP), 정비 시간(MAINTENANCE)은 평소(RUN)와 다른 상황입니다.
# 먼저 **언제, 얼마나** 있었는지 표로 정리합니다.

# %%
print('▶ 상태별 기록 시간(분)')
print(sensor['operation_state'].value_counts())

# 상태가 바뀔 때마다 번호를 1씩 올려 '같은 상태가 이어진 덩어리'를 만듭니다.
#   (지금 상태 != 바로 앞 상태) → 바뀐 곳만 True(1) → 누적합(cumsum) = 덩어리 번호
sensor['block'] = (sensor['operation_state'] != sensor['operation_state'].shift()).cumsum()
# 덩어리마다 상태·시작·끝·길이(분)를 요약
events = sensor.groupby('block').agg(state=('operation_state', 'first'), start=('time', 'min'), end=('time', 'max'), minutes=('time', 'size'))
# RUN이 아닌 덩어리만 남기기
events = events[events['state'] != 'RUN'].reset_index(drop=True)
print()
print('▶ RUN이 아닌 구간 목록')
display(events)

# 📝 결과물: 정지 구간 메모 1줄
print(f'📝 메모: 비정상 운전 구간 {len(events)}개, 총 {events["minutes"].sum()}분. 삭제하지 않고 표시한 뒤, 모델 학습에서만 제외합니다.')

# %% [markdown]
# ### 셀 11 — 📊 결과물 ② : 전체 기간 온도와 정지·기동 구간 표시
# 운전 기록(operation_state)이 먼저이고, 온도 그래프는 그것을 **눈으로 확인하는 보조 자료**입니다.

# %%
is_stop = sensor['operation_state'] == 'STOP'
is_startup = sensor['operation_state'] == 'STARTUP'
is_maint = sensor['operation_state'] == 'MAINTENANCE'

plt.figure(figsize=(13, 4))
plt.plot(sensor['time'], sensor['kiln_temp'], color='tab:red', linewidth=0.6, label='Kiln temperature')
plt.scatter(sensor.loc[is_stop, 'time'], sensor.loc[is_stop, 'kiln_temp'], s=4, color='black', label='STOP')
plt.scatter(sensor.loc[is_startup, 'time'], sensor.loc[is_startup, 'kiln_temp'], s=4, color='orange', label='STARTUP')
plt.scatter(sensor.loc[is_maint, 'time'], sensor.loc[is_maint, 'kiln_temp'], s=4, color='purple', label='MAINTENANCE')
plt.title('Kiln Temperature with Operation States (14 days)')
plt.xlabel('Time')
plt.ylabel('Kiln Temperature (°C)')
plt.legend(loc='lower left', markerscale=4)
plt.grid(alpha=0.3)
plt.show()

# 📈 그래프 읽는 법
#  - 평소 온도는 1,430~1,470°C 근처에서 움직입니다.
#  - 검정(정지)·보라(정비) 구간에서는 온도가 뚝 떨어지고, 주황(기동) 구간에서 천천히 회복합니다.
#  - 이 큰 낙차는 '품질과 온도의 관계'가 아니라 '공장이 켜졌나 꺼졌나'의 차이입니다.

# %% [markdown]
# ### 셀 12 — '정상 운전 행' 표시하기 (지연의 그림자까지)
# 품질 시각에 RUN이었어도, **37분 전**에 STOP·STARTUP이었다면 그 영향이 품질에 남아 있습니다.
# 그래서 **품질 시각 기준 지난 60분이 모두 RUN** 인 행만 '정상 운전 행'(run_60 = 1)으로 표시합니다.

# %%
# is_run : 그 1분이 RUN이면 1, 아니면 0
sensor['is_run'] = (sensor['operation_state'] == 'RUN').astype(int)
# rolling(61).min() : 지금 포함 최근 61분 중 가장 작은 값 → 하나라도 0이면 0
sensor['run_60'] = sensor['is_run'].rolling(61).min()

# 품질 표에 '품질 시각'의 run_60 값을 붙입니다 (시각 기준 결합)
quality = pd.merge(quality, sensor[['time', 'run_60']], left_on='sample_time', right_on='time', how='left').drop(columns='time')

n_run = (quality['run_60'] == 1).sum()
print(f'▶ 정상 운전 품질 행: {n_run}개 / 정지·기동의 영향을 받은 행: {len(quality) - n_run}개')

# %% [markdown]
# ### 셀 13 — 시험 구간을 **먼저** 정해 두기
# AI 실력은 **미래 구간**으로 시험합니다. 그런데 시험 구간의 정답을 보고 시차를 고르면 **시험지를 미리 본 것**과 같습니다.
# 그래서 지금 미리 선을 그어 둡니다.
#
# `[ 학습 구간(앞쪽 약 80%) ] [ gap 60분 ] [ 시험 구간(뒤쪽 약 20%) ]`
#
# 시차 찾기(PART 2)는 **학습 구간에서만** 하고, 시험 구간은 PART 4에서 **딱 한 번만** 봅니다.

# %%
# quantile(0.8) : 시각을 줄 세웠을 때 80% 지점 / floor('15min') : 15분 단위로 내림
cut_time = quality['sample_time'].quantile(0.8).floor('15min')
gap = pd.Timedelta('60min')
train_end = cut_time - gap
print('▶ 학습 구간 :', quality['sample_time'].min(), '~', train_end, '이전')
print('▶ gap(비움) :', train_end, '~', cut_time)
print('▶ 시험 구간 :', cut_time, '부터 끝까지')

# %% [markdown]
# ### 셀 14 — 시차 후보 4개를 눈으로 비교하기 (0 / 20 / 37 / 50분)
# 온도를 **L분 뒤로 밀어서** 각 품질 시각 옆에 **L분 전 온도**를 놓고, 점(산점도)으로 찍어 봅니다.
# - `shift(L)` : 값을 L줄 뒤로 밀기. 1분에 1줄이므로 **L줄 = L분 전**
# - `reindex(품질 시각들)` : 품질이 측정된 시각의 값만 골라오기
#
# 점들이 **오른쪽 위로 가늘게 모일수록** 관계가 강합니다(상관계수 r이 1에 가까움).

# %%
# 1분 온도·산소를 '시각'을 줄 이름으로 둔 시리즈로 준비
temp = sensor.set_index('time')['kiln_temp']
o2 = sensor.set_index('time')['o2_pct']

# 학습 구간 + 정상 운전 + 품질값이 있는 행만 (= 시차 찾기용 데이터)
qa = quality[(quality['sample_time'] < train_end) & (quality['run_60'] == 1)].dropna(subset=['quality_index'])
qa_quality = qa['quality_index'].values
print('▶ 시차 찾기에 쓰는 품질 행:', len(qa))

# L분 전 온도를 품질 시각에 맞춰 가져오기
lag0 = temp.shift(0).reindex(qa['sample_time']).values
lag20 = temp.shift(20).reindex(qa['sample_time']).values
lag37 = temp.shift(37).reindex(qa['sample_time']).values
lag50 = temp.shift(50).reindex(qa['sample_time']).values

# 상관계수 계산 (np.corrcoef 결과의 [0, 1] 칸이 두 값의 상관계수)
r0 = np.corrcoef(lag0, qa_quality)[0, 1]
r20 = np.corrcoef(lag20, qa_quality)[0, 1]
r37 = np.corrcoef(lag37, qa_quality)[0, 1]
r50 = np.corrcoef(lag50, qa_quality)[0, 1]

fig, ax = plt.subplots(1, 4, figsize=(16, 4), sharey=True)
ax[0].scatter(lag0, qa_quality, s=6, alpha=0.5)
ax[0].set_title(f'Lag 0 min (r = {r0:.2f})')
ax[1].scatter(lag20, qa_quality, s=6, alpha=0.5)
ax[1].set_title(f'Lag 20 min (r = {r20:.2f})')
ax[2].scatter(lag37, qa_quality, s=6, alpha=0.5, color='tab:red')
ax[2].set_title(f'Lag 37 min (r = {r37:.2f})')
ax[3].scatter(lag50, qa_quality, s=6, alpha=0.5)
ax[3].set_title(f'Lag 50 min (r = {r50:.2f})')
ax[0].set_ylabel('Quality Index (score)')
ax[0].set_xlabel('Kiln Temp L min before (°C)')
ax[1].set_xlabel('Kiln Temp L min before (°C)')
ax[2].set_xlabel('Kiln Temp L min before (°C)')
ax[3].set_xlabel('Kiln Temp L min before (°C)')
plt.suptitle('Quality vs Kiln Temperature Shifted by Candidate Lags (training period, RUN only)')
plt.tight_layout()
plt.show()

# 💡 해석 — 4개 후보의 상관계수를 표로
display(pd.DataFrame({'시차(분)': [0, 20, 37, 50], '상관계수 r': [r0, r20, r37, r50]}).round(3))
print('💡 해석: 0분(같은 시각)보다 37분 전 온도와 품질이 더 함께 움직입니다.')
print('   50분처럼 너무 많이 밀면 다시 어긋납니다 → 품질에 영향을 준 시점을 지나쳐 버렸기 때문입니다.')

# %% [markdown]
# ### 셀 15 — 📊 결과물 ③ : 0~60분 시차를 모두 비교한 '시차 곡선'
# 셀 14를 0분, 1분, 2분 … 60분까지 **61번** 반복하면 됩니다.
# for문 대신 `apply(lambda L: …)` 를 씁니다. 읽는 법은 이렇습니다.
#
# > `lags.apply(lambda L: 계산식)` = "lags 안의 숫자를 하나씩 L에 넣어 계산식을 실행하고, 결과를 모아 줘"
#
# 먼저 **37분 하나만** 계산해 보고, 같은 식을 61개에 한 번에 적용합니다.

# %%
# 품질값을 '시각'이 줄 이름인 시리즈로 준비 (온도와 시각으로 짝을 맞추기 위해)
qa_series = pd.Series(qa_quality, index=qa['sample_time'])

# (연습) 37분 하나만: 온도를 37분 밀기 → 품질 시각만 골라오기 → 품질과 상관계수
one = temp.shift(37).reindex(qa['sample_time']).corr(qa_series)
print('▶ 연습 — 37분 시차의 상관계수:', round(one, 3), '(셀 14의 r37과 같아야 합니다)')

# (본 계산) 0~60분 전부: 위의 37 자리에 L을 넣어 61번 계산
lags = pd.Series(range(0, 61))
corr_run = lags.apply(lambda L: temp.shift(L).reindex(qa['sample_time']).corr(qa_series))

# (비교) 정지·기동이 섞인 학습 구간 전체 데이터로 같은 계산
qall = quality[quality['sample_time'] < train_end].dropna(subset=['quality_index'])
qall_series = pd.Series(qall['quality_index'].values, index=qall['sample_time'])
corr_all = lags.apply(lambda L: temp.shift(L).reindex(qall['sample_time']).corr(qall_series))

# 봉우리(가장 높은 곳) 찾기
best_lag = int(corr_run.idxmax())
# 봉우리가 넓으면 정확한 분 수는 불확실 → 최고값의 95% 이상인 범위도 함께 봅니다.
near_top = lags[corr_run >= corr_run.max() * 0.95]

plt.figure(figsize=(10, 4.5))
plt.plot(lags, corr_all, color='gray', linestyle='--', label='All data (RUN + STOP + STARTUP)')
plt.plot(lags, corr_run, color='tab:blue', linewidth=2, label='Stable RUN only')
plt.axvline(best_lag, color='tab:red', linestyle=':', label=f'Peak lag = {best_lag} min')
plt.axvspan(near_top.min(), near_top.max(), color='tab:red', alpha=0.1, label='Within 95% of peak')
plt.title('Lag Scan: Correlation between Quality and Shifted Kiln Temperature')
plt.xlabel('Lag (minutes)')
plt.ylabel('Correlation coefficient')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 💡 해석 (숫자는 실행 결과에서 자동으로 채워집니다)
print(f'💡 해석 1: 안정 운전 데이터에서 봉우리는 {best_lag}분입니다 (상관계수 {corr_run.max():.3f}).')
print(f'   봉우리 근처 {near_top.min()}~{near_top.max()}분은 거의 같은 높이 → "약 {near_top.min()}~{near_top.max()}분"처럼 범위로 읽는 것이 안전합니다.')
print(f'💡 해석 2: 정지·기동이 섞인 회색 선은 0분일 때도 {corr_all[0]:.2f}로 높고, 곡선이 평평합니다.')
print('   온도 급락 = 품질 급락이 시차와 상관없이 겹쳐서 생긴 착시입니다. AI가 "공장이 켜졌나"만 배울 수 있습니다.')
print('💡 주의: 상관이 가장 높다 ≠ 원인이 확정되었다. 제품이 이동하는 시간 등 공정 원리로 다시 확인합니다.')

# %% [markdown]
# ---
# ## PART 3. 소프트센서 — 시험 결과를 기다리지 않고 품질 추정하기
# ### 셀 16 — 입력 변수(재료) 만들기: '37분 전 값'
# | 변수 이름 | 뜻 | 만드는 법 |
# |---|---|---|
# | temp_lag37 | 37분 전 온도 한 점 | `shift(37)` |
# | temp_mean10_lag37 | 37~46분 전 온도 10개의 평균 | `rolling(10).mean()` 후 `shift(37)` |
# | o2_lag37 | 37분 전 산소 농도 | `shift(37)` |
# | temp_now, o2_now | (비교용) **같은 시각** 온도·산소 | 그대로 |
#
# 교안 가정대로 37분을 씁니다. 셀 15에서 찾은 범위(약 30~45분) 안에 들어 있습니다.

# %%
LAG = 37

sensor['temp_lag37'] = sensor['kiln_temp'].shift(LAG)
sensor['o2_lag37'] = sensor['o2_pct'].shift(LAG)
# 최근 10분 평균을 먼저 만들고 → 37줄 뒤로 밀기 = 37~46분 전 평균 (모두 과거값만 사용)
sensor['temp_mean10_lag37'] = sensor['kiln_temp'].rolling(10).mean().shift(LAG)
sensor['temp_now'] = sensor['kiln_temp']
sensor['o2_now'] = sensor['o2_pct']

# 36~41번째 줄을 보며 확인
display(sensor[['time', 'kiln_temp', 'temp_lag37', 'temp_mean10_lag37', 'o2_lag37']].iloc[36:42])

# 👀 확인할 것: 00:37 줄의 temp_lag37 = 00:00 줄의 kiln_temp 입니다. (37분 전 값이 옮겨 옴)
#    맨 앞 37줄은 '37분 전'이 없으므로 NaN(빈칸)이 정상입니다.

# %% [markdown]
# ### 셀 17 — 학습표 만들기: 품질 한 번 = 문제 한 개
# 품질이 측정된 시각마다 **입력(과거 센서값)** 과 **정답(실측 품질)** 을 한 줄로 묶습니다.
# 그리고 데이터 정책대로 **제외 건수를 보고**합니다.

# %%
feat_cols = ['temp_lag37', 'temp_mean10_lag37', 'o2_lag37', 'temp_now', 'o2_now']
table = pd.merge(quality, sensor[['time'] + feat_cols], left_on='sample_time', right_on='time', how='left').drop(columns='time')

n_total = len(table)
n_missing = table['quality_index'].isna().sum()
n_not_run = ((table['run_60'] != 1) & table['quality_index'].notna()).sum()

# 정상 운전 행만 남기고, 빈칸이 있는 행은 뺍니다 (0으로 채우지 않음)
table = table[table['run_60'] == 1].dropna(subset=['quality_index'] + feat_cols).reset_index(drop=True)

display(pd.DataFrame({'구분': ['전체 품질 행', '제외 ① 미측정(빈칸)', '제외 ② 정지·기동 영향', '✅ 모델에 쓰는 행'], '행 수': [n_total, n_missing, n_not_run, len(table)]}))
display(table[['sample_time', 'temp_lag37', 'temp_mean10_lag37', 'o2_lag37', 'quality_index']].head())

# %% [markdown]
# ### 셀 18 — 입력 X 와 정답 y 정하기
# - **X (입력)** : AI에게 주는 힌트 = 37분 전 센서값 3개
# - **y (정답)** : AI가 맞혀야 하는 값 = 실측 품질지표

# %%
X_cols = ['temp_lag37', 'temp_mean10_lag37', 'o2_lag37']
X = table[X_cols]
y = table['quality_index']
print('▶ X 크기:', X.shape, '(행 = 문제 수, 열 = 힌트 수)')
print('▶ y 크기:', y.shape)
print(f'▶ 품질지표 범위: {y.min():.1f} ~ {y.max():.1f}점, 평균 {y.mean():.1f}점')

# %% [markdown]
# ---
# ## PART 4. AI 실력은 미래처럼 시험해야 한다
# 같은 AI, 같은 입력으로 **데이터를 나누는 방법만** 바꿔 두 번 시험합니다.
#
# | 실험 | 나누는 법 | 특징 |
# |---|---|---|
# | A. 무작위 분할 | 줄을 섞어 80% 공부, 20% 시험 | 어제·내일이 섞임 → 점수가 좋아 보일 수 있음 |
# | B. 시간순 분할 + gap | 앞쪽 공부, 60분 띄우고 뒤쪽 시험 | 실제 현장 사용과 비슷 |
#
# AI 사용은 3단계: `model = 모델 만들기` → `model.fit(X, y)` 공부 → `model.predict(X)` 예측

# %% [markdown]
# ### 셀 19 — 실험 A : 무작위 분할 (비교용)

# %%
# test_size=0.2 : 20%를 시험용으로 / random_state=42 : 매번 같은 방식으로 섞기 (결과 재현용)
Xtr_r, Xte_r, ytr_r, yte_r = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤포레스트: 판단나무 300그루, 잎 하나에 최소 3개 사례 (너무 외우지 않도록)
model_r = RandomForestRegressor(n_estimators=300, min_samples_leaf=3, random_state=42)
model_r.fit(Xtr_r, ytr_r)
pred_r = model_r.predict(Xte_r)
mae_random = mean_absolute_error(yte_r, pred_r)

print(f'▶ 실험 A (무작위 분할) — 공부 {len(Xtr_r)}행, 시험 {len(Xte_r)}행')
print(f'▶ MAE = {mae_random:.3f}점  → 평균 {mae_random:.2f}점 정도 틀렸다는 뜻')

# %% [markdown]
# ### 셀 20 — 실험 B : 시간순 분할 + gap 60분 (현장형)
# 셀 13에서 미리 정해 둔 경계를 그대로 씁니다. **결과를 보고 경계를 바꾸지 않습니다.**

# %%
train_mask = table['sample_time'] < train_end
test_mask = table['sample_time'] >= cut_time
Xtr_t, ytr_t = X[train_mask], y[train_mask]
Xte_t, yte_t = X[test_mask], y[test_mask]

model_t = RandomForestRegressor(n_estimators=300, min_samples_leaf=3, random_state=42)
model_t.fit(Xtr_t, ytr_t)
pred_t = model_t.predict(Xte_t)
mae_time = mean_absolute_error(yte_t, pred_t)

print(f'▶ 실험 B (시간순 + gap) — 공부 {len(Xtr_t)}행, 시험 {len(Xte_t)}행, gap으로 빠진 행 {(~train_mask & ~test_mask).sum()}행')
print(f'▶ MAE = {mae_time:.3f}점  → 처음 보는 미래 기간에서 평균 {mae_time:.2f}점 정도 틀렸다는 뜻')

# %% [markdown]
# ### 셀 21 — 비교 실험: 시차를 무시하면? / 아무 정보도 안 쓰면?
# - **시차 무시**: 같은 시간순 분할, 같은 모델. 입력만 **같은 시각** 온도·산소로 바꿉니다.
# - **기준선**: 센서 없이 '학습 기간 평균 점수'로 모두 찍는 가장 단순한 예측. AI라면 이것보다는 나아야 합니다.

# %%
X_now = table[['temp_now', 'o2_now']]
model_now = RandomForestRegressor(n_estimators=300, min_samples_leaf=3, random_state=42)
model_now.fit(X_now[train_mask], ytr_t)
pred_now = model_now.predict(X_now[test_mask])
mae_now = mean_absolute_error(yte_t, pred_now)

pred_base = np.full(len(yte_t), ytr_t.mean())
mae_base = mean_absolute_error(yte_t, pred_base)

print(f'▶ 시차 무시(같은 시각 값) MAE = {mae_now:.3f}점')
print(f'▶ 기준선(평균 {ytr_t.mean():.1f}점으로 찍기) MAE = {mae_base:.3f}점')

# %% [markdown]
# ### 셀 22 — 📊 결과물 ④ : 분할 그림 2개
# 파란 점 = 공부(학습)에 쓴 시각, 주황 점 = 시험에 쓴 시각

# %%
fig, ax = plt.subplots(2, 1, figsize=(13, 4.5), sharex=True)
ax[0].scatter(table.loc[Xtr_r.index, 'sample_time'], np.zeros(len(Xtr_r)), s=4, color='tab:blue', label='Train')
ax[0].scatter(table.loc[Xte_r.index, 'sample_time'], np.zeros(len(Xte_r)), s=4, color='tab:orange', label='Test')
ax[0].set_title('Experiment A: Random Split (past and future are mixed)')
ax[0].set_yticks([])
ax[0].legend(loc='upper left', markerscale=3)
ax[1].scatter(table.loc[train_mask, 'sample_time'], np.zeros(train_mask.sum()), s=4, color='tab:blue', label='Train')
ax[1].scatter(table.loc[test_mask, 'sample_time'], np.zeros(test_mask.sum()), s=4, color='tab:orange', label='Test')
ax[1].axvspan(train_end, cut_time, color='gray', alpha=0.4, label='Gap (60 min)')
ax[1].set_title('Experiment B: Time-ordered Split + Gap (learn the past, test the future)')
ax[1].set_yticks([])
ax[1].set_xlabel('Sample time')
ax[1].legend(loc='upper left', markerscale=3)
plt.tight_layout()
plt.show()

# 📈 그래프 읽는 법
#  - 위(A): 주황 점이 기간 전체에 흩어져 있음 → 시험 문제 바로 15분 앞뒤의 비슷한 문제를 공부한 셈
#  - 아래(B): 주황 점이 맨 뒤에만 있음 → 공부한 적 없는 '미래'로 시험

# %% [markdown]
# ### 셀 23 — 📊 결과물 ⑤ : MAE 비교표

# %%
result = pd.DataFrame({
'실험': ['A. 무작위 분할 + 37분 전 입력', 'B. 시간순 분할 + 37분 전 입력', 'B. 시간순 분할 + 같은 시각 입력', '기준선: 평균값으로 찍기'],
'MAE(점)': [mae_random, mae_time, mae_now, mae_base],
'의미': ['가까운 시각이 공부·시험 양쪽에 섞임', '처음 보는 미래 기간을 시험', '공정 지연을 무시', '센서 정보를 전혀 안 씀']
}).round(3)
display(result)

# 막대그래프 (그래프 글자는 영어)
labels = ['A. Random split (lag 37)', 'B. Time split (lag 37)', 'B. Time split (same time)', 'Baseline (mean)']
plt.figure(figsize=(9, 4))
plt.barh(labels, result['MAE(점)'], color=['lightgray', 'tab:blue', 'tab:orange', 'silver'])
plt.gca().invert_yaxis()
plt.title('MAE Comparison (smaller is better)')
plt.xlabel('MAE (quality index points)')
plt.grid(axis='x', alpha=0.3)
plt.show()

# 💡 해석 (숫자는 실행 결과에서 자동으로 채워집니다)
improve_vs_base = (1 - mae_time / mae_base) * 100
improve_vs_now = (1 - mae_time / mae_now) * 100
print(f'💡 해석 1: 소프트센서는 미래 기간에서 평균 {mae_time:.2f}점 틀립니다. 평균값으로 찍는 것보다 오차가 {improve_vs_base:.0f}% 작습니다.')
print(f'💡 해석 2: 같은 시각 값을 쓰면 {mae_now:.2f}점, 37분 전 값을 쓰면 {mae_time:.2f}점 → 시간을 맞추니 오차가 {improve_vs_now:.0f}% 줄었습니다.')
print('💡 해석 3:', np.where(mae_random < mae_time,
f'무작위 분할({mae_random:.2f}점)이 시간순({mae_time:.2f}점)보다 좋아 보입니다. 섞인 시간 덕분에 과대평가됐을 수 있습니다.',
f'이번에는 시간순({mae_time:.2f}점)이 무작위({mae_random:.2f}점)보다 좋았습니다. 항상 그런 법칙은 없으며 데이터에 따라 다릅니다.'))
print('💡 결론: 현장에 쓸지 판단할 때는 시간순 분할(실험 B)의 점수를 기준으로 합니다.')

# %% [markdown]
# ### 셀 24 — 📊 결과물 ⑥ : 미래 기간의 실제 vs 예측 그래프
# 숫자 하나보다 **그래프를 먼저** 봅니다. 예측선이 실제선을 얼마나 잘 따라가나요?

# %%
test_time = table.loc[test_mask, 'sample_time']
plt.figure(figsize=(13, 4.5))
plt.plot(test_time, yte_t, color='black', linewidth=1.5, label='Actual quality (lab)')
plt.plot(test_time, pred_t, color='tab:blue', linestyle='--', label='Soft sensor (lag-37 inputs)')
plt.plot(test_time, pred_now, color='tab:orange', linestyle=':', alpha=0.8, label='Same-time inputs (no lag)')
plt.title('Test Period (future): Actual vs Predicted Quality Index')
plt.xlabel('Sample time')
plt.ylabel('Quality Index (score)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 오차가 가장 컸던 5개 시각 — 원인을 찾아볼 후보
check = pd.DataFrame({'sample_time': test_time, 'actual': yte_t, 'predicted': pred_t})
check['error'] = (check['actual'] - check['predicted']).abs()
print('▶ 오차가 가장 큰 5개 시각 (원인 점검 후보)')
display(check.sort_values('error', ascending=False).head(5))

# 📈 그래프 읽는 법
#  - 검정(실제)과 파랑 점선(소프트센서)이 대체로 같은 방향으로 오르내리면 추세를 잡은 것입니다.
#  - 주황 점선(시차 무시)은 실제보다 '조금 앞서' 움직이는 곳이 보입니다 → 시간이 안 맞은 흔적.
#  - 한 구간에서 계속 벌어지면 원인을 찾습니다: 센서 누락? 지연 시간 변화? 운전 상태 변화? 원료 변화?
#  - 꼭짓점(아주 높거나 낮은 값)은 덜 맞힙니다 → 랜덤포레스트는 '배운 사례들의 평균'으로 답하기 때문.

# %% [markdown]
# ### 셀 25 — ✅ 확인 카드 C : 좋은 점수보다 중요한 다섯 가지 질문
# 아래 답을 보고서에 그대로 옮겨 적을 수 있습니다.

# %%
card = pd.DataFrame({
'질문': ['Q1 미래 정보가 입력에 들어갔나?', 'Q2 측정 시각과 결과 등록 시각을 구분했나?', 'Q3 정지·기동 구간은 처리했나?', 'Q4 미래 구간의 MAE는?', 'Q5 새 실측으로 다시 평가할 계획인가?'],
'이번 실습의 답': ['아니오 — 입력은 모두 37분 이전 센서값, 시차 찾기는 학습 구간에서만',
'예 — sample_time 기준으로 결합, result_time은 입력에 쓰지 않음',
f'예 — 최근 60분이 모두 RUN인 행만 사용, {n_not_run}행 제외(건수 보고)',
f'{mae_time:.2f}점 (무작위 분할 {mae_random:.2f}점은 참고용)',
'예 — 센서 교체·생산 조건 변화 뒤에는 다시 평가']
})
display(card)

# %% [markdown]
# ### 셀 26 — (선택) 결과 파일 내려받기
# 시험 구간의 실제·예측 값을 CSV로 저장해 보고서에 활용합니다.

# %%
check['pred_same_time'] = pred_now
check.to_csv('softsensor_test_result.csv', index=False)
files.download('softsensor_test_result.csv')

# %% [markdown]
# ---
# ## 🤔 생각해 보기 (보고서용 질문)
# 1. 10시에 바꾼 운전 조건을 10시 품질 검사와 바로 비교하면 왜 관계가 흐려질까?
# 2. 시차 곡선에서 50분으로 밀면 왜 다시 상관이 약해질까?
# 3. 정지 구간을 다시 넣고 학습하면 어떤 위험이 생길까?
# 4. 내일 품질을 맞히려는 AI라면, 실험 A와 B 중 어느 점수를 믿어야 할까?
#
# > **오늘의 한 문장** — 좋은 AI는 미래의 답을 미리 보는 AI가 아니라, 과거 정보만으로 미래를 제대로 시험받은 AI다.
