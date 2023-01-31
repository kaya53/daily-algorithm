import sys

sys.stdin = open('input.txt')


def str_to_int(elem):
    # print(ord('A'), ord('F')) # 65 70
    col = ord(elem[0]) - 65
    row = int(elem[1]) - 1
    return row, col


def not_knight(ci, cj, next_i, next_j):
    di = [-2, -1, -2, -1, 2, 1, 2, 1]
    dj = [1, 2, -1, -2, 1, 2, -1, -2]
    for k in range(8):
        ni, nj = ci+di[k], cj+dj[k]
        if (0 <= ni < 6) and (0 <= nj < 6):
            if arr[ni][nj] == arr[next_i][next_j]:  # 8방향 내에 있으면
                return True
    return False



input = sys.stdin.readline
for _ in range(5):
    arr = [input().rstrip() for _ in range(36)]
    chess = [[0]*6 for _ in range(6)]

    msg = 'Valid'
    for k in range(36):
        i, j = str_to_int(arr[k])
        ni, nj = str_to_int(arr[k+1])
        if chess[i][j] == 1:  # 이미 방문한 곳
            msg = 'Invalid'
            break
        if not_knight(i, j, ni, nj):
            msg = 'Invalid'
            break
        else:  # 방문하지 않았다면
            chess[i][j] = 1

    print(msg)
