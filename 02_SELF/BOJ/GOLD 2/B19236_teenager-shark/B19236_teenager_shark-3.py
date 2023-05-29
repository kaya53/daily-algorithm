# 230529 python 64ms
# 의문점
# 1. 왜 dfs를 돌릴 때 상어의 위치를 되돌리지 않아도 될까
# - 상어가 여기를 가보고 그 다음에 저기를 가보고 하는 거니까 되돌려야 할 것 같은데
# - 안되돌리는 게 아니라 teenager-shark-2 버전에서는
#   한 재귀 단계에서 처리해야 할 일을 모두 했기 때문이다.
# - 그러니까 그 단계에서만 처리가 되기 때문에 이전 단계로 돌아오면 알아서 되돌려져 있는 것이다.

# 1-1. 내가 원래 풀었던 대로 바꾸고 -> 보내고 -> 되돌리고로 해도 답은 나온다.
# - 다만, 이렇게 하면 move_shark를 실행하기 전에 (0,0)의 물고기를 먹는 작업을 해줘야 한다.
# - 1.의 방법을 쓰면 이걸 안해줘도 된다.
# - 수업 시간에 했었던 visited를 언제 해주냐처럼 시점 차이일 뿐이지 둘은 똑같은 코드이다.
import sys
from copy import deepcopy

sys.stdin = open('input.txt')


def find_fish(arr, fish_no):
    for i in range(4):
        for j in range(4):
            if arr[i][j] and arr[i][j][0] == fish_no:
                return i, j, arr[i][j][1]


def move_fish(arr, c_shi, c_shj):
    for fish_no in range(1, 17):
        find_res = find_fish(arr, fish_no)
        if not find_res: continue
        fi, fj, fd = find_res
        for k in range(8):
            nd = (fd+k) % 8
            ni, nj = fi + delta[nd][0], fj + delta[nd][1]
            if ni < 0 or ni >= 4 or nj < 0 or nj >= 4 or (ni, nj) == (c_shi, c_shj): continue
            # 방향을 바꿨든 원래 이동이 가능했든
            arr[ni][nj], arr[fi][fj] = arr[fi][fj], arr[ni][nj]
            arr[ni][nj][-1] = nd
            break
            # 이동할 칸이 없음

    return arr


def move_shark(ssum, arr, c_shi, c_shj):
    global res
    
    # for문에서 걸리는 게 하나도 없을 때도 리턴되서 여기로 오면 여기서 최대값이 갱신될 것
    if res < ssum:
        res = ssum

    # 물고기 이동
    arr = move_fish(arr, c_shi, c_shj)

    # 상어 이동
    shd = arr[c_shi][c_shj][1]
    for k in range(1, 4):
        ni, nj = c_shi + delta[shd][0]*k, c_shj + delta[shd][1]*k
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4 or arr[ni][nj][0] == 0: continue
        fish_no = arr[ni][nj][0]
        arr[ni][nj][0] = 0
        move_shark(ssum+fish_no, deepcopy(arr), ni, nj)
        arr[ni][nj][0] = fish_no


delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
# for _ in range(4):
ocean = [[0]*4 for _ in range(4)]
no = 0
for r in range(4):
    inp = list(map(int, input().split()))
    for c in range(4):
        ocean[r][c] = [inp[c*2], inp[2*c+1]-1]

res = ocean[0][0][0]
ocean[0][0][0] = 0

# 처음에 한 번 움직이는 물고기들
move_shark(res, deepcopy(ocean), 0, 0)
print(res)