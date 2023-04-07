import sys

input = sys.stdin.readline


def comb(idx, si, choice):
    if idx == N:
        print(*choice)
        return
    for i in range(1, N+1):
        if i in choice: continue
        comb(idx+1, si+1, choice+[i])


N = int(input())
comb(0, 1, [])