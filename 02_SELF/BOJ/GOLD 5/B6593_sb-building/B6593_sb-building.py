# python3 180ms 소요시간 30분
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(sk, si, sj, building, l, r, c):
    q = deque([(sk, si, sj, 0)])
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    visited[sk][si][sj] = 1

    while q:
        ck, ci, cj, time = q.popleft()

        if building[ck][ci][cj] == 'E':
            return f'Escaped in {time} minute(s).'

        for dk, di, dj in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]:
            nk, ni, nj = ck+dk, ci+di, cj+dj
            if nk < 0 or nk >= l or ni < 0 or ni >= r or nj < 0 or nj >= c: continue
            if building[nk][ni][nj] == '#' or visited[nk][ni][nj]: continue
            visited[nk][ni][nj] = 1
            q.append((nk, ni, nj, time+1))
    return 'Trapped!'


def solution(l,r,c, building):
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if building[k][i][j] == 'S':
                    return bfs(k, i, j, building, l, r, c)


while True:
    L,R,C = map(int, input().split())
    if not L and not R and not C: break
    # 3차원 arr[층][행][열]
    # 동서남북: 행, 열 변화
    # 상하: 층만 변화
    arr = []
    for _ in range(L):
        tmp = []
        for _ in range(R):
            tmp.append(list(input().rstrip()))
        arr.append(tmp)
        input()

    print(solution(L,R,C, arr))