# 566. Пушистики https://coderun.yandex.ru/problem/fuzzies?compiler=python

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, t = map(int, input().split())
    times = sorted(map(int, input().split()))

    times_sum = 0
    for i in range(n):
        times_sum += times[i]
        if times_sum > t:
            print(i-1)
            break
    print(i)



if __name__ == '__main__':
    main()
