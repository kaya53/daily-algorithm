# 소요시간 1시간 python 44ms

import sys

sys.stdin = open('input.txt')


def solution():
    n = int(input())
    snow = list(map(int, input().split()))

    for day in range(1, 1441):
        # 매번 정렬해주는 게 포인트!
        # 매번 가장 많이 쌓인 곳부터 치워준다
        snow.sort(reverse=True)
        snow = calc(n, snow)
        if snow.count(0) == n: return day
    return -1


def calc(n, snow):
    for i1 in range(n):
        if not snow[i1]: continue
        for i2 in range(i1 + 1, n):
            if not snow[i2]: continue
            snow[i1] -= 1
            snow[i2] -= 1
            return snow
    for k in range(n):
        if snow[k]:
            snow[k] -= 1
            return snow


print(solution())