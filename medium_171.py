# 171. Коллекция статуэток https://coderun.yandex.ru/problem/collection-of-figurines/

from collections import defaultdict, Counter

n, k = map(int, input().split())
seq = list(map(int, input().split()))
required = set(range(1, k + 1))
cnt = Counter()
cur_cost, min_cost, l = 0, float('inf'), 0

for r in range(n):
  # фаза "накопления": идем по последовательности, 
  # пока не наберем все необходимые типы статуэток.
  # Попутно считаем накопительным итогом стоимость и считаем,
  # сколько раз встретился каждый тип статуэтки
  right_item = seq[r]
  if right_item in required:
    required.discard(right_item)
  cnt[right_item] += 1
  cur_cost += right_item

  # фаза "отбрасывания лишнего" с левой стороны: левый указатель двигаем вперед,
  # и вычитаем из суммы все что встречается на пути.
  # Двигаем до тех пор, пока у нас не станет не хватать одного любого типа статуэтки.
  # Тогда возвращаемся к фазе накопления. 
  while not required:
    left_item = seq[l]
    min_cost = min(min_cost, cur_cost)
    cnt[left_item] -= 1
    cur_cost -= left_item
    if not cnt[left_item] and left_item <= k:
      required.add(left_item)
    l += 1
print(min_cost)
