import sys
from collections import deque

input = sys.stdin.readline


def slide(i, j, di, dj):
    cnt = 0 # 몇 번 이동했는 지 세는 변수
    while arr[i+di][j+dj] != '#' and arr[i][j] != 'O':
        cnt += 1
        i += di
        j += dj
    return i, j, cnt, arr[i][j] == 'O'


def bfs(q):
    global res_str
    move = 0
    while q:
        move += 1
        for _ in range(len(q)):
            ri, rj, bi, bj, path = q.popleft()
            if move > 10: return -1
            for d in range(4):
                di, dj = delta[d]
                nri, nrj, r_cnt, r_hole = slide(ri, rj, di, dj)
                nbi, nbj, b_cnt, b_hole = slide(bi, bj, di, dj)
                dd = 'U'
                if d == 1: dd = 'D'
                elif d == 2: dd = 'L'
                elif d == 3: dd = 'R'

                if b_hole: continue
                if r_hole:
                    res_str = ''.join(map(str, path+[dd]))
                    return move

                if (nri, nrj) == (nbi, nbj):
                    if r_cnt > b_cnt:
                        nri -= di
                        nrj -= dj
                    else:
                        nbi -= di
                        nbj -= dj

                if (nbi, nbj) in visited[nri][nrj]: continue
                visited[nri][nrj].add((nbi, nbj))
                q.append((nri, nrj, nbi, nbj, path+[dd]))
    return -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
arr = []
red = blue = 0
for i in range(n):
    inp = list(map(str, input()))
    arr.append(inp)
    for j in range(m):
        if inp[j] == 'R':
            red = (i, j)
        elif inp[j] == 'B':
            blue = (i, j)

visited = [[set() for _ in range(m)] for _ in range(n)]
ri, rj = red
visited[ri][rj].add(blue)
q = deque()
q.append((*red, *blue, []))
res_str = ''

ans = bfs(q)
print(ans)
if res_str: print(res_str)

