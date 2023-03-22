import sys

sys.stdin = open('input.txt')


def is_parellel(selected):
    u1, u2 = selected  # 0, 1
    for p1, p2 in univ_ls:
        u1p1 = univ[u1][p1]
        u1p2 = univ[u1][p2]
        u2p1 = univ[u2][p1]
        u2p2 = univ[u2][p2]
        if (u1p1 < u1p2 and u2p1 < u2p2) or (u1p1 > u1p2 and u2p1 > u2p2) or (u1p1 == u1p2 and u2p1 == u2p2):
            continue
        else: return False
    return True


def comb(si, idx, mmax, flag):
    global cnt

    if idx == 2:
        if flag == 'out':
            if is_parellel(selected):
                cnt += 1
        elif flag == 'in':
            univ_ls.append(list(selected))
        return
    for i in range(si, mmax):
        selected[idx] = i
        comb(i+1, idx+1, mmax, flag)
        selected[idx] = 0


m, n = map(int, input().split())  # 우주 개수, 우주 내 행성 개수
univ = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
selected = [0, 0]
univ_ls = []
comb(0, 0, n, 'in')

comb_ls = []
comb(0, 0, m, 'out')

print(cnt)