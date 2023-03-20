import sys

# sys.stdin = open('input.txt')


import sys

# sys.stdin = open('input.txt')


def check(arr):
    # 사다리 출발 번호 == 끝 번호인 지
    for lad in range(n):
        visited = set()
        si, sj = lad, 0
        while si != h-1:
            if sj == 0:
                if arr[si][sj] and (si, sj) not in visited:
                    visited.add((si, sj))
                    sj = sj + 1
                else:
                    si = si + 1
            elif sj == n-1:
                if arr[si][sj-1] and (si, sj-1) not in visited:
                    visited.add((si, sj - 1))
                    sj -= 1
                else:
                    si = si + 1
            else:
                if arr[si][sj] and (si, sj) not in visited:
                    visited.add((si, sj))
                    sj = sj + 1
                elif arr[si][sj-1] and (si, sj-1) not in visited:
                    visited.add((si, sj-1))
                    sj = sj - 1
                else:
                    si = si + 1
        if lad != sj:
            return False
    return True


def comb(si, idx, cnt, arr):
    global flag

    if idx == cnt:
        if check(arr):
            flag = True
        return

    # if arr[si][sj] == 1: return
    for ni in range(si, h-1):
        # if sj == h-2:
        for nj in range(n-1):
            if arr[ni][nj]: continue
            if nj == 0:
                if arr[ni][nj+1]: continue
            elif nj == n - 2:
                if arr[ni][nj - 1]: continue
            elif arr[ni][nj - 1] or arr[ni][nj + 1]: continue
            arr[ni][nj] = 1
            comb(si, idx + 1, cnt, arr)
            arr[ni][nj] = 0
            if flag: return


n, m, h = map(int, input().split())  # 행, 놓여진 가로선 개수, 열
arr = [[0]*(n-1) for _ in range(h-1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

cnt = 0
flag = False
while True:
    cnt += 1
    print(cnt)
    if cnt > 3:
        print(-1)
        break
    comb(0, 0, cnt, arr)
    if flag:
        print(cnt)
        break

