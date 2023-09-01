# 소요시간 15분 44ms
# 문제를 잘 읽고 분기를 잘 짜면 된다
import sys

sys.stdin = open('input.txt')


def get_order():
    board.append(score)
    sorted_board = sorted(board, reverse=True)
    return sorted_board.index(score)+1


# for _ in range(4):
N, score, P = map(int, input().split())
board = []  # 랭킹 리스트가 비어 있을 때
if N: board = list(map(int, input().split()))

if P == N:
    if min(board) < score: print(get_order())
    else: print(-1)
else: print(get_order())