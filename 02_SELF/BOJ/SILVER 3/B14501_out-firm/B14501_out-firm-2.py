import sys

sys.stdin = open('input.txt')


def dfs(now, score, ls):
    global mmax
    if now >= N:
        mmax = max(mmax, score)
        print(score, now, ls)
        return
    for ni in range(now, N+1):
        if ni + time_ls[ni] <= N:
            dfs(ni+time_ls[ni], score+cost_ls[ni], ls+[(ni+time_ls[ni], score+cost_ls[ni])])


for _ in range(4):
    N = int(input())

    time_ls = [0]
    cost_ls = [0]
    for _ in range(N):
        t, c = map(int, input().split())
        time_ls.append(t)
        cost_ls.append(c)

    mmax = 0
    dfs(1, 0, [])
    print(mmax)
    print('-----------')