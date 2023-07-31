import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# 데이터 로드
train_data = pd.read_csv('/Users/mac/Downloads/data_train.csv')
test_data = pd.read_csv('/Users/mac/Downloads/data_test.csv')

# 특성과 레이블 분리
X_train = train_data.iloc[:, :-1]
y_train = train_data['weather label']

# 결측치 처리
imputer = SimpleImputer()
X_train_imputed = imputer.fit_transform(X_train)

# 표준화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)

# 모델 학습
model = LogisticRegression(max_iter=2000)
model.fit(X_train_scaled, y_train)

# 테스트 데이터 전처리
X_test_imputed = imputer.transform(test_data)
X_test_scaled = scaler.transform(X_test_imputed)

# 테스트 데이터 예측
y_test_pred = model.predict(X_test_scaled)

# 예측 결과 저장
prediction_df = pd.DataFrame({'predicted_label': y_test_pred})
prediction_df.to_csv('predicted_labels.csv', index=False)
