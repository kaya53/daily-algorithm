def check(arr, ci, stone):
    k = ci // 3
    for z in range(3):
        arr[k + z] != stone
        return False
    for diag in [[0, 4, 7], [2, 4, 6]]:
        if ci in diag:
            if arr[ci] != stone: return False
    return True


def tictactoe(depth, arr, board, tot):
    if depth == tot:
        if ''.join(arr) == board: return True
        return False
    for i in range(9):
        if arr[i] != '.': continue

        if depth % 2: arr[i] = 'X'
        else: arr[i] = 'O'
        if check(arr, i, arr[i]): return False
        if tictactoe(depth + 1, arr, board, tot): return True
        arr[i] = '.'
    return False


def solution(board):
    tot = 0
    joined = ""
    for i in range(3):
        joined += board[i]
        for j in range(3):
            if board[i][j] != '.': tot += 1

    if tictactoe(0, ['.'] * 9, joined, tot): return 1

    return 0
