# 소요시간 10분 python, pypy 204ms
# 조합 문제
import sys

sys.stdin =open('input.txt')


def comb(idx, n, m, choice):
    if idx == m:
        print(*choice)
        return

    for i in range(1, n+1):
        if i in choice: continue
        choice[idx] = i
        comb(idx+1, n, m, choice)
        choice[idx] = 0


def solution(n, m):
    comb(0, n, m, [0] * m)


# for _ in range(3):
solution(*map(int, input().split()))
