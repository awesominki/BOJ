import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib

# 테스트 데이터 불러오기
test_data = pd.read_csv('/Users/mac/Downloads/data_test.csv')

# 입력 변수(X_test)로 사용할 데이터 전처리
X_test = test_data.copy()  # 예측할 테스트 데이터 복사

# NaN 값을 평균값으로 대체하는 Imputer 사용
imputer = SimpleImputer(strategy='mean')
X_test_imputed = imputer.fit_transform(X_test)

# 데이터 스케일링
scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test_imputed)

# 저장된 모델 불러오기
model = joblib.load('training1.pkl')

# 레이블 예측
y_pred = model.predict(X_test_scaled)

# 예측 결과를 DataFrame으로 변환
result = pd.DataFrame({'predicted_label': y_pred})

# 결과 저장
result.to_csv('result.csv', index=False)
