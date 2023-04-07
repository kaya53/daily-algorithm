import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

# 달팽이 모양으로 꺾을 모서리 찾는 함수
def get_corners():
    t = 1
    d = 2
    cor = set()
    ci, cj = shi, shj
    while (ci, cj) != (0, 0):
        for _ in range(2):
            coi, coj = max(0, ci + delta[d][0] * t), max(0, cj + delta[d][1] * t)
            cor.add((coi, coj))
            d = snail_d[d]
            ci, cj = coi, coj
            if (ci, cj) == (0, 0): break
        t += 1
    return cor


# 얼음 파편 날리는 함수
def destroy_beads(nd, ns):
    ci, cj = shi, shj
    for k in range(1, ns+1):
        ni, nj = ci + delta[nd][0]*k, cj + delta[nd][1]*k
        if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
        arr[ni][nj] = 0


def put_bead(ls):
    ci, cj, cd = shi, shj, 2  # 중앙에서 시작
    while (ci, cj) != (0, 0):
        while ls:
            now_bead = ls.popleft()
            ni, nj = ci + delta[cd][0], cj + delta[cd][1]

            arr[ni][nj] = now_bead
            if (ni, nj) in corners: cd = snail_d[cd]
            if (ni, nj) == (0, 0): return
            ci, cj = ni, nj
        # print(ci, cj)
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if arr[ni][nj]: arr[ni][nj] = 0
        if (ni, nj) in corners: cd = snail_d[cd]

        ci, cj = ni, nj


# 빈칸 하나씩 당기는 함수
def pull_bead():
    # 숫자만 뽑기
    ci, cj, cd = shi, shj, 2  # 중앙에서 시작
    nums = deque()
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if (ni, nj) in corners: cd = snail_d[cd]
        if arr[ni][nj]: nums.append(arr[ni][nj])
        ci, cj = ni, nj

    # 밀어서 넣어놓기
    put_bead(nums)
    # for a in arr:
    #     print(a)


# 구슬 폭발 함수
def bomb_bead():
    global bead1, bead2, bead3

    res = False
    ci, cj, cd = shi, shj, 2
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if (ni, nj) in corners: cd = snail_d[cd]

        if arr[ci][cj] and arr[ci][cj] == arr[ni][nj]:
            b = arr[ci][cj]
            s_cnt = 1
            same = [(ci, cj)]
            ci, cj = ni, nj
            while arr[ci][cj] == b:
                s_cnt += 1
                same.append((ci, cj))
                ni, nj = ci + delta[cd][0], cj + delta[cd][1]
                if (ni, nj) in corners: cd = snail_d[cd]
                ci, cj = ni, nj
            if s_cnt >= 4:
                res = True
                for ii, jj in same:
                    if arr[ii][jj] == 1: bead1 += 1
                    elif arr[ii][jj] == 2: bead2 += 1
                    elif arr[ii][jj] == 3: bead3 += 1
                    arr[ii][jj] = 0
        else: ci, cj = ni, nj
    # for a in arr:
    #     print(a)
    return res


# 구슬 늘리는 함수
def bead_control():
    cd = 2
    # 상어 다음부터 시작
    ci, cj = shi + delta[cd][0], shj + delta[cd][1]
    if (ci, cj) in corners: cd = snail_d[cd]
    controlled = deque()
    while (ci, cj) != (0, 0):
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if (ni, nj) in corners: cd = snail_d[cd]
        if not arr[ci][cj]: break
        if arr[ci][cj] == arr[ni][nj]:
            b = arr[ci][cj]
            s_cnt = 1
            # same = [(ci, cj)]
            ci, cj = ni, nj
            while arr[ci][cj] == b:
                s_cnt += 1
                # same.append((ci, cj))
                ni, nj = ci + delta[cd][0], cj + delta[cd][1]
                if (ni, nj) in corners: cd = snail_d[cd]
                ci, cj = ni, nj
            controlled.extend([s_cnt, b])
        else:  # 연속한 구슬이 1개
            controlled.extend([1, arr[ci][cj]])
            ci, cj = ni, nj
    # print(controlled)
    put_bead(controlled)


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(4):
snail_d = {0: 2, 2: 1, 1: 3, 3: 0}
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shi, shj = N//2, N//2

corners = get_corners()  # 모서리 모음
bead1 = bead2 = bead3 = 0
for _ in range(M):
    nd, ns = map(int, input().split())
    destroy_beads(nd-1, ns)
    pull_bead()
    while bomb_bead():
        pull_bead()
    bead_control()

print(bead1+(2*bead2)+(3*bead3))

