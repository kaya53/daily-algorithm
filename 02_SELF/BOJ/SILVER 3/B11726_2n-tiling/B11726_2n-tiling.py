# 소요시간 15분 python 40ms
# 피보나치같은 규칙이 있는 문제였음
import sys

sys.stdin = open('input.txt')


def solution(num):
    ls = [0] * num

    ls[0] = 1
    if num > 1: ls[1] = 2
    for i in range(2, num):
        ls[i] = ls[i-2] + ls[i-1]
    return ls[num-1]


for n in range(1, 1001):
    print(solution(n) % 10007)
