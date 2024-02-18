def solution(elements):
    N = len(elements)
    dp = elements[:]
    elements = 2 * elements
    answer = set(dp)
    for i in range(2, N):
        for j in range(N):
            dp[j] = dp[j] + elements[j+i-1]
            answer.add(dp[j])
    return len(answer) + 1