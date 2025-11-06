# 271. Интерполяция https://coderun.yandex.ru/problem/interpolation/description
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    X_train = []
    y_train = []

    X_test = []

    for _ in range(1000):
        inp = list(map(float, input().split()))
        X_train.append(inp[:-1])
        y_train.append(inp[-1])

    for _ in range(1000):
        inp = list(map(float, input().split()))
        X_test.append(inp)

    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)

    lr = LinearRegression()
    lr.fit(X_train_poly, y_train)

    y_pred = lr.predict(poly.transform(X_test))
    print(*y_pred, sep='\n')
    

if __name__ == '__main__':
    main()
