# 230604 pypy 6036ms => 20분 정도 소요
# 사전 순으로 출력하면 되므로 하나 나오면 무조건 리턴
import sys

input = sys.stdin.readline


def fill(idx):
    if idx == lenE:
        for a in arr:
            print(''.join(map(str, a)))
        return True

    for nnext in range(1, 10):
        ci, cj = empty[idx]
        if not check(ci, cj, nnext): continue
        arr[ci][cj] = nnext
        if fill(idx+1): return True
        arr[ci][cj] = 0
    return False


def check(ci, cj, num):
    box_i, box_j = ci - (ci % 3), cj - (cj % 3)
    row_i = ci
    col_j = cj

    # box 체크
    for i in range(box_i, box_i+3):
        for j in range(box_j, box_j+3):
            if arr[i][j] == num: return False
    # 행 체크
    for jj in range(9):
        if arr[row_i][jj] == num: return False
    # 열 체크
    for ii in range(9):
        if arr[ii][col_j] == num: return False
    return True


arr = []
empty = []
for n in range(9):
    inp = list(map(int, input().rstrip()))
    arr.append(inp)
    for m in range(9):
        if inp[m] == 0:
            empty.append((n, m))

lenE = len(empty)
choice = [0] * lenE
fill(0)