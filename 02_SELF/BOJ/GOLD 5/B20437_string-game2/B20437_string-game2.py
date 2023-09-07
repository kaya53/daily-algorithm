# 소요시간 1시간 pypy 324ms
# - 처음에 알고리즘 분류가 슬라이딩 윈도우인걸 보고 이걸로 접근했다가 시간 잡아먹음
# - 딕셔너리로 쉽게 풀 수 있는 문제였다.
# 틀린 이유
# 1. i2의 시작 범위를 i1+1로 하면 K=1인 경우를 못잡는다 
import sys

sys.stdin = open('input.txt')

from collections import defaultdict

T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())

    alpha_dict = defaultdict(list)
    for idx, char in enumerate(W):
        alpha_dict[char].append(idx)

    mmin = int(1e9)
    mmax = 0
    for val in alpha_dict.values():
        if len(val) < K: continue

        for i1 in range(len(val)):
            for i2 in range(i1, len(val)):
                if i2 - i1 + 1 == K:
                    now = val[i2] - val[i1] + 1
                    if mmax < now: mmax = now
                    if mmin > now: mmin = now
    if mmin == 10001 or not mmax: print(-1)
    else: print(mmin, mmax)

