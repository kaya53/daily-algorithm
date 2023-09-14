import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(s):
    q = deque([s])

    while q:
        now = q.popleft()

        for idx, nnext in enumerate(arr[now]):
            if not nnext or visited[idx]: continue
            q.append(idx)
            visited[idx] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for start in range(N):
    visited = [0] * N
    bfs(start)
    print(*visited)