# 소요시간 1시간 반(풀이 참고)
# dp인데 기준을 어떻게 잡아야할 지 모르겠어서 헤맸다
# 다시 풀어보자
import sys

sys.stdin = open('input.txt')


def solution(n, nums):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):  # 0 ~ i-1번째까지 현재 값보다 작은 값이 있으면 max 비교하기
            if nums[i] > nums[j]:
                # 왜 현재 것을 max 비교에 넣는가
                # 그 전에 비교해서 갱신되었던 dp[i]가 최대일 수 있기 때문
                dp[i] = max(dp[i], dp[j]+1)  
    return max(dp)


print(solution(int(input()), list(map(int, input().split()))))