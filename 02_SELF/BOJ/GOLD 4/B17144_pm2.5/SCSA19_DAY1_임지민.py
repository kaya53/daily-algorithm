# for _ in range(1):
import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

# 미세먼지 확산; 동시에 확산함
def spread_pm():
    pm = [[0] * m for _ in range(n)]  # 동시에 퍼지니까 담아두기
    for i in range(n):
        for j in range(m):
            if arr[i][j] < 5: continue
            cnt = 0
            sp = 0
            for di, dj in delta:
                ni, nj = i + di, j + dj
                # 인덱스 밖, 공청기 -> 확산 안함
                if ni < 0 or ni >= n or nj < 0 or nj >= m or arr[ni][nj] == -1: continue
                sp = arr[i][j] // 5  # 확산되는 양
                cnt += 1
                pm[ni][nj] += sp
            arr[i][j] -= sp*cnt
    for i in range(n):
        for j in range(m):
            arr[i][j] += pm[i][j]
    return arr


# 공청기 윗부분 작동
def purifier_up(arr):  # 위 오른 아래 왼 순서; 0 1 2 3
    si, sj = purifier[0][0] - 1, 0
    ci, cj = si, sj
    d = 0
    while (ci, cj) != (si+1, sj+1):
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if ni < 0 or ni > si+1 or nj < 0 or nj >= m:
            d = (d+1) % 4
            ni, nj = ci + delta[d][0], cj + delta[d][1]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj
    arr[ci][cj] = 0


# 공청기 아랫부분 작동
def purifier_down(arr):  # 아래 오른 위 왼
    si, sj = purifier[1][0]+1, 0
    ci, cj = si, sj
    d = 2
    while (ci, cj) != (si-1, sj+1):
        ni, nj = ci+delta[d][0], cj + delta[d][1]
        if ni < si-1 or ni >= n or nj < 0 or nj >= m:
            d = (d-1) % 4
            ni, nj = ci + delta[d][0], cj + delta[d][1]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj
    arr[ci][cj] = 0



delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for _ in range(8):
n, m, t = map(int, input().split())
arr = [[] for _ in range(n)]
purifier = []
for nn in range(n):
    inp = list(map(int, input().split()))
    arr[nn] = inp
    for mm in range(m):
        if inp[mm] == -1: purifier.append((nn, mm))

for _ in range(t):
    arr = spread_pm()
    purifier_up(arr)
    purifier_down(arr)

res = 0
for a in arr:
    res += sum(a)
print(res+2)