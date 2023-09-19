# 소요시간: 40분 pypy 352ms
# 이게 되네...?
# 그냥 백트래킹으로 가능한 경우 모두 담아 놓고 입력값이 그 안에 있는 지 없는 지 판별함
import sys

sys.stdin = open('input.txt')


def tictactoe(depth, ls):
    global res, cnt
    
    if depth == 9:  # 다 채워져서 끝난 경우
        if '.' not in ls:
            res.add(''.join(ls))
        return

    for i1, i2, i3 in std:  # 가로, 세로, 대각선이 맞는 경우
        if ls[i1] == ls[i2] == ls[i3] == 'X' or ls[i1] == ls[i2] == ls[i3] == 'O':
            res.add(''.join(ls))
            return

    for i in range(9):
        if ls[i] != '.': continue
        if depth % 2: ls[i] = 'O'
        else: ls[i] = 'X'
        tictactoe(depth+1, ls)
        ls[i] = '.'


std = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]
res = set()
tictactoe(0, ['.'] * 9)

while True:
    target = input()
    if target == 'end': break
    if target in res: print('valid')
    else: print('invalid')

