import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def find_area(range_i, range_j, border):
    popul = 0
    for i in range_i:
        for j in range_j:
            if (i, j) in border: break
            popul += arr[i][j]

    return popul


def calc_population(choice):
    i, j, d1, d2 = choice
    visited = [[0] * n for _ in range(n)]
    border = set()
    fi, fj = i+d2, j+d2
    for dd1 in range(d1+1):
        border.add((i+dd1, j-dd1))
        border.add((fi+dd1, fj-dd1))
    ti, tj = i+d1, j-d1
    for dd2 in range(d2+1):
        border.add((i+dd2, j+dd2))
        border.add((ti+dd2, tj+dd2))

    pop1 = find_area(range(i+d1), range(j+1), border)  # 1
    pop2 = find_area(range(i+d2, -1, -1), range(n-1, j, -1), border)  # 2
    pop3 = find_area(range(i+d1, n), range(j-d1+d2), border)  # 3
    pop4 = find_area(range(n-1, i+d2, -1), range(n-1, j-d1+d2-1, -1), border)  # 4
    pop5 = whole_ssum - (pop1 + pop2 + pop3 + pop4)

    res = max(pop1, pop2, pop3, pop4, pop5) - min(pop1, pop2, pop3, pop4, pop5)
    return res


def comb(idx, i, j, d1, d2):
    global mmin

    if idx == 4:
        ci, cj, cd1, cd2 = choice
        if 0 <= ci <= ci+cd1+cd2 < n and 0 <= cj-cd1 < cj < cj+cd2 < n:
            res = calc_population(choice)
            mmin = min(mmin, res)
        return

    if not idx:
        for ni in range(i, n):
            choice[idx] = ni
            comb(1, ni+1, j, d1, d2)
    elif idx == 1:
        for nj in range(j, n):
            choice[idx] = nj
            comb(2, i, nj+1, d1, d2)
    elif idx == 2:
        for nd1 in range(d1, n):
            choice[idx] = nd1
            comb(3, i, j, nd1+1, d2)
    elif idx == 3:
        for nd2 in range(d2, n):
            choice[idx] = nd2
            comb(4, i, j, d1, nd2+1)


n = int(input())
arr = [[] for _ in range(n)]
whole_ssum = 0
for nn in range(n):
    inp = list(map(int, input().split()))
    arr[nn] = inp
    whole_ssum += sum(inp)


mmin = int(1e9)
choice = [0] * 4
comb(0, 0, 0, 1, 1)
print(mmin)