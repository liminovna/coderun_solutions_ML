# 570. Лента рекомендаций https://coderun.yandex.ru/problem/recomendation-feed
n_recommended, n_picks, limit_per_topic = map(int, input().split(' ')) # первая строка ввода

# строки с названиями видео
recommended = []
for _ in range(n_recommended):
    recommended.append(input())

# строка с id видео
ids = input().split(' ')

cntr_dict = {} # словарь, куда записываются названия и сколько раз они встретились на данный момент
cntr = 0 # счетчик выведенных названий

for i in range(n_recommended):

    if cntr == n_picks: # если мы уже напечатали достаточное количество видео, то выходим из цикла
        continue

    cur_name = recommended[i] # текущее название
    cur_cntr = cntr_dict.get(cur_name, 0) # находим текущее название в cntr_dict

    if cur_cntr < limit_per_topic: # если текущего названия нет в словаре или лимит для него еще не достигнут
        print(cur_name, '#'+ids[i]) # принтим название
        cntr_dict[cur_name] = cur_cntr + 1 # обновляем счетчик для данного видео в cntr_dict
        cntr += 1 # обновляем счетчик выведенных видео

