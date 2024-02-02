def check(arr, ci, stone):
    # 가로줄 체크
    k = ci // 3
    k *= 3
    c1 = 0
    for z in range(3):
        if arr[k + z] == stone: c1 += 1
    if c1 == 3: return True

    # 세로줄 체크
    x = ci % 3
    c2 = 0
    for y in range(0, 7, 3):
        if arr[x + y] == stone: c2 += 1
    if c2 == 3: return True

    # 대각선 체크
    for diag in [[0, 4, 8], [2, 4, 6]]:
        c3 = 0
        if ci in diag:
            for i in diag:
                if arr[i] == stone: c3 += 1
        if c3 == 3: return True
    return False


def tictactoe(depth, arr, board, tot):
    if depth == tot:
        if ''.join(arr) == board:
            # print(arr)
            return True
        return False
    for i in range(9):
        if arr[i] != '.': continue
        if depth % 2:
            arr[i] = 'X'
        else:
            arr[i] = 'O'
        # depth == tot-1이면 이미 모든 돌을 놓은 상태 => 그래서 depth < tot-1로 해줘야 함
        if depth < tot - 1 and check(arr, i, arr[i]):
            arr[i] = '.'
            # 여기에 리턴을 하면 안됨 => 다음 i에 이번 돌을 놓을 수 있는 지 없는 지 확인할 수 없기 때문
            continue
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

    if tictactoe(0, ['.'] * 9, joined, tot) == 1: return 1
    # print(r)

    return 0
