import sys

sys.stdin = open('input.txt')

from collections import deque


def rotate(lenS):
    # 이번 단계의 회전 결과를 담은 배열
    rotated = [[0]*lenA for _ in range(lenA)]

    for i in range(0, lenA, lenS):
        for j in range(0, lenA, lenS):
            for ki in range(lenS):
                for kj in range(lenS):
                    rotated[i+kj][j+lenS-ki-1] = arr[i+ki][j+kj]
    return rotated


def melting_ice(arr):
    melt_ls = []
    for i in range(lenA):
        for j in range(lenA):
            if not arr[i][j]: continue  # 원래 얼음이 없는 칸은 녹이는 작업을 해 줄 필요가 없음
            cnt = 0  # 각 칸의 인접 얼음을 세는 변수
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < lenA and 0 <= nj < lenA and arr[ni][nj]: cnt += 1
            if cnt < 3: melt_ls.append((i, j))

    # 한 번에 녹인다
    for mi, mj in melt_ls:
        arr[mi][mj] -= 1
    return arr


def bfs(arr, si, sj):
    q = deque()
    q.append((si, sj))
    arr[si][sj] = -1  # 방문 처리
    ccnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= lenA or nj < 0 or nj >= lenA or arr[ni][nj] == -1: continue
            if arr[ni][nj]:  # 인접 칸도 얼음이면
                q.append((ni, nj))
                arr[ni][nj] = -1
                ccnt += 1  # 얼음 개수 더하기
    return ccnt


# for _ in range(6):
n, q = map(int, input().split())  # 격자 크기의 지수, 마법 시전 횟수
arr = [list(map(int, input().split())) for _ in range(2**n)]
stages = list(map(int, input().split()))
lenA = 2**n

# 회전하기
for num in stages:
    if num == 0:  # 0이면 회전시킬 필요가 없으니까
        arr = melting_ice(arr)
        continue
    # 회전된 배열로 얼음의 양 구하기
    arr = melting_ice(rotate(2**num))

# 남아있는 얼음의 합 구하기
ssum = 0
for i in range(lenA):
    row_sum = 0
    for j in range(lenA):
        row_sum += arr[i][j]
    ssum += row_sum

mmax = 0
# 모두 회전한 후에 가장 큰 덩어리가 차지하는 칸의 개수 구하기
for si in range(lenA):
    for sj in range(lenA):
        if arr[si][sj]:
            ccnt = bfs(arr, si, sj)
            if mmax < ccnt:
                mmax = ccnt

print(ssum, mmax, sep='\n')