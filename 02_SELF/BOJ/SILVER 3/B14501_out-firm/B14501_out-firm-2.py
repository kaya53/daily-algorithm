import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def dfs(now, score):
    global mmax
    if now > N:  # 일하다보니 퇴사일이다!
        mmax = max(mmax, score)
        # print(score, now, ls)
        return
    for ni in range(now, N+1):
        # 상담이 가능한 경우
        if ni + time_ls[ni] <= N+1:
            dfs(ni+time_ls[ni], score+cost_ls[ni])
    else:  # 이후에 가능한 상담일이 없으면 리턴
        mmax = max(mmax, score)
        return


# for _ in range(4):
N = int(input())

time_ls = [0]
cost_ls = [0]
for _ in range(N):
    t, c = map(int, input().split())
    time_ls.append(t)
    cost_ls.append(c)

mmax = 0
dfs(1, 0)
print(mmax)
