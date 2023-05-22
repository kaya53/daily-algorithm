# 230522 python 52ms - 1시간 30분 정도 소요
# padding을 둘렀을 때 행, 열 인덱스 주의
# 정보가 갱신될 때 바뀌어야 하는 것들 꼼꼼히 체크해서 다 바꿔주기

import sys

sys.stdin = open('input.txt')


def move(no, ci, cj, cd):
    h_idx = horse_arr[ci][cj].index(no)
    moving = horse_arr[ci][cj][h_idx:]  # 움직일 말
    horse_arr[ci][cj] = horse_arr[ci][cj][:h_idx]

    # 움직이려는 칸
    ni, nj = ci + delta[cd][0], cj + delta[cd][1]
    if not arr[ni][nj]:
        if white_and_red(moving, ni, nj) is True: return True
    elif arr[ni][nj] == 1:
        if white_and_red(moving[::-1], ni, nj) is True: return True
    elif arr[ni][nj] == 2:
        # 방향 바꾸기
        nd = cd ^ 1
        infoes[no][-1] = nd
        ni, nj = ci + delta[nd][0], cj + delta[nd][1]
        res = blue(moving, ni, nj)
        if res is True: return True
        elif res is False:
            horse_arr[ci][cj] += moving


def white_and_red(moving, ni, nj):
    horse_arr[ni][nj] += moving
    for m_no in moving:
        infoes[m_no][0], infoes[m_no][1] = ni, nj
    if len(horse_arr[ni][nj]) >= 4: return True


def blue(moving, ni, nj):
    if not arr[ni][nj]:
        if white_and_red(moving, ni, nj) is True: return True
    elif arr[ni][nj] == 1:
        if white_and_red(moving[::-1], ni, nj) is True: return True
    # 파랑이면 움직이지 않음; 말 원래 자리에 놓기
    elif arr[ni][nj] == 2: return False


def solve():
    for turn in range(1, 1001):
        # 한 턴 => 말 차례로 움직이기
        for idx in range(1, K+1):
            i, j, d = infoes[idx]
            if move(idx, i, j, d) is True:
                print(turn)
                return
    else:
        print(-1)


delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# for _ in range(5):
N, K = map(int, input().split())
blues = [[2]*(N+2)]
arr = blues + [[2]+list(map(int, input().split()))+[2] for _ in range(N)] + blues
infoes = [[] for _ in range(K+1)]
horse_arr = [[[] for _ in range(N+2)] for _ in range(N+2)]

for k in range(1, K+1):
    si, sj, sd = map(int, input().split())
    infoes[k] = [si, sj, sd-1]
    horse_arr[si][sj].append(k)

solve()
