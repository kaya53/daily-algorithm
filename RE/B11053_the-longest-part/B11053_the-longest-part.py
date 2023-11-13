# 소요시간 1시간 반(풀이 참고)
# dp인데 기준을 어떻게 잡아야할 지 모르겠어서 헤맸다
# 다시 풀어보자
import sys

sys.stdin = open('input.txt')


def solution(n, nums):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


print(solution(int(input()), list(map(int, input().split()))))