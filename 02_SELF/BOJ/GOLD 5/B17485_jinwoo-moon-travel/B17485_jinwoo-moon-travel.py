import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


def dfs(ci, cj, d):
    res = int(1e9)
    for k in range(3):
        if k == d: continue  # 같은 방향 건너 뛰기
        ni, nj = ci + delta[k][0], cj + delta[k][1]
        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
        if memo[ni][nj][k]:
            res = min(res, memo[ni][nj][k] + arr[ci][cj])
        else:
            ret = dfs(ni, nj, k)
            res = min(res, ret + arr[ci][cj])

    if res == int(1e9): memo[ci][cj][d] = arr[ci][cj]
    else: memo[ci][cj][d] = res

    return memo[ci][cj][d]


delta = [(1, -1), (1, 0), (1, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]

for j in range(M):
    for di in range(3):
        dfs(0, j, di)
for m in memo:
    print(m)

mmin = int(1e9)
for m in memo[0]:
    for num in m:
        if num and mmin > num:
            mmin = num
print(mmin)