import sys

sys.stdin = open('input.txt')

# for _ in range(2):
N = int(input())
balls = [() for _ in range(N)]
info = [[] for _ in range(N)]
for n in range(N):
    c, s = map(int, input().split())
    info[n] = [n, c, s]
info.sort(key=lambda x: x[2])






