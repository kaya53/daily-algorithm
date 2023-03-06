import sys

sys.stdin = open('input.txt')

from collections import deque


N, K = map(int, input().split())
arr = deque(range(1, N+1))
res = [0] * N

i = idx = 0  # arr 순회, res의 인덱스

while arr:
    if len(arr) == 1:
        arr.append(arr.popleft())
    while i < K-1:
        out = arr.popleft()
        arr.append(out)
        i += 1
    if i == K-1:
        target = arr.popleft()
        res[idx] = target
        idx += 1
        i = 0

ans = ', '.join(map(str, res))
print(f'<{ans}>')