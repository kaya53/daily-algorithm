def solution(triangle):
    h = len(triangle)  # 높이
    dp = []
    for tri in triangle:
        dp.append([0] * (len(tri)))

    dp[0][0] = triangle[0][0]
    for i in range(1, h):
        for j in range(len(triangle[i]) - 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + triangle[i][j + 1])

    return max(dp[h - 1])