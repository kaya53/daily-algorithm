# 소요시간: 의미 없음 python 56ms
# 수학적으로 접근해야 하는 문제
import sys

sys.stdin = open('input.txt')

def solution():
    n = int(input())
    pigs = sum(list(map(int, input().split())))
    day = 1
    while n >= pigs:
        day += 1
        pigs *= 4
    return day


T = int(input())
for _ in range(T):
    print(solution())