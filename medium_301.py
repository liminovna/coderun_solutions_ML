# 301. Бутылки рома https://coderun.yandex.ru/problem/bottles-of-rum/description?compiler=python

from itertools import combinations
from collections import Counter
import math


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    with open('input.txt') as f:
        letters = f.readline()

    n = len(letters) # длина последовательности

    # записываем все возможные комбинации из кол-ва элементов <= n
    comb = {}
    for i in range(1,n + 1):
        comb[i] = list(combinations(letters,i))

    # оставляем из комбинаций только уникальные (на случай если есть повторяющиеся буквы)
    uniq_comb = set()
    for c in comb.values():
        for letter in c:
            uniq_comb.add(tuple(sorted(letter)))

    res = 0
    for c in uniq_comb:
        # используем формулу для distinguishable permutations n!/(n_1!*n_2!*...)
        denom = 1
        n_fact = math.factorial(len(c))
        cntr = Counter(c) # счетчик букв в конкретной комбинации
        for v in cntr.values():
            denom *= math.factorial(v)
        res += n_fact/denom
    print(int(res))


if __name__ == '__main__':
    main()
