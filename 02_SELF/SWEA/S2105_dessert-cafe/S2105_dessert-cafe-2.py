import sys

sys.stdin = open('input.txt')


def dfs(ci, cj, d, cakes):
    global res

    if ci == i and cj == j and d == 3: # 시작점으로 돌아옴
        if res < len(cakes):
            res = len(cakes)
        return
    
    # 방향 안바꾸고 다음 턴으로
    ni, nj = ci + delta[d][0], cj + delta[d][1]
    if (0 <= ni < N and 0 <= nj < N) and arr[ni][nj] not in cakes:
        dfs(ni, nj, d, cakes+[arr[ni][nj]])
    # 방향 바꾸고 다음 턴으로
    if 0 <= d <= 2:
        ni, nj = ci + delta[d+1][0], cj + delta[d+1][1]
        if (0 <= ni < N and 0 <= nj < N) and arr[ni][nj] not in cakes:
            dfs(ni, nj, d+1, cakes+[arr[ni][nj]])


delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
T = int(input())
for tc in range(1, T+1):
    # if tc > 1: break
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = -1
    for i in range(N-2):
        for j in range(1, N-1):
            dfs(i, j, 0, [])

    print(f'#{tc} {res}')

