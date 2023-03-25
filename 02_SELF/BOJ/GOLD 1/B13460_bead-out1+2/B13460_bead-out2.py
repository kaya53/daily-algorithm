import sys
from collections import deque

input = sys.stdin.readline

def slide(i, j, di, dj):
    cnt = 0  # 기울일 때 몇 칸을 이동한 건지
    # 다음 칸이 벽이면 이동하면 안됨
    # 다음 칸이 구멍이면 이동해서 그 좌표를 리턴해야 함
    while arr[i+di][j+dj] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        cnt += 1
    return i, j, cnt, arr[i][j] == 'O'  # 구멍에서 멈춘 건지, 벽에서 멈춘 건지


def bfs(q):
    move = 0
    while q:
        move += 1
        for _ in range(len(q)):
            ri, rj, bi, bj = q.popleft()
            if move > 10: return 0
            for di, dj in delta:
                nri, nrj, r_cnt, r_hole = slide(ri, rj, di, dj)
                nbi, nbj, b_cnt, b_hole = slide(bi, bj, di, dj)
                # print('red', di, dj, nri, nrj, r_cnt, r_hole)
                # print('blue', di, dj, nbi, nbj, b_cnt, b_hole)
                if b_hole: continue  # 파란 공이 구멍에 들어간 경우 -> 무시
                if r_hole: return 1  # 빨간 공이 구멍에 들어간 것

                if (nri, nrj) == (nbi, nbj):  # 같은 방향으로 기울어진 경우
                    if r_cnt > b_cnt:
                        nri, nrj = nri - di, nrj - dj
                    else:
                        nbi, nbj = nbi - di, nbj - dj
                if (nbi, nbj) in visited[nri][nrj]: continue
                visited[nri][nrj].add((nbi, nbj))
                q.append((nri, nrj, nbi, nbj))
    return 0


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
red = blue = 0

for i in range(n):
    inp = list(map(str, input()))
    arr[i] = inp
    for j in range(m):
        if inp[j] == 'R':
            red = (i, j)
        elif inp[j] == 'B':
            blue = (i, j)

# 초기 작업
q = deque()
ri, rj = red
visited = [[set() for _ in range(m)] for _ in range(n)]
visited[ri][rj].add(blue)

q.append((*red, *blue))
print(bfs(q))