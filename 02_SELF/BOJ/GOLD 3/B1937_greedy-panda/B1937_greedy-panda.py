import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline


# ci, cj 위치에서 갈 수 있는 최대 칸
def dfs(ci, cj):
    res_max = 0
    for di, dj in delta:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ci][cj] >= arr[ni][nj]: continue
        
        # 메모된 것이 있음
        # 메모된 것: ni, nj에서 갈 수 있는 최대 칸
        # 그 최대 칸 +1이 내가 갈 수 있는 칸
        if memo[ni][nj]: res_max = max(res_max, memo[ni][nj])
        
        # 메모된 것이 없음
        # dfs를 돌려서 최대 칸 수를 알아내야 함
        else:
            ret = dfs(ni, nj)
            res_max = max(res_max, ret)

    # 4방향 어디도 갈 수 없는 상태; 최대 칸 수 리턴할 차례
    memo[ci][cj] = res_max + 1
    return memo[ci][cj]


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[0] * N for _ in range(N)]

for si in range(N):
    for sj in range(N):
        dfs(si, sj)

mmax = 0
for i in range(N):
    for j in range(N):
        if mmax < memo[i][j]: mmax = memo[i][j]

print(mmax)