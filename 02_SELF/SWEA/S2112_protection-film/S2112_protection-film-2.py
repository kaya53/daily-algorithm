import sys

# sys.stdin = open('input.txt')


def test(mtx):
    for j in range(W):
        i = 0
        while i <= D-K:
            ssum = 0
            for ni in range(i, i+K):
                ssum += mtx[ni][j]
            if ssum == 0 or ssum == K: break  # 통과됨
            i += 1
        else: return False
    return True


def powerset(idx, si, n, mtx):
    global flag
    if flag: return
    if idx == n:
        if test(mtx):
            flag = True
        return
    for ni in range(si, D):
        tmp = mtx[ni]
        mtx[ni] = [1] * W
        powerset(idx+1, ni+1, n, mtx)
        mtx[ni] = [0] * W
        powerset(idx+1, ni+1, n, mtx)
        mtx[ni] = tmp


t = int(input())
for tc in range(1, t+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    if test(arr):
        print(f'#{tc} 0')
    else:
        flag = False
        for n in range(1, D+1):
            meds = []
            powerset(0, 0, n, [x[:] for x in arr])
            if flag:
                print(f'#{tc} {n}')
                break


