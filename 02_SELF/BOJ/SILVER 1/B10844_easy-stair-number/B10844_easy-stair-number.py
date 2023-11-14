import sys

sys.stdin = open('input.txt')

def solution(n):
    dp = [[0] * 10 for _ in range(n)]

    dp[0] = [0] + [1] * 9

    for i in range(1, n):
        for j in range(10):
            if not j:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    return sum(dp[-1]) % 1000000000


print(solution(int(input())))