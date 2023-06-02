# 230602 python 105ms => 3시간 30분 소요
# 틀린 이유
# 1. dfs에서 방문한 곳을 또 갈 수 있다는 점을 간과함 => 못 가는 게 아니라 물고기가 없을 뿐임
# 2. dfs를 돌리기 전에 max_cnt 초기값을 0으로 해놓으면 안된다.
import sys
sys.stdin = open('input.txt')


def duplicate():
    copied = []
    for ci in range(4):
        for cj in range(4):
            line = arr[ci][cj][1]
            for cd in range(8):
                if line[cd]: copied.append((ci, cj, cd, line[cd]))
    # print(copied)
    return copied


def move_monster():
    new = [[[0, [0] * 8] for _ in range(4)] for _ in range(4)]
    for ci in range(4):
        for cj in range(4):
            line = arr[ci][cj][1]
            for cd in range(8):
                now = line[cd]
                if not now: continue
                # ni = nj = nd = -1
                for k in range(8):
                    nd = (cd + k) % 8
                    ni, nj = ci + delta[nd][0], cj + delta[nd][1]
                    # 이동 가능한 상황
                    if 0 <= ni < 4 and 0 <= nj < 4 and not corpse[ni][nj] and (ni, nj) != (pac_i, pac_j):
                        # 이동 처리
                        new[ni][nj][1][nd] += now
                        new[ni][nj][0] += now
                        new[ci][cj][1][cd] -= now
                        new[ci][cj][0] -= now
                        break
                # 이동 안함
    for ii in range(4):
        for jj in range(4):
            arr[ii][jj][0] += new[ii][jj][0]
            al = arr[ii][jj][1]
            nl = new[ii][jj][1]
            for z in range(8):
                al[z] += nl[z]


def dfs(idx, dir_ls, loc_ls, cnt, pi, pj):
    global max_cnt, will_next_pac

    if idx == 3:
        if max_cnt < cnt:
            max_cnt = cnt
            will_next_pac = dir_ls
        # elif max_cnt == cnt:
        #     will_next_pac.append(dir_ls)
        return

    for cd in range(4):
        ni, nj = pi + m_delta[cd][0], pj + m_delta[cd][1]
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4: continue
        # 여기서 방문한 곳을 또 갈 수 있는 데 또 방문한다면 물고기가 없다!! -> 이 부분 때문에 답이 안나왔었음
        if (ni, nj) not in loc_ls:
            dfs(idx+1, dir_ls+[cd], loc_ls+[(ni, nj)], cnt+arr[ni][nj][0], ni, nj)
        else:  # 방문한 적이 있다면 다시 가기만 하기
            dfs(idx+1, dir_ls+[cd], loc_ls, cnt, ni, nj)


def move_pacman(move_ls):
    global pac_i, pac_j
    ci, cj = pac_i, pac_j
    for k in move_ls:
        ni, nj = ci + m_delta[k][0], cj + m_delta[k][1]
        if arr[ni][nj][0]:  # 몬스터 먹기
            corpse[ni][nj] = 3  # 이번 턴 제외 2턴 간 유지되므로
            arr[ni][nj][0] = 0
            arr[ni][nj][1] = [0]*8
        ci, cj = ni, nj
    pac_i, pac_j = ci, cj


def remove():
    for ii in range(4):
        for jj in range(4):
            if corpse[ii][jj]: corpse[ii][jj] -= 1


def duplicate_over(duplicated):
    # i, j, 방향, 개수
    for ci, cj, cd, cnt in duplicated:
        arr[ci][cj][0] += cnt
        arr[ci][cj][1][cd] += cnt


m_delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
M, T = map(int, input().split())
pac_i, pac_j = map(lambda x: int(x)-1, input().split())
arr = [[[0, [0]*8] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    i, j, d = map(lambda x: int(x)-1, input().split())
    arr[i][j][1][d] += 1  # 어떤 방향에 몇 마리가 있는 지 체크
    arr[i][j][0] += 1  # 해당 격자의 몬스터 총 개수

corpse = [[0] * 4 for _ in range(4)]
for _ in range(T):
    will_duplicate = duplicate()
    move_monster()
    max_cnt = -1  # 이 부분 0으로 해놓아서 틀렸었음!
    will_next_pac = []
    dfs(0, [], [], 0, pac_i, pac_j)
    move_pacman(will_next_pac)
    # print(pac_i, pac_j)
    remove()
    duplicate_over(will_duplicate)

res = 0
for ei in range(4):
    # print(arr[ei])
    for ej in range(4):
        res += arr[ei][ej][0]
print(res)
