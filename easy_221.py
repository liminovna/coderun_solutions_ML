# 221. Линейно разделимая выборка https://coderun.yandex.ru/problem/linear-separability-problem

import numpy as np


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    data = []
    target = []

    for _ in range(n):
        line = list(map(float, input().split()))
        data.append(line[:-1])
        target.append(line[-1])

    print(*np.linalg.lstsq(data, target, rcond=None)[0])

if __name__ == '__main__':
    main()
