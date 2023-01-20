import sys

sys.stdin = open('input.txt')

for _ in range(5):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    res = (N - 1) + N*(M - 1)
    print(res)