# 소요시간 의미없음 python 52ms
# 풀이가 어렵다기 보다 아이디어가 어려운 문제!

# 풀이
# - 1 ~ n까지 정렬을 해야 한다 => 즉, 오름차순이 되도록 해야 하므로
# - 이 오름차순 흐름에 맞지 않는 숫자는 위치를 옮겨줘야 하는 것이다
# - 그래서 가장 긴 증가하는 부분 수열을 구해야 한다
#   => 이 것들은 이미 오름차순의 형태를 띄고 있으므로 위치를 옮겨줄 필요가 없다
# - 그리고 n에서 이 부분 수열의 길이를 빼주면 된다
import sys

sys.stdin = open('input.txt')


def solution(n, nums):
    dp = [1] * n
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                dp[j] = max(dp[i]+1, dp[j])
    return n - max(dp)


a = int(input())
b = [int(input()) for _ in range(a)]
print(solution(a, b))