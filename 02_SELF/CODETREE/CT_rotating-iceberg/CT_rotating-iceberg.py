# 230601 python 565ms => 2시간 30분 ~ 3시간 소요
# 격자 하나하나를 돌리는 게 아니라 격자를 4등분 해서 격자 채로 돌리는 것이다!!
# => q.rotate() 활용
import sys

sys.stdin = open('input.txt')

from collections import deque


def rotate(r):
    new = [[0] * L for _ in range(L)]
    size = 2**r
    half = size // 2
    # 돌릴 덩어리들 모으기
    for si in range(0, L, size):
        for sj in range(0, L, size):
            q = deque()
            for ki in range(si, si+size, half):
                for kj in range(sj, sj+size, half):
                    line = []
                    for zi in range(ki, ki+half):
                        for zj in range(kj, kj+half):
                            line.append(arr[zi][zj])
                    q.append(line)
            # 돌리기
            q.rotate(2)
            
            # 다시 붙이기
            l_idx = 0
            for nj in range(sj, sj+size, half):
                for ni in range(si, si+size, half):
                    e_idx = 0
                    for xi in range(ni, ni+half):
                        for xj in range(nj, nj+half):
                            new[xi][xj] = q[l_idx][e_idx]
                            e_idx += 1
                    l_idx += 1

    return new


def melting():
    will_melt = []
    for i in range(L):
        for j in range(L):
            if not arr[i][j]: continue  # 이 코드 안넣어서 테케 2,3 틀렸었음
            ice_cnt = 0
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= L or nj < 0 or nj >= L or not arr[ni][nj]: continue
                ice_cnt += 1
            if ice_cnt < 3: will_melt.append((i, j))
    for mi, mj in will_melt:
        arr[mi][mj] -= 1


def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1

    cnt = 1
    while q:
        ci, cj= q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= L or nj < 0 or nj >= L or visited[ni][nj] or not arr[ni][nj]: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1
    return cnt


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(3):
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
rotation = list(map(int, input().split()))

L = 2**N
for r in rotation:
    if r != 0:
        arr = rotate(r)
    melting()

visited = [[0] * L for _ in range(L)]
max_size = 0
for i in range(L):
    for j in range(L):
        if arr[i][j] and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))

# output
res = 0
for a in arr:
    res += sum(a)
print(res, max_size, sep='\n')
