import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def slide(i, j, di, dj):
    cnt = 0
    while arr[i+di][j+dj] != '#' and arr[i][j] != 'O':
        cnt += 1
        i, j = i + di, j + dj
    return i, j, cnt, arr[i][j] == 'O'


def bfs(q):
    move = 0
    while q:
        move += 1
        for _ in range(len(q)):
            ri, rj, bi, bj = q.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nri, nrj, r_cnt, r_hole = slide(ri, rj, di, dj)
                nbi, nbj, b_cnt, b_hole = slide(bi, bj, di, dj)

                if b_hole: continue
                if r_hole: return move

                if (nri, nrj) == (nbi, nbj):
                    if r_cnt > b_cnt:
                        nri, nrj = nri - di, nrj - dj
                    else:
                        nbi, nbj = nbi - di, nbj - dj

                if (nbi, nbj) in visited[nri][nrj]: continue
                visited[nri][nrj].add((nbi, nbj))
                q.append((nri, nrj, nbi, nbj))
    return -1


#for _ in range(7):
n, m = map(int, input().split())
arr = []
red = blue = 0
for ii in range(n):
    inp = list(map(str, input()))
    arr.append(inp)
    for jj in range(m):
        if inp[jj] == 'R': red = (ii, jj)
        elif inp[jj] == 'B': blue = (ii, jj)

visited = [[set() for _ in range(m)] for _ in range(n)]
ri, rj = red
visited[ri][rj].add(blue)
q = deque()
q.append((*red, *blue))
print(bfs(q))