# 소요시간 27분 python 48ms
# 현재 잔을 안 마시는 게 최대일 수도 있음!
import sys

sys.stdin = open('input.txt')


def solution(n, wines):
    dp = [0] * n

    dp[0] = wines[0]
    if n > 1: dp[1] = wines[0] + wines[1]
    if n > 2: dp[2] = max(wines[2]+wines[0], wines[2]+wines[1], dp[1])

    for i in range(3, n):
        # 지금 잔을 안마시는 게 이득일 수도 있음
        dp[i] = max(wines[i]+wines[i-1]+dp[i-3], wines[i]+dp[i-2], dp[i-1])
        # print(dp)
    return max(dp)


n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))
print(solution(n, ls))