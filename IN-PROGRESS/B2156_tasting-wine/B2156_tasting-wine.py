# 소요시간 의미없음 python 48ms
# dp
# 연속으로 3잔을 먹을 수 없음
# 1. 두 잔 전 최대 + i번째 와인(한 칸 띄고 나한테 온 것) 
# 2. 3잔 전 최대 + i-1번째 와인 + i번째 와인(연속으로 나에게 왔기 때문에 3잔 전 최대를 계산해준다)
# 3. 한 잔 전 최대: i번째 와인을 마시지 않음
    # 2579 계단 오르기에서는 마지막 칸을 반드시 밟아야 한다고 했음
    # => 현재 계단을 밟지 않는 걸 고려할 필요가 없음
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(n, wines):
    dp = [0] * n
    dp[0] = wines[0]
    # n이 1이상이기 때문에 앞에 if문 안넣어주면 index error 난다
    if n > 1: dp[1] = wines[0] + wines[1]
    if n > 2: dp[2] = max(wines[0]+wines[2], wines[1]+wines[2], dp[1])
    for i in range(3, n):
        # 두 개 전 최대 + 자신 / 3개 전 최대 + 하나 전 + 자신 / 하나 전 최대 + 나 안 마시기
        dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i], dp[i-1])
    return dp[n-1]


N = int(input().rstrip())
ls = [int(input().rstrip()) for _ in range(N)]
print(solution(N, ls))