import sys
from collections import deque

sys.stdin = open('input.txt')


def slide(i, j, di, dj):
    cnt = 0  # 기울일 때 몇 칸을 이동한 건지
    while arr[i][j] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        cnt += 1
    return i, j, cnt, arr[i][j] == 'O'  # 구멍에서 멈춘 건지, 벽에서 멈춘 건지


def bfs(q):
    move = -1
    while q:
        move += 1
        for _ in range(len(q)):
            ri, rj, bi, bj = q.popleft()
            for di, dj in delta:
                nri, nrj, r_cnt, r_hole = slide(ri, rj, di, dj)
                nbi, nbj, b_cnt, b_hole = slide(ri, rj, di, dj)

                if b_hole: continue
                if r_hole: return  # 빨간 공이 구멍에 들어간 것

                if (nri, nrj) == (nbi, nbj):
                    if r_cnt > b_cnt:
                        nri, nrj = nri - di, nrj - dj
                    else:
                        nbi, nbj = nbi - di, nbj - dj
                if visited[nri][nrj][nbi][nbj]: continue
                visited[nri][nrj][nbi][nbj] = 1
                q.append((nri, nrj, nbi, nbj))
    return 0


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
red = blue = end = 0

for i in range(n):
    inp = list(map(str, input()))
    arr[i] = inp
    for j in range(m):
        if inp[j] == 'R':
            red = (i, j)
        elif inp[j] == 'B':
            blue = (i, j)
        elif inp[j] == 'O':
            end = (i, j)

# 초기 작업
q = deque()
ri, rj = red
visited = [[set() for _ in range(n)] for _ in range(n)]
visited[ri][rj].add(blue)
q.append((*red, *blue))
bfs(q)