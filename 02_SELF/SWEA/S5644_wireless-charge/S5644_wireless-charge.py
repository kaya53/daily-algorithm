# S2644 무선 충전
# 279ms
import sys
from collections import deque
sys.stdin = open('input.txt')


def get_charge_dist(i, j, r, p):
    q = deque()
    q.append((i, j, 0))
    arr[i][j].append(p)
    visited = [[0] * 10 for _ in range(10)]
    visited[i][j] = 1
    while q:
        ci, cj, dist = q.popleft()
        if dist >= r: return
        for di, dj in delta[1:]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= 10 or nj < 0 or nj >= 10 or visited[ni][nj] == 1: continue
            q.append((ni, nj, dist+1))
            arr[ni][nj].append(p)
            visited[ni][nj] = 1


def charge(ai, aj, bi, bj):
    global res

    target_a = arr[ai][aj]
    target_b = arr[bi][bj]

    if not target_a and target_b:
        maxb = 0
        for bno in target_b:
            if maxb < charger[bno]:
                maxb = charger[bno]
        res += maxb
    elif target_a and not target_b:
        maxa = 0
        for ano in target_a:
            if maxa < charger[ano]:
                maxa = charger[ano]
        res += maxa
    elif target_a and target_b:
        max_tot = 0
        size_a, size_b = 0, 0
        for u1 in target_a:
            for u2 in target_b:
                if u1 == u2:
                    if max_tot < charger[u1]:
                        max_tot = charger[u1]
                        size_a = size_b = charger[u1] // 2
                else:
                    if max_tot < charger[u1] + charger[u2]:
                        max_tot = charger[u1] + charger[u2]
                        size_a = charger[u1]
                        size_b = charger[u2]
        res = res + size_a + size_b


delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    path_A = [0] + list(map(int, input().split()))
    path_B = [0] + list(map(int, input().split()))
    charger = []

    # 충전 거리 구하기
    # arr: 충전기 번호
    arr = [[[] for _ in range(10)] for _ in range(10)]
    for no in range(A):
        y, x, c, p = map(int, input().split())
        charger.append(p)
        get_charge_dist(x-1, y-1, c, no)

    res = 0
    asi, asj = aci, acj = 0, 0
    bsi, bsj = bci, bcj = 9, 9
    for time in range(M+1):
        aci, acj = aci + delta[path_A[time]][0], acj + delta[path_A[time]][1]
        bci, bcj = bci + delta[path_B[time]][0], bcj + delta[path_B[time]][1]

        charge(aci, acj, bci, bcj)
        # print('time', time)
        # print(aci, acj)
        # print(bci, bcj)
    # print(res_a, res_b, sep='\n')
    # print(sum(res_a) + sum(res_b))
    print(f'#{tc} {res}')