# 562. 1984 https://coderun.yandex.ru/problem/1984/description

import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n_stop, m_messages = map(int, input().split())

    stop_words = []
    for _ in range(n_stop):
        stop_words.append(input())

    for _ in range(m_messages):
        message = input()
        flag = 1 # 1 - keep, 0 - delete
        for s in stop_words:
            if s in message:
                flag = 0
                break
        if flag == 1:
          print('KEEP')
        else:
          print('DELETE')

    
if __name__ == '__main__':
    main()
