# 200. Разминка https://coderun.yandex.ru/problem/warm-up

# разархивируем данные
!unzip test.zip
!unzip train.zip

# читаем тренировочные данные в датафрейм
import pandas as pd
df = pd.read_csv('train.tsv', delimiter='\t', header=None)
df.head()

df.describe()

# разделяем датафрейм на фичи и таргет и делим все это на трейн и тест
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df.drop(columns=[100])
y = df[100]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)

# обучаем линейную регрессию
reg = LinearRegression()

reg.fit(X_train, y_train)

# X_test = scaler.transform(X_test) 
pred = reg.predict(X_test)

# вычисляем среднюю квадратичную ошибку
import numpy as np
np.mean((pred - y_test)**2)

# читаем в отдельный датафрейм данные для ответа
test_df = pd.read_csv('test.tsv', delimiter='\t', header=None)
test_df

# делаем предсказание
# test_df = scaler.transform(test_df) 
pred = reg.predict(test_df)

# сохраняем предсказания в файл
pd.DataFrame(pred).to_csv('answer.tsv', sep='\t', index=False)
