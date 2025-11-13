# 558. Красота требует жертв https://coderun.yandex.ru/problem/beauty-sacrifice/description

import numpy as np

def foo(i,k):
    # если запрашиваемая вещь есть в наличии и ее стоимость нам по карману
    if items[i][0] == 1 and items[i][1] <= k:
        print(1)
        return [i]
  
    orig_features = items[i,2:] # признаки запрашиваемой вещи
    candidates = items[:,2:] # признаки всех вещей
    distances = np.sum((orig_features - candidates)**2, axis=1) # расстояние от запрашиваемой вещи до всех остальных
    flags = np.where((items[:,1]<=k) & (items[:,0]==1), distances, np.inf) # если вещь не удовлетворяет требованиям (нет в наличии или цена слишком велика), то заменяем расстояние до нее на бесконечность
    print(5)
    return np.argsort(flags)[:5] # сортируем список с расстояниями и выбираем первые 5

# количество вещей, количество запросов
n,q = map(int, input().split())
items = []

# складываем вещи и запросы в списки
for _ in range(n):
    items.append(list(map(int, input().split())))

items = np.array(items)

# выводим ответ
for _ in range(q):
    i, k = map(int, input().split())
    print(*foo(i, k))
