# 소요시간 20분 python 44ms
# 가능한 최대의 크기로 격자를 만들어 놓으면 쉽게 풀리는 문제이다
import sys

sys.stdin = open('input.txt')

def solution():
    n = int(input())
    orders = list(input())
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    arr = [['#']*101 for _ in range(101)]
    ci, cj = 50, 50
    cd = 2
    arr[ci][cj] = '.'

    minI, minJ = 50, 50
    maxI, maxJ = 50, 50
    for order in orders:
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if order == 'F':
            arr[ni][nj] = '.'
            ci, cj = ni, nj
            if minI > ci: minI = ci
            if minJ > cj: minJ = cj
            if maxI < ci: maxI = ci
            if maxJ < cj: maxJ = cj
        else:
            if order == 'R': cd = (cd+1) % 4
            else: cd = (cd-1)%4

    for ri in range(minI, maxI+1):
        for rj in range(minJ, maxJ+1):
            print(arr[ri][rj], end='')
        print()


solution()

