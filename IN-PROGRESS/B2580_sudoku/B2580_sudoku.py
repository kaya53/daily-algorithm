# 소요시간 20분 pypy 2976ms python 시초
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def check(num, arr, ci, cj):
    # i 체크
    for j in range(9):
        if arr[ci][j] == num: return False
    for i in range(9):
        if arr[i][cj] == num: return False
    si, sj = ((ci//3)*3, (cj//3)*3)
    for ni in range(si, si+3):
        for nj in range(sj, sj+3):
            if arr[ni][nj] == num: return False
    return True


def backtrack(n, depth, arr, empty):
    if depth == n:
        for a in arr:
            print(*a)
        print()
        return True

    ci, cj = empty[depth]
    for num in range(1, 10):
        if not check(num, arr, ci, cj): continue
        arr[ci][cj] = num
        if backtrack(n, depth+1, arr, empty): return True
        arr[ci][cj] = 0
    return False


def solution(arr):
    empty = []
    for i in range(9):
        for j in range(9):
            if not arr[i][j]: empty.append((i, j))

    backtrack(len(empty), 0, arr, empty)
    return


solution([list(map(int, input().split())) for _ in range(9)])
