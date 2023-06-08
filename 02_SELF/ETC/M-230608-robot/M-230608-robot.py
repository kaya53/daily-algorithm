import sys

sys.stdin = open('input.txt')


def get_possible():
    ls = []
    for i in range(N):
        for j in range(N):
            if not i_arr[i][j]:
                for k in range(4):
                    ls.append((i, j, k))
    return ls


def can_move():
    for nd in d_dict[cd]:
        ni, nj = ci + delta[nd][0], cj + delta[nd][1]
        # 빈땅 아니면 곡식인데 싹이 없는 곳
        if arr[ni][nj] == 0 or arr[ni][nj] == 2: return ni, nj, nd
    return None


def am_robot():
    global res

    if arr[ci][cj] == 0:
        can = can_move()
        if can:
            arr[ci][cj] = [grass[ci][cj]+1, -1]  # 씨 심기
            grass[ci][cj] += 1
        # 아무 것도 하지 않음
    elif arr[ci][cj] == 2:  # 곡식
        arr[ci][cj] = 0
        res += 1  # 수확


def pm_robot():
    global ci, cj, cd
    nnext = can_move()
    if nnext:
        ci, cj, cd = nnext
    # 이동 가능한 곳 없음 => 이동 안함


def plus_time():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and arr[i][j] != 1 and arr[i][j] != 2:
                arr[i][j][1] += 1
                if arr[i][j][1] == 3 + arr[i][j][0]:  # 곡식
                    arr[i][j] = 2


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
d_dict = {
    0: [3,0,2,1],
    1: [2,1,3,0],
    2: [0,2,1,3],
    3: [1,3,0,2]
}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    i_arr = [list(map(int, input().split())) for _ in range(N)]

    possible = get_possible()

    max_res = 0
    for si, sj, sd in possible:
        ci, cj, cd = si, sj, sd
        res = 0
        grass = [[0] * N for _ in range(N)]
        arr = [i[:] for i in i_arr]
        for _ in range(M):
            plus_time()
            am_robot()
            pm_robot()

        if max_res < res:
            max_res = res
    print(f'#{tc} {max_res}')