import sys
import copy

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 상하좌우 지금 점
di, dj = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]


def count_bomb():
    tmp = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                tmp.append((i, j))
    bombs.append(tmp)
    return bombs, board


def set_bomb():
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
    return


def fire_bomb(fire_list):
    for ci, cj in fire_list:
        for k in range(5):
            ni, nj = ci + di[k], cj + dj[k]
            if (0 <= ni < r) and (0 <= nj < c):
                if board[ni][nj] == 'O':
                    board[ni][nj] = '.'
    # 터뜨린 이후에 남은 폭탄을 bombs에 넣기
    count_bomb()
    return

# for i in range(4):
r, c, n = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]

# 설치된 폭탄을 담을 큐
bombs = []

# 초기화
tmp = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            tmp.append((i, j))
bombs.append(tmp)
# print(board, bombs)

time = 1
while time < n:
    time += 1
    if not time % 2:
        set_bomb()
    else:
        fire_list = bombs.pop(0)
        fire_bomb(fire_list)

for elem in board:
    print(''.join(map(str, elem)))
    # print('--------------')