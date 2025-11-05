# 262. Лента рекомендаций https://coderun.yandex.ru/problem/recommendations
import sys
from collections import deque

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split())
    items = [] # последовательность типов постов
    for _ in range(n):
        items.append(int(input()))

    res_idx = [0] # список правильно расставленных индексов. Чтобы не заморачиваться со сравнением нулевого элемента с предыдущим (которого не существует), складываем его заранее в список, а итерироваться начинаем с первого элемента
    deq_idx = deque()

    for l in range(1, n): # итерируемся с первого элемента, т.к. нулевой уже добавлен в результирующий список
        if items[l] != items[res_idx[-1]]: # если текущий элемент не равен предыдущему
            res_idx.append(l) # складываем текущий элемент в результирующий список

            if deq_idx and items[deq_idx[0]] != items[res_idx[-1]]: # после того как мы вставили подходящий элемент, можно после него вставить отложенный элемент из очереди
                res_idx.append(deq_idx.popleft())
        else:
            deq_idx.append(l) # так как элемент повторяет предыдущий, складываем его пока в очередь

    return res_idx


if __name__ == '__main__':
    print(*main())
