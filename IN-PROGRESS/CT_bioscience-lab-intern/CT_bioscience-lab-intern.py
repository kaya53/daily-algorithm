import sys

sys.stdin = open('input.txt')


def move_germ(ci, cj):
    # 크기, 움직일 거리, 방향 => 바뀔 수 있는 건 방향과 위치
    size, dist, d = arr[ci][cj]
    calc_dist = dist
    ni, nj = -1, -1
    if d == 0:  # 상
        if calc_dist <= ci: # 방향 안바꾸고 그냥 갈 수 있음
            ni = ci - calc_dist
        else:  # 그 이상
            calc_dist -= ci
            k, z = divmod(calc_dist, N-1)
            if k % 2 == 0:
                d ^= 1
                ni = z
            else:
                ni = N - 1 - z
        nj = cj
    elif d == 3:  # 좌
        if calc_dist <= cj:
            nj = cj - calc_dist
        else:
            calc_dist -= cj
            k, z = divmod(calc_dist, M-1)
            if k % 2 == 0:
                d ^= 1
                nj = z
            else:
                nj = M - 1 -z
        ni = ci
    elif d == 1:
        if calc_dist <= (N-1) - ci:
            ni = ci + calc_dist
        else:
            calc_dist -= N-1-ci
            k, z = divmod(calc_dist, N-1)
            if k % 2 == 0:
                d ^= 1
                ni = N-1-z
            else: ni = z
        nj = cj
    elif d == 2:
        if calc_dist <= (M - 1) - cj:
            nj = cj + calc_dist
        else:
            calc_dist -= M - 1 - cj
            k, z = divmod(calc_dist, M-1)
            if k % 2 == 0:
                d ^= 1
                nj = M-1-z
            else:
                nj = z
        ni = ci
    # 현재 사이즈가 더 큰 경우에만 들어감
    return ci, cj, ni, nj, d, arr[ci][cj]


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상하우좌
# for _ in range(4):
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    i, j, s, d, b = map(int, input().split())
    arr[i-1][j-1] = [b, s, d-1]  # 크기, 움직이는 거리, 이동 방향

res = 0
for j in range(M):  # 승용이가 한 칸씩 이동
    # 곰팡이 채취
    for i in range(N):
        if arr[i][j]:
            res += arr[i][j][0]
            arr[i][j] = 0
            break
    # 곰팡이 이동
    after_move = []
    only_after = set()
    for mi in range(N):
        for mj in range(M):
            if arr[mi][mj]:
                # 움직인 이후 좌표
                moved = move_germ(mi, mj)
                if moved: after_move.append(moved)

    tmp = [[0] * M for _ in range(N)]
    for bi, bj, ai, aj, new_d, before in after_move:
        # print(bi, bj, 'size', arr[bi][bj][0], 'before //', end=' ')
        # print(ai, aj, arr[ai][aj], 'after')
        # print(tmp[ai][aj], tmp[bi][bj])

        if (ai, aj) == (bi, bj):
            arr[ai][aj][2] = new_d
            tmp[ai][aj] = arr[ai][aj][:]
        elif tmp[ai][aj] == 0 or (tmp[ai][aj] and tmp[ai][aj][0] < arr[bi][bj][0]):
            tmp[ai][aj] = [arr[bi][bj][0], arr[bi][bj][1], new_d]
        # for t in tmp:
        #     print(t)
        # print()
    arr = tmp
    # for a in arr:
    #     print(a)
    # print()
print(res)