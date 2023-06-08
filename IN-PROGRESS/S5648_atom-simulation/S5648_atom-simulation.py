import sys

sys.stdin = open('input.txt')


def crash():
    global res, remain

    moved = [[0, 0, 0, 0] for _ in range(N)]
    for idx, atom in enumerate(atoms):
        if not atom: continue
        ci, cj, cd, en = atom
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        atoms[idx][0], atoms[idx][1] = ni, nj
        moved[idx] = [ci, cj, ni, nj]

    crash_set = set()
    for me in range(N):
        for you in range(N):
            if me == you: continue
            if not atoms[me] or not atoms[you]: continue
            mci, mcj, mni, mnj = moved[me]
            yci, ycj, yni, ynj = moved[you]
            # 충돌함
            if ((mni, mnj) == (yni, ynj)) or ((mci, mcj) == (yni, ynj) and (mni, mnj) == (yci, ycj)):
                crash_set.add(me)
                crash_set.add(you)
    if crash_set:
        remain -= len(crash_set)
        for deleted in crash_set:
            en = atoms[deleted][-1]
            res += en
            atoms[deleted] = None
        return True
    return False


def check():
    for me in range(N):
        for you in range(N):
            if me == you or not atoms[me] or not atoms[you]: continue
            mi, mj, md = atoms[me][:3]
            yi, yj, yd = atoms[you][:3]

            if (mi == yi) or (mj == yj):
                dist2 = max(abs(mi-yi), abs(mj-yj))
                mni, mnj = mi + delta[md][0]*dist2, mj + delta[md][1]*dist2
                yni, ynj = yi + delta[yd][0]*dist2, yj + delta[yd][1]*dist2
                if (mi == yi) and abs(mni-yni) <= 1: return False
                if (mj == yj) and abs(mnj-ynj) <= 1: return False
            else:
                if abs(mi - yi) == abs(mj - yj):
                    dist1 = abs(mi - yi)
                    mni, mnj = mi + delta[md][0] * dist1, mj + delta[md][1] * dist1
                    yni, ynj = yi + delta[yd][0] * dist1, yj + delta[yd][1] * dist1
                    if (mni, mnj) == (yni, ynj): return False
    return True


d_comb = [(0, 2), (0, 3), (2, 1), (3, 1), (2, 0), (3, 0), (1, 2), (1, 3)]
delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [[0, 0, 0, 0] for _ in range(N)]
    for n in range(N):
        x, y, d, k = map(int, input().split())
        atoms[n] = [y, x, d, k]

    res = 0
    remain = N
    while True:
        crash()
        if remain <= 1: break
        if check(): break
    print(f'#{tc} {res}')