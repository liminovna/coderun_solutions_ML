# 282. D-CoV-3999 https://coderun.yandex.ru/problem/dcov3999
import sys


def main():
    n = int(input()) # кол-во человек
    a = list(map(int, input().split())) # утренние результаты ПЦР

    infected = set([i for i in range(n) if a[i] == 1]) # список зараженных

    person_meeting = {} # словарь сотрудник: [встреча1, встреча2, ...]
    for i in range(n):
        seq = list(map(int, input().split()))
        if seq[0] != 0:
            person_meeting[i] = sorted(seq[1:])

    meeting_person = {} # словарь встреча: [сотрудник1, сотрудник2, ...]
    for p, ms in person_meeting.items():
        for m in ms:
            if m not in meeting_person.keys():
                meeting_person[m] = []
            meeting_person[m].append(p)

    infected_meetings = set()

    # теперь определяем заболевших в течение дня, обновляя список "зараженных" встреч
    for m in sorted(meeting_person.keys()):
        ps = meeting_person[m]
        if any(p in infected for p in ps):
            infected.update(ps)

    print(*[1 if i in infected else 0 for i in range(n)])        

if __name__ == '__main__':
    main()
