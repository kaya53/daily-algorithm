import sys

sys.stdin = open('input.txt')


def is_player(i, j):
    for other in range(M):
        if (i, j) == player_info[other][:2]: return True
    return False


def move(i, j, d):
    ni, nj = i + delta[d][0], j + delta[d][1]
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
        d = (d+2) % 4
        ni, nj = i + delta[d][0], j + delta[d][1]
    return ni, nj, d


def fight(me, enemy):
    me_power = player_info[me][3]
    enemy_power = player_info[enemy][3]
    me_tot = me_power + gun[me]
    enemy_tot = enemy_power + gun[enemy]

    if (me_tot > enemy_tot) or (me_tot == enemy_tot and me_power > enemy_power):
        print('win', me, 'lose', enemy)
        lose(enemy)
        win(me, me_tot-enemy_tot)
    else:
        print('win', enemy, 'lose', me)
        lose(me)
        win(enemy, enemy_tot - me_tot)


def lose(no):
    i, j, d = player_info[no][:3]
    if gun[no]:
        g_arr[i][j].append(gun[no])
        gun[no] = 0

    for _ in range(4):
        i, j = i + delta[d][0], j + delta[d][1]
        if 0 <= i < N and 0 <= j < N and not is_player(i, j): break
        d = (d+1)%4
    # print(i, j, d)
    player_info[no][:3] = i, j, d
    if g_arr[i][j]:
        g_arr[i][j].sort()
        gun[no] = g_arr[i][j].pop()


def win(no, sc):
    point[no] += sc
    i, j = player_info[no][:2]
    check_gun(no, i, j)


def check_gun(no, i, j):
    now_gun = gun[p_no]
    gun_ls = g_arr[i][j]
    if now_gun:
        gun_ls += [now_gun]
    gun_ls.sort()
    gun[no] = gun_ls.pop()
    g_arr[i][j] = gun_ls


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(1):
    N, M, K = map(int, input().split())
    g_arr = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        inp = list(map(int, input().split()))
        for c in range(N):
            if inp[c]: g_arr[r][c].append(inp[c])
    player_info = [[] for _ in range(M)]
    for m in range(M):
        x, y, d, s = map(int, input().split())
        player_info[m] = [x-1, y-1, d, s]

    gun = [0] * M
    point = [0] * M
    for _ in range(K):
        for p_no in range(M):
            ci, cj, cd = player_info[p_no][:3]
            # 1칸 이동
            ci, cj, cd = move(ci, cj, cd)
            player_info[p_no][:3] = ci, cj, cd

            # 이동한 칸에 플레이어가 있는 지 확인
            for other_no in range(M):
                if p_no == other_no: continue
                if (ci, cj) == (player_info[other_no][0], player_info[other_no][1]):
                    fight(p_no, other_no)
                    break
            else:  # 플레이어 없음
                if gun[p_no]:
                    check_gun(p_no, ci, cj)
                else:  # 총기 소지 안하고 있음
                    g_arr[ci][cj].sort()
                    gun[p_no] = g_arr[ci][cj].pop()
            print(player_info)
            print(gun)
            for g in g_arr:
                print(g)
            print()
        print(*point)
        print('--------------------------------')
