# 소요시간 20분 python 104ms
# dp 초기값을 잘못해놔서 틀렸다
# 각 인덱스에서 가장 큰 증가하는 수열의 기본 값은 0이 아니라 자기 자신임
import sys

sys.stdin = open('input.txt')


def solution(n, nums):
    dp = nums[:]  # 이렇게 하니까 맞았다 처음엔 dp = [0] * n으로 함
    for i in range(n):
        std = nums[i]
        for j in range(i):
            if nums[j] < std:
                dp[i] = max(dp[i], dp[j] + nums[i])
    return max(dp)


print(solution(int(input()), list(map(int, input().split()))))