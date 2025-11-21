# 1. Найди кота! https://coderun.yandex.ru/selections/2024-summer-ml/problems/cat-search
import sys
from collections import deque


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    matrix = []
    for l in sys.stdin.readlines():
        matrix.append(list(map(int, l.strip().split())))

    n = len(matrix)
    m = len(matrix[0])
    visited = [[False]*m for _ in range(n)]

    def check_pos(r,c):
        return 0<=r<n and 0<=c<m and matrix[r][c] == 1 and not visited[r][c]

    deq = deque()

    cat_count = 0

    new_matrix = [[0]*m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if not visited[row][col] and matrix[row][col] == 1:
                # print((row, col))
                # res = []
                deq.append((row, col))
                # print(deq)
                while deq:
                    # print(deq)

                    cur_row, cur_col = deq.pop()
                    visited[cur_row][cur_col]=True
                    # res.extend((cur_row, cur_col))
                    new_matrix[cur_row][cur_col] = cat_count + 1
                    # print(new_matrix)

                    # left
                    if check_pos(cur_row, cur_col-1):
                        deq.append((cur_row, cur_col-1))
                        # print(deq)
                    # right
                    if check_pos(cur_row, cur_col+1):
                        deq.append((cur_row, cur_col+1))
                        # print(deq)
                    # top
                    if check_pos(cur_row-1, cur_col):
                        deq.append((cur_row-1, cur_col))
                        # print(deq)
                    # bottom
                    if check_pos(cur_row+1, cur_col):
                        deq.append((cur_row+1, cur_col))
                        # print(deq)
                # cats.append(res)
                cat_count+=1

    print(cat_count)
    for i in new_matrix:
        print(*i)




if __name__ == '__main__':
    main()
