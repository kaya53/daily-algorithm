# 230530 python 151ms => 1시간 30분 가량 소요
# 유의할 점
# 1. 바뀌는 부분을 갱신할 때 겹칠 수 있는 부분 유의; new_mono
# 2. 자료 구조 꼼꼼히 생각하고 문제 풀기 시작하기
# 3. 특정 시간이 지나면 사라지는 부분 짤 때 숫자를 어디 부터 시작할 지
import sys

sys.stdin = open('input.txt')


def minus_monopoly():
    for i in range(N):
        for j in range(N):
            if monopoly[i][j] and monopoly[i][j][1] > 0:
                monopoly[i][j][1] -= 1
                # 독점 계약 만료
                if monopoly[i][j][1] == 0: monopoly[i][j] = 0


def move_player():
    global remain
    new_mono = [0] * (M+1)  # 나중에 모노폴리 배열을 바꾸기 위한 배열
    new = [[0] * N for _ in range(N)]
    for p_no in range(1, M+1):
        if not players[p_no]: continue
        pi, pj, pd = players[p_no]
        nnext = (-1, -1, -1)
        for nd in players_order[p_no][pd]:
            ni, nj = pi + delta[nd][0], pj + delta[nd][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if monopoly[ni][nj] == 0:
                nnext = ni, nj, nd
                break
            elif nnext == (-1, -1, -1) and monopoly[ni][nj][0] == p_no:
                nnext = (ni, nj, nd)
        next_i, next_j, next_d = nnext
        # print(p_no, nnext)
        if new[next_i][next_j]:  # 이미 다른 플레이어가 들어와 있는 상황
            other_no = new[next_i][next_j]
            remain -= 1
            if other_no > p_no:  # 기존에 있던 애가 사라짐
                players[other_no] = None
                new[next_i][next_j] = p_no
                players[p_no] = [next_i, next_j, next_d]
                # monopoly[next_i][next_j] = [p_no, K]
                new_mono[p_no] = (next_i, next_j)
                new_mono[other_no] = 0
            else:  # 현재 들어온 수가 사라짐
                players[p_no] = None
                new_mono[p_no] = 0
        else:  # 빈칸
            new[next_i][next_j] = p_no
            players[p_no] = [next_i, next_j, next_d]
            # monopoly[next_i][next_j] = [p_no, K]
            new_mono[p_no] = (next_i, next_j)
    for m in range(1, M+1):  # 각 플레이어의 독점 현황 배열(monopoly) 바꿔주기
        if not new_mono[m]: continue
        mi, mj = new_mono[m]
        monopoly[mi][mj] = [m, K+1]  # 새로 한 독점 계약 => 기존 것에 추가
    return new
        

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 순
# for _ in range(2):
N, M, K = map(int, input().split())
arr = [[] for _ in range(N)]

# 인덱스가 플레이어 번호, [플레이어 위치, 방향]
players = [[] for _ in range(M+1)]
players_order = [[[] for _ in range(4)] for _ in range(M+1)]
monopoly = [[0] * N for _ in range(N)]
for r in range(N):
    inp = list(map(int, input().split()))
    arr[r] = inp
    for c in range(N):
        if inp[c] > 0:
            players[inp[c]] = [r, c]
            monopoly[r][c] = [inp[c], K+1]

idx = 1
for dd in map(lambda x: int(x)-1, input().split()):
    players[idx].append(dd)
    idx += 1
# 우선 순위
for no in range(1, M+1):
    for dc in range(4):
        inp1 = list(map(lambda x: int(x)-1, input().split()))
        players_order[no][dc] = inp1

remain = M
for turn in range(1, 1001):
    # print(turn, '----------------')
    minus_monopoly()
    arr = move_player()

    if players[1] and remain == 1:
        print(turn)
        break
else:
    print(-1)