import sys
from collections import deque

sys.stdin = open('input.txt')


def sliding(ri, rj, bi, bj, d):
    # d: 기우는 방향
    # 기울여서 끝점이 나오면 끝 but 빨간색만 들어가야 함
    if d == 0: 
        for c in range(1, m-2):  # 양 끝은 벽이니까
            if arr[ri][c] == '.': continue
            for cc in range(c+1, m-2):
                arr[ri][cc], arr[ri][cc+1] = arr[ri][cc+1], arr[ri][cc]
    elif d == 1:
        pass
    elif d == 2:
        pass
    elif d == 3:
        pass



def bfs(q):
    ri, rj = red
    bi, bj = blue
    ei, ej = end
    while q:
        now_d = q.popleft()
        # 기울이기
        sliding(ri, rj, bi, bj, now_d)


n, m = map(int, input().split())
arr = [[] for _ in range(n)]
red = blue = end = 0
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
for d in range(4):
    ni, nj = ri + delta[d][0], rj + delta[d][1]
    if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
    if arr[ni][nj] != '#':
        q.append(d)

bfs(q)
