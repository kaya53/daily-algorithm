# 소요시간: 15 ~ 20분 pypy 1684ms
# 2000일이 답인게 없는지 for문 최대를 2001까지로 해도 정답이긴 하다
import sys

sys.stdin = open('input.txt')

from collections import deque

def ff(si, sj, visited, arr, n, l, r):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    ls = [(si, sj)]
    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]: continue
            if l <= abs(arr[ci][cj] - arr[ni][nj]) <= r:
                q.append((ni, nj))
                ls.append((ni, nj))
                visited[ni][nj] = 1
    return visited, ls


def solution():
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for day in range(1, 2002):
        can_open = []
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j]: continue
                visited, ls = ff(i, j, visited, arr, n, l, r)
                if len(ls) > 1:
                    can_open.append(ls)
        if not can_open: return day - 1

        for union in can_open:
            cnt = len(union)
            tot = 0
            for ui, uj in union:
                tot += arr[ui][uj]
            new = tot // cnt
            for ui, uj in union:
                arr[ui][uj] = new

# for _ in range(5):
print(solution())