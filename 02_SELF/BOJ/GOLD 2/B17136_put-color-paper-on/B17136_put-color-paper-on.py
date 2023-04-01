import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def can_stick(si, sj, size):
    for i in range(si, si+size):
        for j in range(sj, sj+size):
            # 인덱스 밖, 0인 칸, 이미 색종이가 붙여진 칸이 있으면
            if (i < 0 or i >= 10 or j < 0 or j >= 10) or not arr[i][j]:
                return False
    return True


def paper_on_off(si, sj, size, marking):
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            arr[i][j] = marking  # 색종이 붙이기/ 떼기


def backtrack(ci, cnt, one_cnt, paper_ls, paper_cnt):  # 현재 좌표, 선택한 색종이 개수
    global res
    if res <= cnt: return
    if not paper_cnt: return  # 25장 다 쓴 경우
    if not one_cnt:
        res = min(res, cnt)
        return

    for ni in range(ci, 10):
        for nj in range(10):
            if arr[ni][nj] != 1: continue
            for size in range(1, 6):
                if not paper_ls[size]: continue # 이미 다 쓴 경우
                if not can_stick(ni, nj, size): return
                paper_on_off(ni, nj, size, 0)

                one_cnt -= size*size
                paper_cnt -= 1
                paper_ls[size] -= 1
                backtrack(ni, cnt+1, one_cnt, paper_ls, paper_cnt)
                paper_on_off(ni, nj, size, 1)
                paper_cnt += 1
                paper_ls[size] += 1
                one_cnt += size * size


for _ in range(8):
    arr = [list(map(int, input().split())) for _ in range(10)]
    res = 26
    paper_ls = [0] + [5]*5
    one_cnt = 0
    for a in arr:
        one_cnt += sum(a)
    backtrack(0, 0, one_cnt, paper_ls, 25)
    if res == 26:
        print(-1)
    else:
        print(res)

