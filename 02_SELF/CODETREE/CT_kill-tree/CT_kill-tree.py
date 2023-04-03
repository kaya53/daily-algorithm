import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def grow_tree():
    # 어차피 arr에서 빼고 하는 것 없이 구한 tree_cnt만 더해주면 되므로; 나무가 있냐 없냐가 문제니깐
    # 여기서는 임시 배열이 굳이 필요가 없다.
    can_grow = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue
            tree_cnt = 0
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if arr[ni][nj] > 0: tree_cnt += 1
            can_grow[i][j] += tree_cnt  # 여기서 바로 arr에 더해줘도 됨!
    for ii in range(N):
        for jj in range(N):
            arr[ii][jj] += can_grow[ii][jj]


def spread_tree():
    can_spread = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue
            empty_cnt = 0
            spread_ls = []
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if not arr[ni][nj]:
                    empty_cnt += 1
                    spread_ls.append((ni, nj))
            if empty_cnt:
                size = arr[i][j] // empty_cnt
                for ssi, ssj in spread_ls:
                    can_spread[ssi][ssj] += size

    for ii in range(N):
        for jj in range(N):
            arr[ii][jj] += can_spread[ii][jj]


def check_drug():
    pop_ls = []
    for dr in drug:
        if drug[dr] > C:  # 제초제 사라짐
            dri, drj = dr
            if arr[dri][drj] == -2:  # 벽은 -2로 표기를 안해놨기 때문에
                arr[dri][drj] = 0
            pop_ls.append(dr)
    for elem in pop_ls:
        drug.pop(elem)


def max_drug():
    mmax = max_i = max_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue
            killed = arr[i][j]
            for di, dj in diag_delta:
                for kk in range(1, K+1):
                    ni, nj = i + di*kk, j+ dj*kk
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: break
                    # if not arr[ni][nj] or arr[ni][nj] == -1: break
                    if arr[ni][nj] <= 0: break
                    # if arr[ni][nj] > 0:
                    killed += arr[ni][nj]
            # print(i, j, killed)
            if mmax < killed:
                mmax, max_i, max_j = killed, i, j
            # elif mmax == killed:
            #     if max_i > i:
            #         max_i, max_j = i, j
            #     elif max_i == i and max_j > j:
            #         max_j = j
    return mmax, max_i, max_j


def spread_drug(max_i, max_j):
    # 제초제 뿌리기
    arr[max_i][max_j] = -2
    drug[(max_i, max_j)] = 0
    for ddi, ddj in diag_delta:
        for k in range(1, K + 1):
            ni, nj = max_i + ddi * k, max_j + ddj * k
            if ni < 0 or ni >= N or nj < 0 or nj >= N: break
            if arr[ni][nj] == -2:
                drug[(ni, nj)] = 0
                break
            elif arr[ni][nj] > 0:
                drug[(ni, nj)] = 0
                arr[ni][nj] = -2
            elif arr[ni][nj] == 0:
                drug[(ni, nj)] = 0
                arr[ni][nj] = -2
                break
            elif arr[ni][nj] == -1:
                drug[(ni, nj)] = 0
                break


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
diag_delta = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# for _ in range(2):
N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

drug = {}
res = 0
for _ in range(M):

    grow_tree()
    spread_tree()

    ans, mi, mj = max_drug()

    res += ans
    spread_drug(mi, mj)
    for dr in drug:
        drug[dr] += 1
    check_drug()
print(res)

