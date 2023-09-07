import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs():
    q = deque([(bulbs, 0)])
    visited = set()
    visited.add(bulbs)

    while q:
        curr, cnt = q.popleft()
        if curr == res: return cnt
        for i in range(N):
            tmp = list(map(int, bulbs))
            for k in [i-1, i, i+1]:
                if k < 0 or k >= N: continue
                tmp[k] ^= 1

            if tuple(tmp) in visited: continue
            q.append((tmp, cnt+1))
            visited.add(tuple(tmp))
    return -1


N = int(input())
bulbs = input()
res = input()
