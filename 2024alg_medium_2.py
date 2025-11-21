# 2. Поход в горы https://coderun.yandex.ru/selections/2024-summer-ml/problems/mountain-trip/description?compiler=pypy
import sys

def calc_limit(limit, times, n):
    # сортируем список прибывающих
    times.sort()

    # если посетителей меньше, чем вместимость, то можем сразу вернуть ответ inf
    if len(times) <= limit:
        print('INF')
        return

    def is_valid(guess):
      '''
      Проверяем, подходит ли предполагаемое значение, т.е. уместятся ли все посетители при условии, что они проведут в гостинице GUESS часоов
      '''
      t2_idx = 0
      for t_idx in range(n):
          # ищем количество посетителей в гостинице, которые прибудут строго до момента отбытия посетителя под индексом t
          while t2_idx < n and times[t2_idx] < times[t_idx] + guess:
              t2_idx += 1
              # если за это время в гостинице набирается больше заданного ограничения limit, то значение guess нам не подходит
              if t2_idx - t_idx > limit:
                  return False
      return True

    # ищем бинарным поиском длительность посещения mid
    left = 0
    right = times[-1] - times[0] # разница во времени между 0 и последним прибывшим
    res = 0

    
    while left <= right:
        mid = (left + right) // 2 # начинаем поиск ответа со срединного значения между left и right

        # если mid позволяет разместить всех посетителей, продолжаем искать как бы по правую сторону от mid, 
        # т.к. возможно, есть другое подходящее значение, при котором можно разместить большее количество человек
        if is_valid(mid):
            res = mid
            left = mid + 1
        # если mid слишком большое, т.е. за указанное количество часов в гостиннице собирается слишком много посетителей, 
        # то продолжаем искать меньшее значение как бы по левую сторону от mid
        else:
            right = mid - 1
          
    # если подходящего значения не нашлось
    if res == 0:
        print("Impossible")
        return
    print(res)
    return


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, limit = map(int, input().split())
    times = [int(input()) for _ in range(n)]
    calc_limit(limit, times, n)


if __name__ == '__main__':
    main()
