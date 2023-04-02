import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_area(sn, sm, sticker):
    for i in range(N):
        for j in range(M):
            # if arr[i][j]: continue
            stick_ls = can_stick(sn, sm, i, j, sticker)
            if stick_ls:
                for si, sj, e in stick_ls:
                    if e: arr[si][sj] = e
                return True # 붙였으면 끝
    return False


def can_stick(sn, sm, i, j, sticker):
    stick_ls = []
    for di in range(sn):
        for dj in range(sm):
            ni, nj = i + di, j + dj
            # 못붙이는 경우
            if ni < 0 or ni >= N or nj < 0 or nj >= M: return
            if arr[ni][nj] and sticker[di][dj]: return
            if not arr[ni][nj] and sticker[di][dj]:
                stick_ls.append((ni, nj, 1))
            if not sticker[di][dj]:
                stick_ls.append((ni, nj, 0))
    return stick_ls


# for _ in range(8):
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

# 입력이 최대 100개까지 들어오니까 다 저장하지 말고 하나하나 처리하기
for _ in range(K):
    sn, sm = map(int, input().split())
    now_sticker = [list(map(int, input().split())) for _ in range(sn)]
    for _ in range(4):
        if find_area(sn, sm, now_sticker): break
        else:
            now_sticker = list(map(list, zip(*now_sticker[::-1])))
            sn, sm = sm, sn
res = 0
for a in arr:
    # print(a)
    res += sum(a)
print(res)