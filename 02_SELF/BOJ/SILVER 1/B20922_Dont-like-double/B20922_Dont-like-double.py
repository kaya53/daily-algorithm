# 소요시간 30분 python 300ms
# 투 포인터 사용
import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())
nums = list(map(int, input().split()))

cnt_ls = [0] * (max(nums)+1)
left = right = 0

res = 0
while right < len(nums):
    # print(right)
    if cnt_ls[nums[right]] < K:
        cnt_ls[nums[right]] += 1
        right += 1
        # print(right)
    else:
        cnt_ls[nums[left]] -= 1
        left += 1
    if res < right-left:
        res = right - left
print(res)