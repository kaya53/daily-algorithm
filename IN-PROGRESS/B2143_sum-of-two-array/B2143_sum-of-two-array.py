# 1. a, b 각 배열의 누적합을 구한다
# 2. 투 포인터를 활용해 각각 부 배열의 합을 구한다
    # - 이중 포문을 써서 a의 부배열의 합이 ~~일 때, b 부배열의 합은 ~~
    # - (1,000,000) 최대 백만번 연산
    # - 투 포인터의 위치를 이진 탐색으로..?
    # - a의 부배열의 합은 T 미만이어야 하고
    # - b 부배열의 합은 T-(a부배열의 합) 이 되는 것

import sys

sys.stdin = open('input.txt')


def accumulate(l, arr):
    res = [0] * l
    res[0] = arr[0]
    for i in range(1, l):
        res[i] = res[i-1]+arr[i]
    return res


def solution(t, n, arrA, m, arrB):
    accumA = accumulate(n, arrA)
    accumB = accumulate(m, arrB)

    la, ra = 0, 0
    while la < n and ra < n:
        now = accumA[ra]-accumA[la-1] if la else accumA[ra]
        print(la, ra, now)
        if now >= t:  # 부배열의 합을 줄여야 함
            la += 1
        else:  # b 부배열 탐색해도 됨
            ra += 1

            


solution(int(input()), int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split())))