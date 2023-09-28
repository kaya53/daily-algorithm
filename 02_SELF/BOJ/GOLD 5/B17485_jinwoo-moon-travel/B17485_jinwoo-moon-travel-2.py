import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline


def dfs(ci, cj, prev):
    res = int(1e9)
    for k in range(3):
        if k == prev: continue
        ni, nj = ci + delta[k][0], cj + delta[k][1]
        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
        if memo[ni][nj][k]:
            res = min(res, memo[ni][nj][k]+arr[ci][cj])
        else:
            ret = dfs(ni, nj, k)
            res = min(res, ret+arr[ci][cj])

    # 여기로 빠져나왔다는 건 가장 끝 줄까지 왔거나,
    # ci, cj칸이 모두 메모되어서 dfs를 타지 않았다는 것
    if res == int(1e9):  # res가 갱신되지 않은 상태로 여기까지 오면 가장 첫 줄을 기록할 차례
        memo[ci][cj][prev] = arr[ci][cj]
    else:  # res가 갱신되었다면 그걸로 현재 값을 갱신해주면 됨
        memo[ci][cj][prev] = res

    return memo[ci][cj][prev]


delta = [(1, -1), (1, 0), (1, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]

for j in range(M):
    for d in range(3):
        nj = j + delta[d][1]
        dfs(0, j, d)

for m in memo:
    print(m)

