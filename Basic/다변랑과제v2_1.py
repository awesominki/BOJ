import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib

# 데이터 불러오기
data = pd.read_csv('/Users/mac/Downloads/data_train.csv')

# 입력 변수(X)와 레이블(y)로 분할
X = data.iloc[:, :-1]
y = data['weather label']

# NaN 값을 평균값으로 대체하는 Imputer 생성
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# 로지스틱 회귀 모델 생성 및 학습
model = LogisticRegression(max_iter=2600)
model.fit(X_scaled, y)

# 모델 저장
joblib.dump(model, 'training1.pkl')

