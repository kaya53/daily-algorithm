import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]


# 함수명과 local 변수명이 같음 -> 다르게 바꾸자 ; 재귀함수의 경우는 이렇게 하면 재귀 호출이 안됨
# cnt 함수가 너무 길다
def cnt(color, i, j):
    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1)]:
        ci, cj = i, j
        ls = [(ci, cj)]
        # cnt = 1
        omok = 1
        for k in range(5):
            ni, nj = ci + di, cj + dj
            if (0 <= ni < 19) and (0 <= nj < 19):
                if board[ni][nj] != color:
                    break
                # else:  # break가 있으면 else를 굳이 쓰지 않아도 됨
                # cnt += 1
                omok += 1
                ci, cj = ni, nj
                ls.append((ci, cj))

        # if cnt == 5:
        if omok == 5:
            mmin = ls[0][1]
            res = (ls[0][0], ls[0][1])
            for i, j in ls:
                if j < mmin:
                    mmin = j
                    res = (i, j)
            # print(ls, res)

            fi, fj = ls[0][0]-di, ls[0][1]-dj
            bi, bj = ls[-1][0]+di, ls[-1][1]+dj
            try:
                if board[fi][fj] != color and board[bi][bj] != color:
                    return color, res
            except:  # 갔더니 인덱스 밖이면 5개가 맞다는 것
                return color, res


def solve(board):
    for i, elem in enumerate(board):
        if sum(elem) != 0:
            for j in range(19):
                if board[i][j] == 1:
                    sol = cnt(1, i, j)
                    if sol and sol[0] == 1:  # 오목 판별 함수; 인자- 1
                        return sol
                elif board[i][j] == 2:
                    sol = cnt(2, i, j)
                    if sol and sol[0] == 2:
                        return sol


res = solve(board)
# print(res)
if res == None:
    print(0)
else:
    print(res[0])
    print(res[1][0]+1, res[1][1]+1)