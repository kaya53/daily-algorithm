import sys

# sys.stdin = open('input.txt')


import sys

# sys.stdin = open('input.txt')


def comb(si, idx, cnt, arr):
    global flag

    if idx == cnt:
        # if si == n-1 and sj == 0:  # 끝까지 가면 0을 다음 재귀로 넘기니까
        #     flag = True
        if cnt == 2:
            print(si, sj)
            for a in arr:
                print(a)
            print()

        return

    # if arr[si][sj] == 1: return
    for ni in range(si, n):
        # if sj == h-2:
        for nj in range(1, h-1):
            if not arr[ni][nj-1] and not arr[ni][nj] and arr[ni][nj+1]:
                arr[ni][nj] = arr[ni][nj+1] = 1
                comb(si, idx+1, cnt, arr)
                arr[ni][nj] = arr[ni][nj+1] = 0


n, m, h = map(int, input().split())  # 행, 놓여진 가로선 개수, 열
arr = [[0]*h for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1], arr[a-1][b] = 1, 1

cnt = 0
flag = False
while True:
    cnt += 1
    comb(0, 0, cnt, arr)
    print('------')
    if cnt == 2:
        break
    # if flag: break  # 사다리 결과가 시작 번호가 아닌 경우


def comb(si, sj, idx, cnt, arr):
    global flag

    if idx == cnt:
        # if si == n-1 and sj == 0:  # 끝까지 가면 0을 다음 재귀로 넘기니까
        #     flag = True
        if cnt == 2:
            print(si, sj)
            for a in arr:
                print(a)
            print()

        return

    # if arr[si][sj] == 1: return
    for ni in range(si, n):
        # if sj == h-2:
        for nj in range(sj, h-1):
            if arr[ni][nj] == 1: continue  # 이미 가로선이 놓인 칸 -> 그 다음 칸으로
            if nj == h-2: # 하나 더만 보고 갈 수 있으면 가기
                if not arr[ni][nj-1] and not arr[ni][nj] and not arr[ni][nj+1]:
                    arr[ni][nj] = arr[ni][nj+1] = 1
                    comb(ni+1, 0, idx+1, cnt, arr)
                    arr[ni][nj] = arr[ni][nj+1] = 0
                    sj = 0
                    if flag: return
                else:  # 선택 없이 그 다음 행으로
                    comb(ni+1, 0, idx, cnt, arr)
                    if flag: return

            else:  # 한 칸 오른쪽이랑 두칸 오른쪽을 보고 갈 수 있으면 가기
                if (nj < 1 or not arr[ni][nj-1]) and not arr[ni][nj] and not arr[ni][nj+1] and not arr[ni][nj+2]:
                    arr[ni][nj] = arr[ni][nj+1] = 1
                    comb(ni, nj+1, idx + 1, cnt, arr)
                    arr[ni][nj] = arr[ni][nj+1] = 0
                    if flag: return

                else:
                    comb(ni, nj+1, idx, cnt, arr)
                    if flag: return


n, m, h = map(int, input().split())  # 행, 놓여진 가로선 개수, 열
arr = [[0]*h for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1], arr[a-1][b] = 1, 1

cnt = 0
flag = False
while True:
    cnt += 1
    comb(0, 0, 0, cnt, arr)
    print('------')
    if cnt == 2:
        break
    # if flag: break  # 사다리 결과가 시작 번호가 아닌 경우