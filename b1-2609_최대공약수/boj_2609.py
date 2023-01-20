import sys

sys.stdin = open('input.txt')

for _ in range(4):
    N, M = map(int, input().split())
    n, m = N, M

    while m != 0:
        n %= m
        n, m = m, n
    print(n)
    print(N*M // n)