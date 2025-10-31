# 177. Тайна египетских пирамид https://coderun.yandex.ru/problem/egypt
import sys
import numpy as np
from scipy import optimize

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    data = []
    for _ in range(n):
        data.append(tuple(map(float, input().split())))

    data = np.array(data)
    X = data[:,0]
    y = data[:,1]

    def func(x, a,b,c,d):
        y = a * np.tan(x) + (b * np.sin(x) + c * np.cos(x)) ** 2 + d * np.sqrt(x)
        return y

    res = optimize.curve_fit(func, xdata=X, ydata = y)[0]
    print(*map("{:.2f}".format, res))


if __name__ == '__main__':
    main()
