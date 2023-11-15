# 소요시간 의미 없음 pypy 140ms
# - 각 인덱스까지 공통 수열을 구할 때, 주어진 두 수열 간에 보고 있는 인덱스가 다를 수 있다
# - 그 인덱스를 어떻게 표시해야 하나 고민했는데
# dp 리스트를 2차원으로 만들어서 각 행, 열 인덱스가 수열의 인덱스가 되도록 하면 된다
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]  # 첫번째 알파벳들도 정상적으로 비교하기 위해 행, 열을 하나씩 늘려줌

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 보고 있던 인덱스를 하나씩 증가
            else:  # 다르면 이전 숫자 그대로 가져오기
                # 2번째 문자열에서 지금 인덱스보다 하나 전 값 // 1번째 문자열에서 지금 인덱스보다 하나 전 값 중에서 큰 것
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[n][m]


print(solution(list(input().rstrip()), list(input().rstrip())))