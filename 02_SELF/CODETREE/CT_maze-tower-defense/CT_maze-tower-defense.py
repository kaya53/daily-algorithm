# 230601 python 192ms => 1시간 30 ~ 2시간 소요
import sys

sys.stdin = open('input.txt')


def get_corners():
    cor = set()
    ci, cj = SI, SJ
    d = 2
    for k in range(1, N+1):
        for _ in range(2):
            ni, nj = max(0, ci+delta[d][0]*k), max(0, cj+delta[d][1]*k)
            cor.add((ni, nj))
            d = (d-1) % 4
            ci, cj = ni, nj
            if (ni, nj) == (0, 0): return cor


def attack(d, n_size):
    global score

    for k in range(1, n_size+1):
        ni, nj = SI + delta[d][0]*k, SJ + delta[d][1]*k
        if arr[ni][nj]:
            score += arr[ni][nj]
            arr[ni][nj] = 0

    ci, cj = SI, SJ
    num = []
    d = 2
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if (ni, nj) in corner: d = (d-1) % 4
        if arr[ni][nj]: num.append(arr[ni][nj])
        ci, cj = ni, nj
    return num


def pull(num):
    global arr
    new = [[0] * N for _ in range(N)]

    # 붙이기
    ci, cj = SI, SJ
    d = 2
    while (ci, cj) != (0, 0):
        if not num: break
        now = num.pop(0)
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if (ni, nj) in corner: d = (d - 1) % 4
        new[ni][nj] = now
        ci, cj = ni, nj

    arr = new


def hit():
    global arr, score

    ci, cj = SI, SJ
    d = 2
    num = []
    now = []
    flag = False
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if not now:
            now.append(arr[ni][nj])
        else:
            if now[0] == arr[ni][nj]:
                now.append(arr[ni][nj])
            else:
                if len(now) < 4: num += now
                elif len(now) >= 4:
                    score += now[0]*len(now)
                    # print(now[0], len(now))
                    flag = True
                now = [arr[ni][nj]]
        if (ni, nj) in corner: d = (d - 1) % 4
        ci, cj = ni, nj

    # 붙이기
    return flag, num


def redisplay():
    # new = [[0] * N for _ in range(N)]
    new_num = []
    ci, cj = SI, SJ
    d = 2
    now = 0
    now_cnt = 0
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if not now:
            now = arr[ni][nj]
            now_cnt += 1
        else:
            if now == arr[ni][nj]: now_cnt += 1
            else:
                new_num += [now_cnt, now]
                now = arr[ni][nj]
                now_cnt = 1
        if (ni, nj) in corner: d = (d - 1) % 4
        ci, cj = ni, nj

    pull(new_num)


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

SI, SJ = N//2, N//2
corner = get_corners()
score = 0
for _ in range(M):
    cd, size = map(int, input().split())
    line = attack(cd, size)
    pull(line)

    f, line2 = hit()
    pull(line2)
    while f:
        f, line2 = hit()
        pull(line2)
    redisplay()

print(score)