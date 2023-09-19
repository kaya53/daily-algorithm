# 소요시간 : 약 1시간 pypy 148ms
# 이진 탐색: 기준을 수열 길이에 놓고 함
# - 어디에 =을 넣고 빼냐에 따라 답이 달라지는 데 이 부분을 잘 모르겠음
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def func():
    left = 1
    right = N
    while left <= right:  # 여기에 = 넣고
        mid = (left + right) // 2
        tot = sum(nums[:mid])
        mmax = tot
        for i in range(N-mid):
            tot = tot - nums[i] + nums[i+mid]
            if mmax < tot: mmax = tot
        if mmax < S: left = mid + 1
        else: right = mid - 1
    return left  # 여기에 + 1 빼니까 맞았음


N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

res = func()
# print(res)
if res > N: print(0)
else: print(res)