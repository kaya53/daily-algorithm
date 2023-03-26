# 백트래킹
# def backtrack(idx, si, sj)
    # if 도착점 도달:
        # 점수의 최대값 갱신; 10번 다 돌았어도 이걸 먼저 써서 걸리기 때문에 아래에서 점수 최댓값 갱신 안해줘도 됨
        # return
    # if idx == 10: 10번 다 돌았으면
        # return
    # for i in range(4):
        # i번 말 내보내기
        # move(i, i번 말 현위치, dices[idx]) => 비트 연산자 써서 이동시킨 것 취소할 수 있나? 이동한 자리 1이면 ^ 써서 뒤로
        # backtrack(idx+1)
        # move(i, i번 말 현위치) 취소 => 아니야 토글링 말고 그냥 MOVE 자체를 안하면 되잖아
            # visited 처리하지 말고 그냥 말이 어디에 있는 지만 보기

# print(0^1, 1^1, 2^3, 3^3, 4^5, 5^5)  # 1 0 1 0 1 0

import sys

sys.stdin = open('input.txt')

dices = list(map(int, input().split()))

# 1차원 배열로 펴기
board_std = [i for i in range(0, 41, 2)]
board_10 = [13, 16, 19, 25]
board_20 = [22, 24, 25]
board_30 = [28, 27, 26, 25]
board_25 = [30, 35, 40]

def move(i, si):
    pass

# leftdown = [(0, -1), (-1, 1), (1, 0)]
# rightdown = [(1, 0), (1, 1), (0, 1)]  # 10-> 13으로 갈 수도 있기 때문에 순서 유의!; 안해도 되나?
# righttop = [(0, 1), (-1, 1), (-1, 0)]
# lefttop = [(-1, 0), (-1, -1), (0, -1)]  # 30 => 28로 갈 수도 있기 때문에 0, -1이 마지막으로 오게

# board = [
#     [0, 0, 0, -1, -2, 0, 0, 0, 0],
#     [0, 0, 4, 2, 40, 38, 36, 0, 0],
#     [0, 6, 0, 0, 35, 0, 0, 34, 0],
#     [8, 0, 0, 0, 30, 0, 0, 0, 32],
#     [10, 13, 16, 19, 25, 26, 27, 28, 30],
#     [12, 0, 0, 0, 24, 0, 0, 0, 28],
#     [0, 14, 0, 0, 22, 0, 0, 26, 0],
#     [0, 0, 16, 18, 20, 22, 24, 0, 0]
# ]
# si, sj = 0, 3
# ei, ej = 0, 4
#
# def move(si, sj, k):  # 현재 좌표, 몇 칸 움직이는 지
#     # delta 정하기
#     if board[si][sj] == 10:
#         delta = [(0, 1)]
#     elif board[si][sj] == 20:
#         delta = [(-1, 0)]
#     elif board[si][sj] == 30:
#         delta = [(0, -1)]
#
#     if 0 <= si < 4 and 0 <= sj < 4:
#         delta = leftdown
#     elif 4 <= si < 8 and 0 <= sj < 4:
#         delta = rightdown
#     elif 4<= si < 8 and 4 <= sj < 9:
#         delta = righttop
#     elif 0 <= si < 4 and 4 <= sj < 9:
#         delta = lefttop
#
    # 정한 delta를 가지고 움직이기

