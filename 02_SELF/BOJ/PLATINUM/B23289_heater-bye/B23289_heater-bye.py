import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

# 해당 방향에 벽이 있는 지 체크
def check_wall(ti, tj, d, k):  # k: wall_check 내에서 몇 번째인지
    for chec in wall_check[d][k]:
        dti, dtj, dni, dnj = chec
        nti, ntj = ti + dti, tj + dtj
        nni, nnj = ti + dni, tj + dnj
        if (nti, ntj, nni, nnj) in walls or (nni, nnj, nti, ntj) in walls : return True
    return False


# 모든 온풍기에서 바람이 나옴
def wind_out(wind):  # 퍼진 바람
    for hi, hj, d in heater:  # 히터의 좌표, 방향
        hhi, hhj = hi+delta[d][0], hj+delta[d][1]
        if hhi < 0 or hhi >= n or hhj < 0 or hhj >= m: return
        wind[hhi][hhj] += 5
        target = [(hhi, hhj)]
        for size in range(4, 0, -1):
            tmp = []
            for ti, tj in target:
                for k in range(3):
                    di, dj = spread_d[d][k]
                    ni, nj = ti + di, tj + dj
                    if (ni < 0 or ni >= n or nj < 0 or nj >= m) or ((ni, nj) in tmp): continue
                    if check_wall(ti, tj, d, k): continue
                    wind[ni][nj] += size
                    tmp.append((ni, nj))
            target = tmp
    return wind


# 격자 내 온도가 조절됨; 동시에 조절됨, 중간에 벽이 있으면 또 온도 조절 안됨
def control_temp(wind):
    tmp = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not wind[i][j]: continue
            for kk in range(4):
                ni, nj = i + delta[kk][0], j + delta[kk][1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]: continue
                if check_wall(i, j, kk, 1): continue
                sp = abs(wind[i][j] - wind[ni][nj]) // 4
                if wind[i][j] > wind[ni][nj]:
                    tmp[ni][nj] += sp
                    tmp[i][j] -= sp
                elif wind[i][j] < wind[ni][nj]:
                    tmp[ni][nj] -= sp
                    tmp[i][j] += sp
            visited[i][j] = 1

    for iii in range(n):
        for jjj in range(m):
            wind[iii][jjj] += tmp[iii][jjj]
    return wind


# 모서리 행, 열의 온도가 1씩 감소; 온도가 0이상인 것만
def corner_down(wind):
    for e in edge:
        xs, xe = e[0]
        ys, ye = e[1]
        for i in range(xs, xe):
            for j in range(ys, ye):
                if wind[i][j] > 0:
                    wind[i][j] -= 1
    return wind


# watch 배열에 있는 칸의 온도가 k 이상인지 확인
def check_k(wind):
    for hi, hj in watch:
        if wind[hi][hj] < K: return False
    return True


delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 우 좌 상 하
spread_d = {
    0: [(-1, 1), (0, 1), (1, 1)],
    1: [(-1, -1), (0, -1), (1, -1)],
    2: [(-1, -1), (-1, 0), (-1, 1)],
    3: [(1, -1), (1, 0), (1, 1)]
}
wall_check = {
    0: [[(0, 0, -1, 0), (-1, 0, -1, 1)], [(0, 0, 0, 1)], [(0, 0, 1, 0), (1, 0, 1, 1)]],
    1: [[(0, 0, -1, 0), (-1, 0, -1, -1)], [(0, 0, 0, -1)], [(0, 0, 1, 0), (1, 0, 1, -1)]],
    2: [[(0, 0, 0, -1), (0, -1, -1, -1)], [(0, 0, -1, 0)], [(0, 0, 0, 1), (0, 1, -1, 1)]],
    3: [[(0, 0, 0, -1), (0, -1, 1, -1)], [(0, 0, 1, 0)], [(0, 0, 0, 1), (0, 1, 1, 1)]],
}
# for _ in range(9):
n, m, K = map(int, input().split())  # 행, 열, 기준 온도
edge = [[(0, 1), (0, m)], [(1, n-1), (0, 1)], [(1, n-1), (m-1, m)], [(n-1, n), (0, m)]]
# arr = [[] for _ in range(n)]
heater = []  # 온풍기가 있는 칸, 그 방향
watch = []  # 조사해야 하는 칸
for nn in range(n):
    inp = list(map(int, input().split()))
    # arr[nn] = inp
    for mm in range(m):
        if inp[mm] == 5: watch.append((nn, mm))
        elif inp[mm] > 0: heater.append((nn, mm, inp[mm]-1))

w = int(input())
walls = []  # 벽 정보
for _ in range(w):
    i, j, t = map(lambda x: x-1, map(int, input().split()))
    if t == -1:  # t: 0
        walls.append((i, j, i-1, j))
    elif t == 0:  # t: 1
        walls.append((i, j, i, j+1))

choco = 0
wind = [[0] * m for _ in range(n)]
while True:
    wind = wind_out(wind)
    wind = control_temp(wind)
    wind = corner_down(wind)
    choco += 1
    if choco > 100:
        choco = 101
        break
    if check_k(wind): break
# for w in wind:
#     print(w)
print(choco)