# 230602 python 795ms => 2시간 30분 ~ 3시간 소요
import sys

sys.stdin = open('input.txt')


def spread_wind():
    for ai, aj, ad in aircon:
        now = [[0] * N for _ in range(N)]

        si, sj = ai + delta[ad][0], aj + delta[ad][1]  # 한 칸 직진
        now[si][sj] = 5
        ls = [(si, sj)]
        size = 5
        while ls:
            size -= 1
            if size == 0: break
            for _ in range(len(ls)):
                ci, cj = ls.pop(0)
                for k in range(3):
                    di, dj = spread[ad][k]
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                    # 그 너머는 퍼지지 않으므로 ls에 넣어주지 않는다.
                    if is_wall(ci, cj, ni, nj, di, dj, ad, k): continue
                    now[ni][nj] = size
                    ls.append((ni, nj))
        for ii in range(N):
            for jj in range(N):
                wind_arr[ii][jj] += now[ii][jj]


def is_wall(ci, cj, ni, nj, di, dj, ad, k):
    if not ad % 2:  # 왼쪽, 오른쪽 방향
        if k == 1:  # 직진
            if ((ci, cj), (ni, nj)) in wall: return True
        else:  # 대각선
            # 대각선과 그 바로 위/아래
            if ((ci, cj), (ci+di, cj)) in wall or ((ci+di, cj), (ni, nj)) in wall: return True
        return False
    else:  # 위, 아래 방향
        if k == 1:  # 직진
            if ((ci, cj), (ni, nj)) in wall: return True
        else:
            # 대각선과 그 바로 위/아래
            if ((ci, cj), (ci, cj+dj)) in wall or ((ci, cj+dj), (ni, nj)) in wall: return True
        return False


def mix_air():
    will_mix = [[0] * N for _ in range(N)]
    # for wind in wind_arr:
    #     print(wind)
    # print()
    for ci in range(N):
        for cj in range(N):
            for k in range(4):
                di, dj = delta[k]
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if is_wall(ci, cj, ni, nj, di, dj, k, 1): continue
                diff = (wind_arr[ni][nj] - wind_arr[ci][cj]) // 4
                if diff > 0:
                    will_mix[ni][nj] -= diff
                    will_mix[ci][cj] += diff
    for wi in range(N):
        for wj in range(N):
            wind_arr[wi][wj] += will_mix[wi][wj]


def minus_wall():
    for ii in [0, N-1]:
        for jj in range(N):
            if not wind_arr[ii][jj]: continue
            wind_arr[ii][jj] -= 1

    for ii in range(1, N-1):
        for jj in [0, N-1]:
            if not wind_arr[ii][jj]: continue
            wind_arr[ii][jj] -= 1


def check():
    for oi, oj in office:
        if wind_arr[oi][oj] < K: return False
    return True


spread = {
    0: [(-1, -1), (0, -1), (1, -1)],
    1: [(-1, -1), (-1, 0), (-1, 1)],
    2: [(-1, 1), (0, 1), (1, 1)],
    3: [(1, -1), (1, 0), (1, 1)]
}
delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌상우하
N, M, K = map(int, input().split())
# arr = [[] for _ in range(N)]
office = []
aircon = []
for r in range(N):
    inp = list(map(int, input().split()))
    # arr[r] = inp
    for c in range(N):
        if inp[c] == 1: office.append((r, c))
        elif inp[c] > 1: aircon.append((r, c, inp[c]-2))  # 위치, 방향

wall = []
for _ in range(M):
    i, j, s = map(lambda x: int(x)-1, input().split())
    if s == -1: # 위칸
        wall.append(((i, j), (i-1, j)))
        wall.append(((i-1, j), (i, j)))
    else:  # 왼쪽
        wall.append(((i, j), (i, j-1)))
        wall.append(((i, j-1),(i, j)))

# print(office)
# print(aircon)
# print(wall)
wind_arr = [[0] * N for _ in range(N)]
for turn in range(1, 101):
    spread_wind()
    mix_air()
    minus_wall()
    if check():
        print(turn)
        break
    # for wi in wind_arr:
    #     print(wi)
    # break
else:
    print(-1)