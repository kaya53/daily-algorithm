# 메모리 초과 발생
import sys

sys.stdin = open('input.txt')


def solution(n):
    dp = [[[0] * n for _ in range(29)] for _ in range(29)]



deltas = [
    [(-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)],
    [(-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1)]
]
T = int(input())
for N in range(T):
    # N = int(input())
    solution(N)