# 소요시간 20분: python 88ms
# i번째 최대값으로 가능한 모든 경우의 생각해봐서 비교한다
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(n, nums):
    dp = nums[:]

    for i in range(1, n):
        # 직전까지 최대+현재 수, 현재 수만, 직전 수 + 현재 수
        dp[i] = max(dp[i-1]+ nums[i], dp[i], nums[i-1]+nums[i])
    return max(dp)

# for _ in range(5):
print(solution(int(input()), list(map(int, input().rstrip().split()))))