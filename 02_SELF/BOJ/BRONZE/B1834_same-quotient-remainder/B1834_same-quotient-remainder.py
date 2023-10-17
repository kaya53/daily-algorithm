# 소요시간 5분 python 232ms
import sys

sys.stdin = open('input.txt')


def solution(n):
    tot = 0
    for i in range(1, n):
        tot += (i*n)+i
    return tot


print(solution(int(input())))

