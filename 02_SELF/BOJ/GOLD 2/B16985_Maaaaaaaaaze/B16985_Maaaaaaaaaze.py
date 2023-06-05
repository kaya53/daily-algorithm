# 230604 python 584ms => 3시간 ~ 3시간 30분 소요
# 하... 가지가지하는 임지민....
# 1. delta에서 윗 보드로 가는 경우를 고려하지 않아서 틀렸었다
# - 처음에 그리디적인 관점에서 윗보드로 가는게 무조건 불리하다고 생각해서 뺐었다.
# - 하지만 못가는 칸에 대해서 아래로 갔다가 다른 칸으로 가서 다시 위로 갔다가 하는게
#   가능한 유일한 경로일 경우를 간과한 것이다...!
# - 이렇게 delta 부분만 고쳐주니까 바로 통과함...ㅎ
# 2. 최소값이 12로 갱신된 경우 더 작아질 게 없어서 계속 리턴시켰더니 시간이 확 줄어듦
# 3. 보드가 돌아가므로 입구와 출구가 달라지는 경우는 고려할 필요가 없다 => 이걸 생각했어야지 ^^
import copy, sys

sys.stdin = open('input.txt')
from collections import deque

# input = sys.stdin.readline


def comb(idx):
    if idx == 5:
        comb_ls.append(list(choice))
        return
    for ni in range(5):
        if ni in choice: continue
        choice[idx] = ni
        comb(idx+1)
        choice[idx] = -1


def rotate_comb(idx):
    if min_dist == 12: return  # 이거 넣으니까 1/6로 줄어듦 (3000대 => 500대)
    if idx == 5:
        # 회전하기 => board가 3차원 배열이므로 딥카피 사용
        board_k = rotate(rotate_choice, copy.deepcopy(board))
        # 판 순서 바꾸기
        for o1, o2, o3, o4, o5 in comb_ls:
            bfs([board_k[o1], board_k[o2], board_k[o3], board_k[o4], board_k[o5]])
        return

    for k in range(4):
        rotate_choice[idx] = k
        rotate_comb(idx+1)
        rotate_choice[idx] = 0


def rotate(r_choice, board_r):
    for k in range(5):
        now_board = board_r[k]  # 돌릴 판
        now_r = r_choice[k]  # 돌릴 방향
        if now_r == 0: continue  # 회전 안함
        elif now_r == 1:  # 시계 90도
            board_r[k] = list(map(list, zip(*now_board[::-1])))
        elif now_r == 2: # 반시계 90도
            board_r[k] = list(map(list, zip(*now_board)))[::-1]
        else: # 180도 회전
            tmpr = list(map(list, zip(*now_board[::-1])))
            board_r[k] = list(map(list, zip(*tmpr[::-1])))
    return board_r
        

def bfs(board_c):
    global min_dist

    if not board_c[0][0][0] or not board_c[4][4][4]: return  # 입출구가 가능한 칸이 아니면 리턴

    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    dist = -1
    while q:
        dist += 1
        if dist >= min_dist: return
        for _ in range(len(q)):
            c_no, ci, cj = q.popleft()
            if (c_no, ci, cj) == (4, 4, 4):
                if min_dist > dist:
                    min_dist = dist
                return

            for dn, di, dj in delta:
                n_no, ni, nj = c_no + dn, ci + di, cj + dj
                if n_no < 0 or n_no > 4 or ni < 0 or ni > 4 or nj < 0 or nj > 4: continue
                if board_c[n_no][ni][nj] == 0 or visited[n_no][ni][nj]: continue

                q.append((n_no, ni, nj))
                visited[n_no][ni][nj] = 1


# 윗 보드로 가는 경우도 고려했어야지...!
delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0)]
# input
board = []
for _ in range(5):
    tmp = []
    for _ in range(5):
        inp = list(map(int, input().rstrip().split()))
        tmp.append(inp)
    board.append(tmp)

# 처리
min_dist = 126
# 판 순서 구하기
comb_ls = []
choice = [-1]*5
comb(0)
# print(len(comb_ls), comb_ls)

# 회전 순서 구하기
rotate_choice = [0]*5
rotate_comb(0)

# output
if min_dist == 126:
    print(-1)
else:
    print(min_dist)