# 타이타닉 데이터셋 : 로지스틱 회귀 분석 
# 250429

#데이터 불러오기 및 확인 
import pandas as pd
file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/titanic.csv'
data = pd.read_csv(file_url) # 데이터셋 읽기
data.head()

# 전처리 : 범주형 변수 변환
data = data.drop(['Name','Ticket'], axis=1) # Name과 Ticket 변수 삭제

    # 남은 두 object형 one-hot incoding 
data = pd.get_dummies(data, columns = ['Sex','Embarked'], drop_first = True) 

data.describe() # 통계 정보 출력
data.info()

    # 시각화
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(data.corr()) # 상관관계에 대한 히트맵 생성
plt.show() # 그래프 출력(최근 버전에서는 제외 가능)
sns.heatmap(data.corr(), cmap='coolwarm', vmin=-1, vmax=1, annot=True)
plt.show()

    # 변수 고윳값 확인 
for i, name in enumerate(data.columns):
    print(f'{i} {name} : {set(data[name])}')

data.info()
data.corr() # 상관관계 출력

# 모델링 및 예측
from sklearn.model_selection import train_test_split
X = data.drop('Survived', axis = 1)
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

    # 모델 학습 및 예측 
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression(max_iter=1000) # 모델이 완전히 수렴하도록 최대반복횟수 설정 
model.fit(X_train, y_train)
pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred) # 실제값과 예측값으로 정확도 계산 
# 정확도 0.7808988764044944

# 모델이 학습한 변수의 가중치 확인 
model_coef = pd.Series(model.coef_[0], index=X.columns) #컬러 이름 매핑 
model_coef 
'''
Pclass       -1.182269
Age          -0.039923
SibSp        -0.321323
Parch         0.007930
Sex_male     -2.568671
Embarked_Q   -0.078756
Embarked_S   -0.235564'''

# feature engeering
    # SibSp와 Parch 변수 합치기
data['family'] = data['SibSp'] + data['Parch'] 
    # SibSp와 Parch 변수 삭제
data.drop(['SibSp','Parch'], axis=1, inplace=True) 
data.head() 

# 모델링 및 예측
from sklearn.model_selection import train_test_split
X = data.drop('Survived', axis = 1)
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=150)

    # 모델 학습 및 예측 
from sklearn.linear_model import LogisticRegression 
model = LogisticRegression(max_iter=1000) # 모델이 완전히 수렴하도록 최대반복횟수 설정 
model.fit(X_train, y_train)
pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred) # 실제값과 예측값으로 정확도 계산 
# 정확도 0.8033707865168539

# 모델이 학습한 변수의 가중치 확인 
model_coef = pd.Series(model.coef_[0], index=X.columns) #컬러 이름 매핑 
model_coef 
'''
Pclass       -1.109578
Age          -0.033839
Sex_male     -2.546131
Embarked_Q    0.002236
Embarked_S   -0.522834
family       -0.225614'''
