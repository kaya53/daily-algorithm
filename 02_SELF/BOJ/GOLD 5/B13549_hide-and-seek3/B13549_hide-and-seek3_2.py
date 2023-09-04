import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs():
    q = deque([(N, 0)])
    visited = [0] * 100001
    visited[N] = 1

    while q:
        curr, time = q.popleft()
        if curr == K or curr*2 == K: return time
        if curr <= 100000 and curr*2 != K:
            q.append((curr*2, time))

        for d in [-1, 1]:
            nnext = curr + d
            if nnext < 0 or nnext > 100000 or visited[nnext]: continue
            q.append((nnext, time + 1))
            visited[nnext] = 1


N, K = map(int, input().split())
print(bfs())

