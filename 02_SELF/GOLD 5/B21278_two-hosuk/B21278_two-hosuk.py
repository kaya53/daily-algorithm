import sys

sys.stdin = open('input.txt')

v, e = map(int, input().split())
infos = [tuple(map(int, input().split())) for _ in range(e)]

choice = [0, 0]
candidates = []
def comb(si, cnt):
    if cnt == 2:
        candidates.append(tuple(choice))
        return
    for i in range(si, v+1):
        choice[cnt] = i
        comb(i+1, cnt+1)
        choice[cnt] = 0
comb(1, 0)


