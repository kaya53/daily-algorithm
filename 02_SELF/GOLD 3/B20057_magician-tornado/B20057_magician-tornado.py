import sys

sys.stdin = open('input.txt')

import math


def sand_tornado(arr, mi, mj, k):  # 대상 배열, 토네이도의 이동한 위치
    global res

    now = arr[mi][mj]
    spreaded = 0
    ai, aj = -1, -1  # 알파자리
    for dkey in sand_dir[k].keys():
        di, dj = dkey
        ni, nj = mi + di, mj + dj
        ai, aj = ni, nj
        # 인덱스 밖으로 나가면 결과에 더해주기
        val = math.trunc(sand_dir[k][dkey]*now)
        spreaded += val
        if ni < 0 or ni >= n or nj < 0 or nj >= n:
            res += val
        else:
            arr[ni][nj] += val
    # 알파 자리
    if ai < 0 or ai >= n or aj < 0 or aj >= n:
        res += now - spreaded
    else:
        arr[ai][aj] += now - spreaded
    arr[mi][mj] = 0  # 이동 완료


sand_dir = [
    {(-2, 0): 0.02, (-1, -1): 0.1, (-1, 0): 0.07, (-1, 1): 0.01, (0, -2): 0.05, (1, -1): 0.1, (1, 0): 0.07, (1, 1): 0.01, (2, 0): 0.02, (0, -1): 0},
    {(-1, -1): 0.01, (-1, 1): 0.01, (0, -2): 0.02, (0, -1): 0.07, (0, 1): 0.07, (0, 2): 0.02, (1, -1): 0.1, (1, 1): 0.1, (2, 0): 0.05, (1, 0): 0},
    {(-2, 0): 0.02, (-1, -1): 0.01, (-1, 0): 0.07, (-1, 1): 0.1, (0, 2): 0.05, (1, -1): 0.01, (1, 0): 0.07, (1, 1): 0.1, (2, 0): 0.02, (0, 1): 0},
    {(-2, 0): 0.05, (-1, -1): 0.1, (-1, 1): 0.1, (0, -2): 0.02, (0, -1): 0.07, (0,1): 0.07, (0, 2): 0.02, (1, -1): 0.01, (1, 1): 0.01, (-1, 0): 0}
]
# for _ in range(6):
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

dist = []  # 토네이도 이동 거리
for x in range(1, n):
    for _ in range(2):
        dist.append(x)
dist += [n-1]

ti, tj = n//2, n//2
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상
k = -1  # 초기 방향
for d in dist:  # 이번 턴에 이동하는 칸
    k = (k+1) % 4  # 턴 이동할 때 마다 방향 바꿔주기
    for _ in range(d):
        # 1. 토네이도가 이동한다.
        ni, nj = ti + dir[k][0], tj + dir[k][1]
        ti, tj = ni, nj
        # print(ni, nj)
        # 2. 한 칸 이동하면 이동한 것에 맞게 모래가 흩날린다. -- 함수로 빼기
        # ti, tj, 토네이도의 이동한 위치
        # 날릴 모래가 있으면 돌리기
        if arr[ti][tj]:
            sand_tornado(arr, ti, tj, k)
# for elem in arr:
#     print(elem)
print(res)