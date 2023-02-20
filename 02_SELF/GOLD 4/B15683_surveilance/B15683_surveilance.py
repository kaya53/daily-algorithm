import sys

sys.stdin = open('input.txt')

from copy import deepcopy

def comb(cnt):
    global res
    if cnt == len(cctv):
        dir_ls.append(list(choice))
        return
    x = cctv_len[cctv[cnt][-1]]  # cctv 종류 선택 2, 2, 5; choice의 cnt 자리가 cctv 자리가 되어야 하니까
    for j in range(x):  # cctv 방향 선택
        choice[cnt] = j
        comb(cnt+1)
        choice[cnt] = 0


def unseen():
    global res

    for dir_comb in dir_ls:
        copy_arr = deepcopy(arr)
        for cIdx, camera in enumerate(cctv):
            ci, cj, k = camera  # cctv 위치, cctv 번호, 방향 델타의 각 요소에 접근할 인덱스
            delta = dir_comb[cIdx]
            delta_ls = cctv_dir[k][delta]

            for di, dj in delta_ls:  # 여기 이 리스트에 각 방향별 델타가 와야 함
                si, sj = ci, cj
                while True:
                    ni, nj = si + di, sj + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= m or copy_arr[ni][nj] == 6: break
                    if not copy_arr[ni][nj]:
                        copy_arr[ni][nj] = 7
                    si, sj = ni, nj
        # 이 지점에서 사각 지대 세기
        zero_cnt = 0
        for i in range(n):
            for j in range(m):
                if not copy_arr[i][j]: zero_cnt += 1

        if zero_cnt < res:
            res = zero_cnt



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv_len = [0, 4, 2, 4, 4, 1]
cctv_dir = [0,
    [[(0, -1)], [(0, 1)], [(-1, 0)], [(1, 0)]],
    [((-1, 0), (1, 0)), ((0, -1), (0, 1))],
    [((0, -1), (-1, 0)), ((-1, 0), (0, 1)), ((0, 1), (1, 0)), ((1, 0), (0, -1))],
    [((-1, 0), (1, 0), (0, 1)), ((-1, 0), (1, 0), (0, -1)), ((0, -1), (0, 1), (-1, 0)), ((0, -1), (0, 1), (1, 0))],
    [((-1, 0), (1, 0), (0, -1), (0, 1))]
]
cctv = []
# 0. cctv 위치 알아내기
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j, arr[i][j]])

# 1. 방향의 조합 구하기
choice = [0] * len(cctv)
dir_ls = []  # [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
comb(0)

# 2. 각 조합에 대해서 사각지대 구하기
res = float('inf')
unseen()

print(res)