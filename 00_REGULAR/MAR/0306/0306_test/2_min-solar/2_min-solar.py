import sys

sys.stdin = open('input.txt')

choice = []
def backtrack(ssum, time, ci, cj):
    global min_res
    if ssum >= min_res: return
    if time > t: return
    if ci == ei and cj == ej:
        ssum += 2  # 도착점 포함 안하기
        if min_res > ssum:
            min_res = ssum
        return

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        # 인덱스 밖, 건물, 출발점을 만나면 건너뛰기
        if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 0 or arr[ni][nj] == -1: continue
        now = arr[ni][nj]
        arr[ni][nj] = 0
        backtrack(ssum + now, time+1, ni, nj)
        arr[ni][nj] = now


n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

si, sj, ei, ej = 0, 0, 0, 0
maxV = 0
for i in range(n):
    for j in range(n):
        maxV = max(maxV, arr[i][j])
        if arr[i][j] == -1:
            si, sj = i, j
        elif arr[i][j] == -2:
            ei, ej = i, j

min_res = int(1e9)
# ssum = 0
backtrack(0, 0, si, sj)

if min_res == int(1e9):
    print(-1)
else:
    print(min_res)


