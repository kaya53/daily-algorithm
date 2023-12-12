# 소요시간 의미 없음 python 148ms
# 구현
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# for _ in range(4):
H, W, X, Y = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(H+X)]
answer = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        answer[i][j] = board[i][j]

for ii in range(X, H):
    for jj in range(Y, W):
        answer[ii][jj] = board[ii][jj] - answer[ii-X][jj-Y]

for a in answer:
    print(*a)