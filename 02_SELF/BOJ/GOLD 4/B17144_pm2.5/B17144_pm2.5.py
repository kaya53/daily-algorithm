import sys

sys.stdin = open('input.txt')


def spread_pm():
    for i in range(r):
        for j in range(c):
            if arr[i][j][0] > 0:
                cnt = 0  # 확산된 개수
                spread = arr[i][j][0] // 5  # 주변으로 확산되는 양
                for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= r or nj < 0 or nj >= c or arr[ni][nj][0] == -1: continue
                    cnt += 1
                    arr[ni][nj][1] += spread  # 퍼질 예정만큼 담기
                arr[i][j][1] -= spread*cnt  # 날아갈 애들도 넣기
    # 확산 시키고 미먼 돌리기를 한 번에?
    for ii in range(r):
        for jj in range(c):
            if arr[ii][jj][0] or arr[ii][jj][1]:
                arr[ii][jj][0] += arr[ii][jj][1]
                arr[ii][jj][1] = 0


def purified_up(d, dir, std, ui, uj):
    while True:
        di, dj = dir[d]
        ni, nj = ui + di, uj + dj
        if ni < 0 or ni > std or nj < 0 or nj >= c:
            d += 1
            ni, nj = ui + dir[d][0], uj + dir[d][1]
        if arr[ni][nj][0] == -1:
            break
        arr[ui][uj][0] = arr[ni][nj][0]
        ui, uj = ni, nj
    arr[ui][uj][0] = 0


def purified_down(d, dir, std, li, lj):
    while True:
        di, dj = dir[d]
        ni, nj = li + di, lj + dj
        if ni < std or ni >= r or nj < 0 or nj >= c:
            d += 1
            ni, nj = li + dir[d][0], lj + dir[d][1]
        if arr[ni][nj][0] == -1:
            break
        arr[li][lj][0] = arr[ni][nj][0]
        li, lj = ni, nj
    arr[li][lj][0] = 0


# for _ in range(8):
r, c, t = map(int, input().split())
arr = [[[0, 0] for _ in range(c)] for _ in range(r)]

purifier = []
for y in range(r):
    inp = map(int, input().split())
    for x, elem in enumerate(inp):
        if elem:
            arr[y][x][0] = elem
            if elem == -1: purifier.append((y, x))

for _ in range(t):  # t초 동안 공청기 돌림
    # 1. 미먼 확산
    spread_pm()

    # 상-우-하-좌
    purified_up(0, [(-1, 0), (0, 1), (1, 0), (0, -1)], purifier[0][0], purifier[0][0] - 1, purifier[0][1])
    purified_down(0, [(1, 0), (0, 1), (-1, 0), (0, -1)], purifier[1][0], purifier[1][0] + 1, purifier[1][1])

ssum = 0
for elem in arr:
    for k in elem:
        if k[0] > 0: ssum += k[0]
print(ssum)