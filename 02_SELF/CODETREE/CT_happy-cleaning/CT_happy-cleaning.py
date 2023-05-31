# 230531 python 525ms => 1시간 정도 소요
import sys

sys.stdin = open('input.txt')


def find_corner():
    cor = []
    d = 0
    i = j = N//2

    for l in range(1, N+1):
        for _ in range(2):
            cni, cnj = max(0, i+delta[d][0]*l), max(0, j+delta[d][1]*l)
            cor.append((cni, cnj))
            if (cni, cnj) == (0, 0): return set(cor)
            i, j = cni, cnj
            d = (d+1) % 4


def spread_dust(i, j, d):
    global res

    now_dust = arr[i][j]
    s_delta = spread_dir[d]
    # print(len(s_delta))
    total = 0
    for di, dj in s_delta.keys():
        ratio = s_delta[(di, dj)]
        sni, snj = i+di, j+dj
        if ratio == 'a':
            # print(now_dust, total)
            if sni < 0 or sni >= N or snj < 0 or snj >= N:
                res += now_dust - total
            else:
                arr[sni][snj] += now_dust - total
        else:
            total += int(now_dust * ratio)
            if sni < 0 or sni >= N or snj < 0 or snj >= N:
                res += int(now_dust*ratio)
            else:
                arr[sni][snj] += int(now_dust*ratio)
    arr[i][j] = 0


spread_dir = {
    0: {(-1, 1): 0.01, (1, 1): 0.01, (-2, 0): 0.02, (-1, 0): 0.07, (1, 0): 0.07, (2, 0): 0.02, (-1, -1): 0.1, (1, -1): 0.1, (0, -2): 0.05, (0, -1): 'a'},
    1: {
        (-1, -1): 0.01, (-1, 1): 0.01, (0, -2): 0.02, (0, -1): 0.07, (0, 1): 0.07, (0, 2): 0.02,
        (1, -1): 0.1, (1, 1): 0.1, (2, 0): 0.05, (1, 0): 'a'
    },
    2: {
        (-1, -1): 0.01, (1, -1): 0.01, (-2, 0): 0.02, (-1, 0): 0.07, (1, 0): 0.07, (2, 0): 0.02,
        (-1, 1): 0.1, (1, 1): 0.1, (0, 2): 0.05, (0, 1): 'a'
    },
    3 : {
        (1, -1): 0.01, (1, 1): 0.01, (0, -2): 0.02, (0, -1): 0.07, (0, 1): 0.07, (0, 2): 0.02,
        (-1, -1): 0.1, (-1, 1): 0.1, (-2, 0): 0.05, (-1, 0): 'a'
    }
}

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상
# for _ in range(3):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

corner = find_corner()
ci, cj, cd = N//2, N//2, 0

res = 0
while (ci, cj) != (0, 0):
    # 1. 1칸 이동
    ni, nj = ci + delta[cd][0], cj + delta[cd][1]
    # 2. 먼지 날리기
    spread_dust(ni, nj, cd)
    ##
    if (ni, nj) in corner: cd = (cd+1) % 4
    ci, cj = ni, nj
# for a in arr:
#     print(a)
print(res)

