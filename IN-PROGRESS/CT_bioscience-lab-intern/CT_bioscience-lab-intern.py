import sys

sys.stdin = open('input.txt')


def move_germ():
    pass


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상하우좌
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
    for mi in range(N):
        for mj in range(M):
            if arr[mi][mj]: move_germ()