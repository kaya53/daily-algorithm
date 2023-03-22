import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

# for _ in range(5):
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# nums = arr[:]
sorted_nums = tuple(range(1, n+1))
idx = 0
res = -1
q = deque()
q.append((tuple(arr[:]), 0))
visited = set()
while q:
    nums, cnt = q.popleft()

    if nums == sorted_nums:
        res = cnt
        break

    for i in range(n-k+1):
        tmp = tuple(nums[:i] + nums[i:i+k][::-1] + nums[i+k:])
        if tmp not in visited:
            q.append((tmp, cnt+1))
            visited.add(tmp)

print(res)