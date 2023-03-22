import sys

sys.stdin = open('input.txt')


def rotate(arr, x, direction, k):
    # 이 함수에서는 돌아간 원판 리턴하기
    idx = x
    # print(x, direction, k)
    while idx <= n:  # x의 배수인 원판을 모두 돌려야 하니까
        # print('b4', arr[idx])
        rotation = k % m
        # print('rotation', rotation, idx)
        if direction == 0:  # 시계
            # tmp = arr[idx]
            # s = m - rotation
            # for elem in arr:
            #     print(elem)
            # print(tmp, tmp[s:], tmp[:s], s)
            arr[idx] = arr[idx][m-rotation:] + arr[idx][:m-rotation]
        elif direction == 1:  # 반시계
            # if k == 3:
            #     print(arr[idx][:rotation], arr[idx][rotation:])
            arr[idx] = arr[idx][rotation:] + arr[idx][:rotation]
        # print('after', arr[idx])
        idx += x
    return arr


def calc(arr):
    global zero_cnt

    # 모든 원판에 대해서 연산 수행
    # flag = 0  # 이 원판에서 인접하면서 같은 수가 있는 것을 세는 것
    to_zero = []
    for ci in range(1, n+1):
        for cj in range(m):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if ni <= 0 or ni > n: continue
                if nj < 0 or nj >= m:
                    nj %= m
                if arr[ci][cj] and arr[ni][nj] and arr[ci][cj] == arr[ni][nj]:
                    to_zero.append((ci, cj))
                    to_zero.append((ni, nj))
                    # flag = 1 # 이 개수가 정확한 개수가 아님
    # zero_cnt += cnt
    # print('zero', cnt, zero_cnt)
    if to_zero:
        for zi, zj in to_zero:
            if not arr[zi][zj]: continue
            arr[zi][zj] = 0
    else:  # 인접한 수가 없음
        zero_cnt = n*m
        ssum = avg = 0
        for x in range(1, n+1):
            ssum += sum(arr[x])
            zero_cnt -= arr[x].count(0)
        # print('avgs', ssum, zero_cnt)
        if not zero_cnt:
            avg = ssum / n*m
        else:
            avg = ssum / zero_cnt
        for z in range(1, n+1):
            for k in range(m):
                if not arr[z][k]: continue
                if arr[z][k] > avg: arr[z][k] -= 1
                elif arr[z][k] < avg: arr[z][k] += 1
    return arr


# for _ in range(5):
n, m, t = map(int, input().split())  # 격자 수, 원판 내 정수의 수, 총 회전 수
arr = [[0]] + [list(map(int, input().split())) for _ in range(n)]
infos = [list(map(int, input().split())) for _ in range(t)]
zero_cnt = 0

for info in infos:
    x, d, k = info  # x의 배수인 원판 돌리기, 돌릴 방향, 회전 수
    # 1. 원판을 돌린다.
    rotated_arr = rotate(arr, x, d, k)
    # 2. 수를 지운다.
    arr = calc(rotated_arr)

tot = 0
for elem in arr:
    tot += sum(elem)
print(tot)
