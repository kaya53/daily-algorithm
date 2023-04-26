import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs():
    q = deque()
    visited = set()
    q.append(N)
    visited.add(N)
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == K: return time
            for nnext in [now-1, now+1, now*2]:
                if nnext < 0 or nnext > 100000 or nnext in visited: continue
                q.append(nnext)
                visited.add(nnext)


N, K = map(int, input().split())
print(bfs())
