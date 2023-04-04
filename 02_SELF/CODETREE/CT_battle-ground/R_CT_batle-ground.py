# 2023. 4. 4. 화
# 181ms

import sys

sys.stdin = open('input.txt')


def check_player(ci, cj, now_no):
    # 해당 자리에 플레이어가 있는 지 체크
    # ci, cj = player[now_no][:2]
    for other_no in range(M):
        if now_no == other_no: continue
        if player[other_no][:2] == [ci, cj]: return other_no
    return False


# 자신의 방향대로 1칸씩 이동 => 이동 칸의 플레이어 유무 리턴
def move(now_no):
    ci, cj, cd = player[now_no][:3]
    ni, nj = ci + delta[cd][0], cj + delta[cd][1]
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
        cd = (cd + 2) % 4
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
    player[now_no][:3] = [ni, nj, cd]
    # print(player[now_no])
    # 이동한 자리의 플레이어 유무
    return ni, nj, check_player(ni, nj, now_no)


# 플레이어를 만나면 싸우기
def fight(now_no, other_no):  # 지금 보고 있는 플레이어, 그 자리에 있던 플레이어
    # print(now_no, other_no)
    now_initial = player[now_no][-1]
    other_initial = player[other_no][-1]
    now_score = now_initial + players_gun[now_no]
    other_score = other_initial + players_gun[other_no]
    val = now_score - other_score
    # print(val)
    if val > 0 or (not val and now_initial > other_initial):
        lose_player(other_no)  # 틀린 이유 1. : 내려놓는 걸 먼저 해야하므로 진 플레이어에 대한 함수를 먼저 실행해야 함
        win_player(now_no, val)
    elif val < 0 or (not val and now_initial < other_initial):
        lose_player(now_no)
        win_player(other_no, abs(val))


# 이긴 플레이어에 대해
def win_player(p_no, val):
    points[p_no] += val
    # print(p_no, val)
    check_gun(player[p_no][0], player[p_no][1], p_no)


# 진 플레이어에 대해
def lose_player(p_no):
    # 총 내려 놓기
    p_gun = players_gun[p_no]
    players_gun[p_no] = 0  # 틀린 이유 2: 내려놓으면 이 부분을 갱신해줘야 하는 데 안함
    ci, cj, cd = player[p_no][:3]
    if p_gun: arr[ci][cj].append(p_gun)
    
    # 한 칸 이동
    ni, nj = ci + delta[cd][0], cj + delta[cd][1]

    if (ni < 0 or ni >= N or nj < 0 or nj >= N) or check_player(ni, nj, p_no) is not False:
        for _ in range(4):
            cd = (cd + 1) % 4
            player[p_no][2] = cd
            ni, nj = ci + delta[cd][0], cj + delta[cd][1]
            if 0 <= ni < N and 0 <= nj < N and check_player(ni, nj, p_no) is False:
                break
    player[p_no][:2] = [ni, nj]
    # 격자 안이면서 플레이어 없는 곳: ni, nj
    check_gun(player[p_no][0], player[p_no][1], p_no)


# 내 총과 격자 총들 중 센 것 가져오기
def check_gun(ci, cj, p_no):
    gun_on_arr = arr[ci][cj]
    p_gun = players_gun[p_no]
    if p_gun:  # 플레이어가 총을 가지고 있으면 
        gun_on_arr.append(p_gun)
    if not gun_on_arr: return # 플레이어 총이든 격자 총이든 하나라도 있으면
    gun_on_arr.sort()
    players_gun[p_no] = gun_on_arr.pop()  # 가장 큰 값을 넣어주기


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 - 오른 - 아래 - 왼
# input
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
player = [[] for _ in range(M)]
players_gun = [0] * M
points = [0] * M
for nn in range(N):
    inp = list(map(int, input().split()))
    for nnn in range(N):
        if inp[nnn]: arr[nn][nnn].append(inp[nnn])
        # 총이 없으면(0): 넣지 않기

for mm in range(M):
    x, y, d, s = map(int, input().split())
    player[mm] = [x-1, y-1, d, s]


# main
for _ in range(K):  # k라운드 진행
    # print(_, '--------------------')
    for player_no in range(M):  # 1번부터 차례대로 진행
        # print('move', player_no+1)
        now_pi, now_pj, other_pno = move(player_no)
        # print(now_pi, now_pj, other_pno)
        if other_pno is False:
            check_gun(now_pi, now_pj, player_no)
        else:
            fight(player_no, other_pno)

        # print(player)
        # print(players_gun)
        # for a in arr:
        #     print(a)
        # print()
print(*points)