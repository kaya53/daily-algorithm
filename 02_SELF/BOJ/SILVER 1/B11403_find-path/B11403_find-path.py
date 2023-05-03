import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(curr):
    q = deque()
    q.append(curr)
    while q:
        curr = q.popleft()
        for nnext in range(N):
            if not arr[curr][nnext] or visited[nnext]: continue
            q.append(nnext)
            visited[nnext] = 1


# for _ in range(2):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for node in range(N):
    visited = [0] * N
    bfs(node)
    print(*visited)