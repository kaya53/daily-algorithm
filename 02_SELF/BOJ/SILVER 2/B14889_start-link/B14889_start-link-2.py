import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def check(start, link):
    global mmin

    s_res = 0
    for s1 in start:
        for s2 in start:
            if s1 == s2: continue
            s_res += arr[s1][s2]

    l_res = 0
    for l1 in link:
        for l2 in link:
            if l1 == l2: continue
            l_res += arr[l1][l2]

    r = abs(s_res-l_res)
    if mmin > r:
        mmin = r


def comb(idx, ci, now_set):
    if idx == N // 2:
        check(now_set, whole-now_set)
        return

    for ni in range(ci, N):
        now_set.add(ni)
        comb(idx+1, ni+1, now_set)
        now_set.remove(ni)


# for _ in range(3):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

whole = set(range(N))
half = N // 2
choice = [0] * N
mmin = int(1e9)
comb(0, 0, set())
print(mmin)