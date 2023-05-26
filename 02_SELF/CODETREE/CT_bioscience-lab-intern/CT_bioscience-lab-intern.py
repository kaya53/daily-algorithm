# 230525 python 268ms
# 유의할 점
# 1. 한 번에 여러 칸을 움직일 때 계산하는 방법
# 2. 움직인 후 처리 => 움직이기 전을 지우기가 애매하니까 새로운 배열에 넣고 하자
import sys

sys.stdin = open('input.txt')


def move_germ(ci, cj):
    # 크기, 움직일 거리, 방향 => 바뀔 수 있는 건 방향과 위치
    size, dist, d = arr[ci][cj]
    # ni, nj = -1, -1
    if d > 1:  # 좌, 우
        ni = ci
        nj = cj + dist*delta[d][1]
        k, z = divmod(nj, M-1)
        if k % 2 == 0: nj = z
        else:
            d ^= 1
            nj = M - 1 - z
    else:  # 상하
        ni = ci + dist*delta[d][0]
        nj = cj
        k, z = divmod(ni, N-1)
        if k % 2 == 0: ni = z
        else:
            d ^= 1
            ni = N - 1 - z

    # 현재 사이즈가 더 큰 경우에만 들어감
    if not new_arr[ni][nj] or new_arr[ni][nj][0] < size:
        new_arr[ni][nj] = [size, dist, d]


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상하우좌
# for _ in range(4):
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    i, j, s, d, b = map(int, input().split())
    arr[i-1][j-1] = [b, s, d-1]  # 크기, 움직이는 거리, 이동 방향

res = 0
for j in range(M):  # 승용이가 한 칸씩 이동
    # 곰팡이 채취
    for i in range(N):
        if arr[i][j]:
            res += arr[i][j][0]
            arr[i][j] = 0
            break
    # 곰팡이 이동
    new_arr = [[0] * M for _ in range(N)]
    for mi in range(N):
        for mj in range(M):
            if arr[mi][mj]:  move_germ(mi, mj)
    arr = new_arr

print(res)