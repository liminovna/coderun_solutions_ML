# 214. Рестораны https://coderun.yandex.ru/problem/restaurants/

import sys


def main():

    '''
    Коэффициенты получены следующим образом

    # Читаем данные
    data = []
    with open('restaurants_train.txt') as f:
    for _ in f.readlines():
        data.append(list(map(float, _.split())))

    # Кладем их в датафрейм
    import pandas as pd

    df = pd.DataFrame(data)
    df.columns = ['winner', 'rating1', 'rating2', 'distance1', 'distance2']

    # Разделяем данные по первому и второму ресторанам в отдельные датафреймы, 
    # чтобы далее сложить их в один датафрейм вертикально
    df_pt2 = df[['winner', 'rating2', 'distance2']]

    df.drop(columns=['rating2', 'distance2'], inplace=True)

    df.columns = 'winner', 'rating', 'distance'
    df_pt2.columns = 'winner', 'rating', 'distance'

    # Для вычисления весов будем использовать логистическую регрессию, 
    # а в качестве классов будут значения 1 и 0 -- выиграл или проиграл.
    # Для "вторых" ресторанов мы должны "развернуть" ответы.
    df_pt2['winner'] = 1-df_pt2['winner']

    df = pd.concat([df, df_pt2])

    # убираем "равные" рестораны
    df.drop(df[df['winner']==0.5].index, inplace=True)

    # обучаем логистическую регрессию
    from sklearn.linear_model import LogisticRegression

    lr = LogisticRegression()
    # df[['rating', 'distance']] = scaler.fit_transform(df[['rating', 'distance']])

    lr.fit(df[['rating', 'distance']], df['winner'])

    r_w, d_w = lr.coef_
    '''

    r_w = -0.21787759
    d_w = 0.55446636

    n = int(sys.stdin.readline())
    for _ in range(n):
        r, d = map(float, sys.stdin.readline().split())

        if r == -1:
            r = 5.0

        score = - r*r_w - d*d_w
        print(score)


if __name__ == '__main__':
    main()
