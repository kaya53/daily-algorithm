import sys, copy

sys.stdin = open('input.txt')

from collections import deque


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
    if idx == 5:
        board_n = copy.deepcopy(board)
        # 회전하기
        board_n = rotate(rotate_choice, board_n)

        # 판 순서 바꾸기
        for o1, o2, o3, o4, o5 in comb_ls:
            board_n[0], board_n[1], board_n[2], board_n[3], board_n[4] = \
                board_n[o1], board_n[o2], board_n[o3], board_n[o4], board_n[o5]

        # 입출구 순서(판 번호, 행, 열) 순
        # for se in order:
        bfs(board_n)
        return

    for k in range(4):
        rotate_choice[idx] = k
        rotate_comb(idx+1)
        rotate_choice[idx] = 0


def rotate(r_choice, board_n):
    for k in range(5):
        now_board = board_n[k]
        now_r = r_choice[k]
        if not now_r: continue # 회전 안함
        elif now_r == 1:  # 시계 90도
            board_n[k] = list(map(list, zip(*now_board[::-1])))
        elif now_r == 2: # 반시계 90도
            board_n[k] = list(map(list, zip(*now_board)))[::-1]
        else:  # 180도 회전
            tmp = list(map(list, zip(*now_board[::-1])))
            board_n[k] = list(map(list, zip(*tmp[::-1])))
    return board_n
        

def bfs(se, board_n):
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    start, si, sj, end, ei, ej = se
    q = deque([(start, si, sj)])
    visited[start][0][0] = 1

    while q:
        now_board, ci, cj = q.popleft()
        ## 여기부터 짜기 시작



order = [((0, 0, 0), (4, 4, 4)), ((0, 4, 0), (4, 0, 4)), ((0, 0, 4), (4, 4, 0)), ((0, 4, 4), (4, 0, 0))]
board = []
for _ in range(5):
    tmp = []
    for _ in range(5):
        inp = list(map(int, input().split()))
        tmp.append(inp)
    board.append(tmp)

# arr = list(map(list, zip(*board[0])))[::-1]  # 반시계 90도
# arr = list(map(list, zip(*board[0][::-1])))  # 시계 90도

# 판 순서 구하기
comb_ls = []
choice = [-1]*5
comb(0)
# print(len(comb_ls), comb_ls)

# 회전 순서 구하기
rotate_choice = [0]*5
rotate_comb(0)
