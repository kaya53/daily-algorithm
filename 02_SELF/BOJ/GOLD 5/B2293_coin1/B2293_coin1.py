# 소요시간 의미 없음 pypy 132ms
# 다시 풀어보자 이해는 되지만 내가 구현은 못할 것 같다
import sys

sys.stdin = open('input.txt')


def solution(n, k, coins):
    dp = [0] * (k+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    # print(dp)
    return dp[k]


N, K = map(int, input().split())
ls = [int(input()) for _ in range(N)]
print(solution(N, K, ls))