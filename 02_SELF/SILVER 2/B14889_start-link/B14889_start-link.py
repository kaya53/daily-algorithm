import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def calc(start, link):
    global mmin

    s_cnt = 0
    for i in start:
        for j in start:
            if i == j: continue
            s_cnt += stat[i-1][j-1]
            # print(i, j)
    l_cnt = 0
    for ii in link:
        for jj in link:
            if ii == jj: continue
            l_cnt += stat[ii-1][jj-1]

    diff = abs(s_cnt - l_cnt)
    if mmin > diff:
        mmin = diff


def comb(idx, si):
    if mmin == 0: return
    if idx == n//2:
        calc(choice, list(set(w)- set(choice)))
        # print()
        return
    for i in range(si, n+1):
        choice[idx] = i
        comb(idx+1, i+1)


# for _ in range(3):
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

w = list(range(1, n+1))
choice = [0] * (n//2)
mmin = int(1e9)
comb(0, 1)
print(mmin)