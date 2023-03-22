import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def down(arr):
    for sj in range(J):  # 시작 세로선
        ci, cj = 0, sj
        # try:
        while ci < I:
            if cj + 1 <= J - 1 and arr[ci][cj]:
                ci, cj = ci + 1, cj + 1
            elif cj - 1 >= 0 and arr[ci][cj-1]:
                ci, cj = ci + 1, cj - 1
            else:
                ci += 1
        if sj != cj:
            return False
    return True


def ladder(si, idx, n, arr):  # 현재 행 번호, 몇개 골랐는 지, 총 고를 사다리 수, 배열
    global flag

    if idx == n:
        if flag: return
        if down(arr):
            # i => i로 가는 경우
            flag = True
        return
    for ni in range(si, I):
        for nj in range(J-1):
            # 전후에 사다리가 있으면 continue 조건 추가하기
            if arr[ni][nj]: continue
            if J-2 != 0:  # 한 줄 이상일 때만 이 조건 보기
                if not nj and arr[ni][nj+1]: continue
                elif nj == J-2 and arr[ni][nj-1]: continue
                elif 0 < nj < J-2 and (arr[ni][nj-1] or arr[ni][nj+1]): continue
            arr[ni][nj] = 1
            ladder(ni, idx+1, n, arr)
            if flag: return
            arr[ni][nj] = 0


# for _ in range(7):
J, M, I = map(int, input().split())  # i, j: 행열, m: 초기에 놓여있는 가로선 수
arr = [[0] * (J-1) for _ in range(I)]
for m in range(M):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

res = -1
flag = False
for n in range(4):
    ladder(0, 0, n, arr)
    if flag:
        res = n
        break
print(res)

