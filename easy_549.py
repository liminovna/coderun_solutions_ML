# 549. Расстояние редактирования https://coderun.yandex.ru/problem/distance-editing

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = map(int, input().split()) # длина первого слова, длина второго слова

    source_word = '#' + input() # первое слово
    target_word = '#' + input() # второе слово

    i,d,s = map(int, input().split()) # стоимость вставки, удаления, замены

    dp = [[0]*(m+1) for row in range(n+1)] # создаем пустую матрицу
    
    # заполняем матрицу в первой строке
    for row in range(n+1):
      dp[row][0] = row*d

    # заполняем матрицу в первом столбце
    for col in range(m+1):
      dp[0][col] = col*i

    for row in range(1,n+1):
      for col in range(1,m+1):
        # print(row, col)
        # print(source_word[row], target_word[col])
        if source_word[row] == target_word[col]: # если текущие буквы совпадают
        #   # print(source_word[row], target_word[col])
          dp[row][col] = dp[row-1][col-1]

        else:
          dp[row][col] = min(
            dp[row-1][col]+d,
            dp[row-1][col-1]+s,
            dp[row][col-1]+i
            )
          
    # print(*dp, sep='\n')
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
