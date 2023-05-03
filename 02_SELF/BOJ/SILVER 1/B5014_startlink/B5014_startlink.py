import sys

sys.stdin = open('input.txt')

from collections import deque

# for _ in range(2):
F, S, G, U, D = map(int, input().split())

q = deque()
q.append(S)
visited = set()
visited.add(S)

btn = -1
res = 'use the stairs'
while q:
    btn += 1
    for _ in range(len(q)):
        now = q.popleft()
        if now == G:
            res = btn
            break
        for nnext in [now+U, now-D]:
            if nnext < 1 or nnext > F or nnext in visited: continue
            q.append(nnext)
            visited.add(nnext)
print(res)