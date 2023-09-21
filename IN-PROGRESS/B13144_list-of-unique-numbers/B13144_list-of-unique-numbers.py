import sys

sys.stdin = open('input.txt')

from collections import defaultdict

# for _ in range(3):
N = int(input())
nums = list(map(int, input().split()))

left = right = 0
cnt_ls = [0] * 100001
res = 0
while left <= right < N:
    if not cnt_ls[nums[right]]:
        cnt_ls[nums[right]] = 1
        res += (right-left+1)
        right += 1
    else:
        cnt_ls[nums[left]] = 0  # 슬라이딩 윈도우처럼 사용하는 부분이 포인트였음
        left += 1


print(res)
