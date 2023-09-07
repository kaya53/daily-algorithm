# 소요시간 30분 python 144ms pypy 160ms
#
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

# for _ in range(2):
N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
left = 0
right = N-1
mmin = 2000000001
n1 = 0
n2 = 0
while left < right:
    now = nums[left] + nums[right]
    if now == 0:
        mmin = 0
        n1, n2 = nums[left], nums[right]
        break
    if abs(mmin) > abs(now):
        mmin = now
        n1, n2 = nums[left], nums[right]

    if now < 0: left += 1
    else: right -= 1
print(n1, n2)
