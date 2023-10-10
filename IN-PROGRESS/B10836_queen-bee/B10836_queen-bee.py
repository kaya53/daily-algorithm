# 소요시간: 의미없음 pypy 3264ms / 2580ms
# 머리를 써야 하는 구현!
# 불필요한 연산은 최대한 줄이고 꼭 필요한 연산만 해야 한다

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    n, k = map(int, input().rstrip().split())
    arr = [1] * (2*n-1)

    for _ in range(k):
        zero, one, two = map(int, input().rstrip().split())
        for k in range(zero, zero+one):
            arr[k] += 1
        for z in range(zero+one, zero+one+two):
            arr[z] += 2

    for i in range(n):
        for j in range(n):
            if j == 0: print(arr[n-(i+1)], end=' ')
            else: print(arr[n+j-1], end=' ')
        print()


solution()