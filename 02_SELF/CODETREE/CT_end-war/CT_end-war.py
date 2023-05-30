# 230530 python 1114ms => 1시간 반 소요
# 기울어진 직사각형을 만드는 dfs 코드!
import sys

sys.stdin = open('input.txt')


def dfs(ci, cj, d, choice):
    if d == 3 and (ci, cj) == (si, sj):
        get_size(choice)
        return

    ni, nj = ci + delta[d][0], cj + delta[d][1]
    if ni < 0 or ni >= N or nj < 0 or nj >= N: return  # 직사각형 성립 안됨
    dfs(ni, nj, d, choice+[(ni, nj)])
    if d < 3: dfs(ni, nj, d+1, choice+[(ni, nj)])


def get_size(choice):
    global res_min
    top = left = (N, N)
    right = bottom = (-1, -1)
    for ci, cj in choice:
        if ci < top[0]: top = (ci, cj)
        if cj < left[1]: left = (ci, cj)
        if ci > bottom[0]: bottom = (ci, cj)
        if cj > right[1]: right = (ci, cj)

    new = [[0]* N for _ in range(N)]
    one = two = three = four = five = 0
    # 2번
    for wi in range(left[0]):
        for wj in range(top[1]+1):
            if (wi, wj) in choice: break
            new[wi][wj] = 2
            two += arr[wi][wj]
    for ti in range(right[0] + 1):
        for tj in range(N-1, top[1], -1):
            if (ti, tj) in choice: break
            new[ti][tj] = 3
            three += arr[ti][tj]
    for foi in range(left[0], N):
        for foj in range(bottom[1]):
            if (foi, foj) in choice: break
            new[foi][foj] = 4
            four += arr[foi][foj]
    for fi in range(right[0]+1, N):
        for fj in range(N-1, bottom[1]-1, -1):
            if (fi, fj) in choice: break
            new[fi][fj] = 5
            five += arr[fi][fj]
    for i in range(N):
        for j in range(N):
            if new[i][j] == 0:
                one += arr[i][j]
    now_max = max(one, two, three, four, five)
    now_min = min(one, two, three, four, five)

    if res_min > now_max - now_min:
        res_min = now_max - now_min


delta = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
# for _ in range(3):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res_min = int(1e9)
for si in range(2, N):
    for sj in range(1, N-1):
        dfs(si, sj, 0, [])
print(res_min)