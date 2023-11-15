import sys

sys.stdin = open('input.txt')


def solution(n, k, ls):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, k+1):  # 남은 무게
            now_w, now_v = ls[i]

            if j < now_w:  # 넣을 수 없음
                dp[i][j] = dp[i-1][j]
            else:  # 넣을 수 있으면 넣고, 안넣고 경우 나눠 생각하기
                dp[i][j] = max(now_v+dp[i-1][j-now_w], dp[i-1][j])
    return dp[n][k]


n, k = map(int, input().split())
ls = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

print(solution(n, k, ls))