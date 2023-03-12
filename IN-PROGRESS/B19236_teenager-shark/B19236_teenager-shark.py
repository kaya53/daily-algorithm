import sys

sys.stdin = open('input.txt')


def change_dir(ci, cj, d):
    tmp = d
    while True:
        d = (d + 1) % 8
        if d == 0: d = 8
        nni, nnj = ci + delta[d][0], cj + delta[d][1]
        # if arr[ci][cj][0] == 3:
        #     print('333', d)
        if 0 <= nni < 4 and 0 <= nnj < 4:
            if arr[nni][nnj] and arr[nni][nnj][0] != -1:
                fishes[arr[nni][nnj][0]] = ((ci, cj), d)
                fishes[arr[ci][cj][0]] = ((nni, nnj), d)
                # arr[nni][nnj], arr[ci][cj] = arr[ci][cj], arr[nni][nnj]
                arr[nni][nnj], arr[ci][cj] = [arr[ci][cj][0], d], arr[nni][nnj]
                break
            elif not arr[nni][nnj]:
                arr[nni][nnj] = [arr[ci][cj][0], d]
                fishes[arr[ci][cj][0]] = ((nni, nnj), d)
                break
        if d == tmp:  # 다 돌았는 데도 갈 곳이 없는 경우 -> 이동 안함
            break
    # print('while out')

def move_fish():
    print(fishes)
    for fish in fishes:
        if not fish: continue  # 0번 idx나 물고기가 없는 칸
        loc, d = fish
        ci, cj = loc
        now_dir = delta[d]
        # 이번 방향으로 갔는 데 이동 가능하면; 빈칸이거나, 다른 물고기가 있음
        ni, nj = ci + now_dir[0], cj + now_dir[1]
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 가능한 경우 1: 상어가 아닌 물고기가 있는 경우
            # if arr[ni][nj] and arr[ni][nj][0] != -1:
            if arr[ni][nj] and arr[ni][nj][0] != -1:
                # 방향도 그대로 가지고 이동
                fishes[arr[ni][nj][0]] = ((ci, cj), arr[ni][nj][1])
                fishes[arr[ci][cj][0]] = ((ni, nj), arr[ci][cj][1])
                arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
            # 가능한 경우 2: 빈칸인 경우
            elif not arr[ni][nj]:
                arr[ni][nj] = arr[ci][cj]
                fishes[arr[ci][cj][0]] = ((ni, nj), arr[ci][cj][1])
            else:  # 인덱스 안인데 상어가 있거나, 상어도 있는데 빈칸도 아닌 경우
                change_dir(ci, cj, d)
        else:  # 인덱스 밖 - 이동 가능한 방향을 찾을 때까지 돈다
            change_dir(ci, cj, d)

def move_shark():  # 백트래킹
    pass


# input
arr = [[], [], [], []]
for k in range(4):
    inp = list(map(int, input().split()))
    for z in range(0, 7, 2):
        arr[k].append([inp[z], inp[z+1]])

# 상어가 (0, 0)에 가서 7번 물고기를 먹었다
# -1 : 상어
arr[0][0][0] = -1
for elem in arr:
    print(elem)
    
# 물고기의 순서
fishes = [0] * 17
for i in range(4):
    for j in range(4):
        fishes[arr[i][j][0]] = ((i, j), arr[i][j][1])

delta = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}

while True:
    # 종료 조건: 상어가 더 이상 이동할 곳이 없을 때
    # 1. 물고기 이동
    move_fish()
    print()
    for elem in arr:
        print(elem)
    for idx, fish in enumerate(fishes):
        print(idx, fish)
    # 2. 상어 이동 - 백트래킹
    move_shark()
    break