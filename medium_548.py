# 548. Исправить все опечатки https://coderun.yandex.ru/problem/fix-all-misprints/description

# Файл с ответом не принимается системой (хз почему), правильный ли ответ -- неизвестно

! unzip task_1.zip

import numpy as np

dct = set(np.loadtxt('dict.txt', dtype=str, usecols=(0,)))
# len(dct) # 61988

def calc_edit_dist(source, target, i=1,d=1,s=1,sw=1):
    """
    Считаем расстояние редактирования. Помимо операций insert, delete, substitute добавлена swap -- перестановка двух соседних букв
    """

    source_word = '#' + source # первое слово
    target_word = '#' + target # второе слово

    n = len(source)
    m = len(target)

    dp = [[0]*(m+1) for row in range(n+1)] # создаем пустую матрицу

    # заполняем матрицу в первой строке
    for row in range(n+1):
      dp[row][0] = row*d

    # заполняем матрицу в первом столбце
    for col in range(m+1):
      dp[0][col] = col*i

    dp = np.array(dp)

    for row in range(1,n+1):
      for col in range(1,m+1):
        # print(row, col)
        # print(source_word[row], target_word[col])
        if source_word[row] == target_word[col]: # если текущие буквы совпадают
        #   # print(source_word[row], target_word[col])
          dp[row, col] = dp[row-1, col-1]

        else:
            dp[row,col] = min(
            dp[row-1, col]+d,
            dp[row-1, col-1]+s,
            dp[row, col-1]+i
            )

            # если предыдущая буква равна букве, которая стоит по тому же индексу в "правильном" слове и наоборот, то считаем, что это операция swap 
            if source_word[row] == target_word[col-1] and source_word[row-1] == target_word[col]:
                # print('!')
                dp[row,col] = min(dp[row,col], dp[row-1,col-1])

    # print(*dp, sep='\n')
    # print(dp[-1,-1])
    return (dp[-1,-1], dp)
    # print(dp)

def get_sequence(dp, source, target):
    """
    Применить операции редактирования к слову с опечаткой, чтобы оно превратилось в "ближайшее" слово из словаря
    """
    sequence = []
    idx_seq = []
    i, j = len(source), len(target)

    while i > 0 or j > 0:
        idx_seq.append((i,j))
        # print(sequence)
        if i > 0 and j > 0 and source[i - 1] == target[j - 1]:
            # буквы совпадают
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] == dp[i][j - 1] == dp[i - 1][j]:
            # swap
            i -= 2
            j -= 2
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            # substitute
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            # delete
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            # insert
            j -= 1


    # print(idx_seq)
    source_word = '#' + source # первое слово
    target_word = '#' + target # второе слово
    sequence = []
    prev_seq = list(source_word) # список слов, к которому мы будем применять операции редактирования

    for i,j in list(reversed(idx_seq)):
        # print(i, j, source_word[i],target_word[j], sequence)
        # буквы совпали
        if source_word[i] == target_word[j]:
            # print(i, j, source_word[i],target_word[j], 'match')
            pass
        # перестановка двух соседних букв
        elif dp[i][j] == dp[i - 1][j - 1] == dp[i][j - 1] == dp[i - 1][j]:
            # print(prev_seq[i-1], prev_seq[i-2])
            prev_seq[i] = target_word[j]
            prev_seq[i-1] = source_word[i]
            sequence.append(prev_seq.copy())
            # print(i, j, source_word[i],target_word[j], 'swap', prev_seq)
        # замена буквы
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            # print(prev_seq[i-1])
            prev_seq[i] = target_word[j]
            sequence.append(prev_seq.copy())
            # print(i, j, source_word[i],target_word[j], 'substit', prev_seq)
        # удаление
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            prev_seq[i] = ''
            sequence.append(prev_seq.copy())
            # print(i, j, source_word[i],target_word[j], 'del', prev_seq)
        # добавление
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            prev_seq[i] = prev_seq[i] + target_word[j]
            sequence.append(prev_seq.copy())
            # print(i, j, source_word[i],target_word[j], 'insert', prev_seq)


    return list(map(lambda x: ''.join(x).replace('#', ''), sequence))


def foo(src, dct):
    """
    Ищем "ближайшее" слова из словаря для слова с опечаткой
    """
    # если слово все-таки без опечатки, то возвращаем его же
    if src in dct:
        return (src, 0)

    best_cand = '' # "ближайшее" слово
    best_score = float('inf') # наименьшее расстояние до словарного слова
    best_dp = None # таблица для рассчета расстояния редактирования до "ближайшего" слова

    # try:

    # проходимся по каждому слову из словаря
    for i, targ in enumerate(dct):
        # print(i, src, targ)
        if not(len(src) > 2 and len(set(src) ^ set(targ)) > 2):
            dist, dp = calc_edit_dist(src, targ)
            if dist == 1:
                return (src, 1, targ)
            if dist < best_score:
                best_cand = targ
                best_score = dist
                best_dp = dp

    # print(best_score)
    if best_score > 2:
        return (src, '3+')

    # print(src, best_score, best_cand)
    return (src, 2, *get_sequence(best_dp, src, best_cand))


with open('queries.txt') as f, open('answer.txt', 'a+') as o:
    cntr = 0
    while cntr <= 100_000:
        cntr += 1
    
        src = f.readline().strip()
        # print('starting', src)
        print(*foo(src, dct), file=o, end='\n')

        # каждые 1000 строк сообщаем, где мы
        if cntr % 1000 == 0:
            print(cntr)
