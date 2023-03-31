import sys

sys.stdin = open('input.txt')


from copy import deepcopy


def dfs(si, sj, score, arr):
    global max_score
    # 물고기 와구
    score += arr[si][sj][0]
    if max_score < score:
        max_score = score
    arr[si][sj][0] = 0  # 먹은 자리는 0으로

    # 물고기 이동
    for k in range(1, 17):  # 1~16까지 순서대로 가게 하기 위해서
        ci, cj = -1, -1
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == k:  # k번 상어를 찾았다
                    ci, cj = i, j
                    break
        if ci == -1 and cj == -1: continue  # 해당 물고기가 없는 경우
        now_d = arr[ci][cj][1]

        for d in range(8):  # 8방향 탐색 => 모두 안되면 이번 물고기는 이동을 안함
            next_d = (now_d + d) % 8  # 이렇게 하면 현재 방향부터 탐색 가능; 갈 수 있는 게 나오면 걔를 골라서 break
            ni, nj = ci + delta[next_d][0], cj + delta[next_d][1]
            if (ni < 0 or ni >= 4 or nj < 0 or nj >= 4) or (ni == si and nj == sj): continue  # 인덱스 밖 or 상어를 만나면 x
            arr[ci][cj][1] = next_d
            arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
            break

    # 물고기 다시 와구와구
    shark_d = arr[si][sj][1]
    for z in range(1, 4):  # 3칸까지 이동 가능
        ni, nj = si + delta[shark_d][0]*z, sj + delta[shark_d][1]*z
        if (0 <= ni < 4 and 0 <= nj < 4) and arr[ni][nj][0] > 0:  # 인덱스 밖이면 x
            dfs(ni, nj, score, deepcopy(arr))  # [i[:] for i in arr] 이건 딥카피가 안된다.


delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
# for _ in range(4):
arr = [[], [], [], []]
for y in range(4):
    inp = list(map(int, input().split()))
    for x in range(0, 7, 2):
        arr[y].append([inp[x], inp[x+1]-1])  # 방향 -1 해줌

max_score = 0
dfs(0, 0, 0, arr)  # 상어 초기 위치, 점수, 배열
print(max_score)