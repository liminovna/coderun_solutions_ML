# 184. Восстановление коэффициентов https://coderun.yandex.ru/problem/coefficients-restoration/description

import pandas as pd

# загружаем данные в датафрейм
df = pd.read_csv('data.csv', header=None)
df.columns = ['x', 'y']

# рисуем точки просто из любопытства
import matplotlib.pyplot as plt
plt.scatter(df['x'], df['y'])

# фитим коэффициенты с помощью scipy.optimize.curve_fit
from scipy import optimize
import numpy as np

def func(x, a,b,c):
    y = a**2 * np.sin(x)**2 + b**2 * np.log(x)**2 + 2*a*b*np.sin(x)*np.log(x)+c*x**2
    return y

res = optimize.curve_fit(func, xdata=df['x'], ydata = df['y'])

# смотрим насколько хорошо подходят коэффициенты 
y_pred = func(df['x'], *res[0]) 

plt.scatter(df['x'], df['y'])
plt.scatter(df['x'], y_pred)

# ответ
res[0]
