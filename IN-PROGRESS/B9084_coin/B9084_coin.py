# 소요시간 20분 python 52ms
# 어제 푼 문제랑 유사 - 123 더하기 4
# 1. 첫번째 동전의 배수인 금액은 무조건 경우의 수 1씩 있음
# 2. 나머지 동전에 대해서는 i-coin의 경우의 수를 더해준다.
    # - 나머지 동전에 대해서는 경우의 수 1씩 안채워줘도 되는 이유?
    # => 0원일 때도 1로 채워주는데 예를 들어 5원이면 처음 for문을 돌 때 dp[0]에서 1을 가져와서 계속 늘려주기 때문
    # - 그리고 이 과정에서 동전이 섞여서 되는 경우들도 겹쳐서 세지는 것 없이 더해진다
import sys

sys.stdin = open('input.txt')


def solution(n, coins, m):
    dp = [0] * (m+1)
    for i in range(n):
        coin = coins[i]
        if not i:  # 첫 번째 동전만 써서 채우는 경우
            for k in range(0, m+1, coin):
                dp[k] = 1
        else:
            for z in range(coin, m+1):
                dp[z] += dp[z-coin]
    return dp[m]


T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    M = int(input())
    print(solution(N,C,M))