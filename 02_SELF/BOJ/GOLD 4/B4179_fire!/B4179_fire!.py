import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(sti, stj):
    q = deque([(sti, stj)])
    visited = [[0] * M for _ in range(N)]
    visited[sti][stj] = 1

    time = 0
    while True:
        time += 1
        while fire:
            for _ in range(len(fire)):
                fi, fj = fire.popleft()
                for dfi, dfj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nfi, nfj = fi + dfi, fj + dfj
                    if nfi < 0 or nfi >= N or nfj < 0 or nfj >= M: continue
                    if arr[nfi][nfj] == '#' or arr[nfi][nfj] == 'F': continue
                    arr[nfi][nfj] = 'F'
                    fire.append((nfi, nfj))
            break

        while q:
            for _ in range(len(q)):
                ci, cj = q.popleft()
                if ci == 0 or ci == N-1 or cj == 0 or cj == M-1:
                    return time

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                    if arr[ni][nj] == '#' or arr[ni][nj] == 'F' or visited[ni][nj]: continue
                    visited[ni][nj] = 1
                    q.append((ni, nj))
            break

        if not q: return 'IMPOSSIBLE'


# for _ in range(2):
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
si, sj = -1, -1
fire = deque()
for nn in range(N):
    inp = list(input())
    arr[nn] = inp
    # print(inp)
    for mm in range(M):
        if inp[mm] == 'J': si, sj = nn, mm
        elif inp[mm] == 'F': fire.append((nn, mm))
print(bfs(si, sj))