import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def move_player(no):
    ci, cj, d = players[no][:3]
    ni, nj = ci + delta[d][0], cj + delta[d][1]
    if ni < 0 or ni >= n or nj < 0 or nj >= n:
        d = (d+2)%4
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        players[no][2] = d
    return ni, nj


def check_player(mi, mj, no):
    for nnext in range(m):
        if no == nnext: continue
        if (players[nnext][0], players[nnext][1]) == (mi, mj):
            return nnext
    return -1


def lose_player(ci, cj, no):
    # 총을 내려 놓는다.
    if gun[no]:
        arr[ci][cj].append(gun[no])
        gun[no] = 0
    # 이동한다.
    d = players[no][2]
    ni, nj = ci + delta[d][0], cj + delta[d][1]
    # 격자가 있거나 플레이어가 있으면
    while (ni < 0 or ni >= n or nj < 0 or nj >= n) or check_player(ni, nj, no) != -1:
        d = (d + 1) % 4
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        players[no][2] = d
    players[no][0], players[no][1] = ni, nj
    if arr[ni][nj]:
        max_gun(ni, nj, arr[ni][nj], no)


def fight(enemy, now):
    enemy_po = players[enemy][3] + gun[enemy]
    now_po = players[now][3] + gun[now]
    ci, cj = players[now][:2]
    if enemy_po > now_po:  # 원래 이 칸에 있던 애가 이김
        point[enemy] += enemy_po - now_po
        # 진 애 먼저; 총을 바닥에 놔야 함
        lose_player(ci, cj, now)
        # 이긴 애
        max_gun(ci, cj, arr[ci][cj], enemy)  # 이긴 애
    elif enemy_po < now_po:
        point[now] += now_po - enemy_po
        lose_player(ci, cj, enemy)  # 진 애
        max_gun(ci, cj, arr[ci][cj], now)  # 이긴 애
    elif enemy_po == now_po:
        if players[enemy][3] > players[now][3]: # 원래 이 칸에 있던 애가 이김
            lose_player(ci, cj, now)  # 진 애
            max_gun(ci, cj, arr[ci][cj], enemy)  # 이긴 애
        else:  # 새로 들어온 애가 이김
            lose_player(ci, cj, enemy)  # 진 애
            max_gun(ci, cj, arr[ci][cj], now)  # 이긴 애


def max_gun(gi, gj, gun_std, no):
    if gun[no]: gun_std.append(gun[no])
    if not gun_std: return
    gun_std.sort()
    res = gun_std.pop()
    # 나머지 총은 격자에 두기
    arr[gi][gj] = gun_std
    gun[no] = res
    return


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for _ in range(3):
n, m, k = map(int, input().split())  # 격자, 플레이어 수, 라운드 수
arr = [[0]*n for _ in range(n)]  # 총의 정보
for ii in range(n):
    inp = list(map(int, input().split()))
    for jj in range(n):
        arr[ii][jj] = [inp[jj]]

players = [0] * m  # 여기서는 좌표, 방향만 바꾼다. 능력치는 가만 두기
for mm in range(m):
    i, j, d, s = map(int, input().split())
    players[mm] = [i-1, j-1, d, s]

gun = [0] * m  # 플레이어 별 현재 가지고 있는 총의 공격력
point = [0] * m  # 플레이어 별 포인트 획득

for _ in range(k):  # 총 k번 진행
    # 1. 한 명씩 순차적으로 이동
    for no in range(m):
        mi, mj = move_player(no)  # 위치, 방향
        players[no][0], players[no][1] = mi, mj
        # 이동한 칸에 플레이어가 있는 지, 총이 있는 지 파악하기
        enemy = check_player(mi, mj, no)
        if enemy != -1:
            fight(enemy, no)
        else:
            max_gun(mi, mj, arr[mi][mj], no)

print(*point)