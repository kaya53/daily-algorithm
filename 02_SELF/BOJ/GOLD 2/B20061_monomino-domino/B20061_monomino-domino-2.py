import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline
# 빨강에서 초록, 파랑보드로 움직임
def move(b, si, sj):
    if b == 1:
        # 아래 두 보드에서 쓰이는 ci, cj 변수 안꼬이나 잘 보기
        # 파랑 보드
        ci, cj = si, sj
        for nj in range(6):
            if blue[nj][3-si] == 1: break
            cj = nj
        blue[cj][3-si] = 1
        # 초록 보드
        for ni in range(6):
            if green[ni][sj] == 1: break
            ci = ni
        green[ci][sj] = 1

    elif b == 2:  # 가로로 긴 것
        ci, cj = si, sj
        for nj in range(5):
            if blue[nj+1][3-si] == 1: break
            cj = nj
        blue[cj][3-si] = blue[cj+1][3-si] = 1
        for ni in range(6):
            if green[ni][sj] == 1 or green[ni][sj+1] == 1: break
            ci = ni
        green[ci][sj] = green[ci][sj+1] = 1
    else:  # 세로로 긴 것
        ci, cj = si, sj
        for nj in range(6):
            if blue[nj][3-si] == 1 or blue[nj][2-si] == 1: break
            cj = nj
        blue[cj][3-si] = blue[cj][2-si] = 1
        for ni in range(5):
            if green[ni+1][sj] == 1: break
            ci = ni
        green[ci][sj] = green[ci+1][sj] = 1


# 진한 초록, 파랑보드에 지워질 행/열이 있는 지
def check():
    # 초록 보드 순회
    global score
    for i in range(6):
        if sum(green[i]) == 4:  # 지워지고 윗칸이 아래로 내려옴
            score += 1
            for j in range(i, 0, -1):
                green[j] = green[j-1]
            green[0] = [0, 0, 0, 0]

    # 진한 파란 보드 순회
    for z in range(6):
        if sum(blue[z]) == 4:
            score += 1
            for k in range(z, 0, -1):
                blue[k] = blue[k - 1]
            blue[0] = [0, 0, 0, 0]


# 연한 부분 체크
def check_pastel():
    global green, blue
    # 초록 보드
    gc = 0
    for i in range(2):
        if 1 in green[i]: # 블록이 있으면
          gc += 1
    if gc == 1:
        green = [[0]*4] + green[:5]
    elif gc == 2:
        green = [[0]*4] + [[0]*4] + green[:4]

    # 파란 보드
    bc = 0
    for j in range(2):
        if 1 in blue[j]:
            bc += 1
    if bc == 1:
        blue = [[0] * 4] + blue[:5]
    elif bc == 2:
        blue = [[0] * 4] + [[0] * 4] + blue[:4]


# for _ in range(7):
n = int(input())
# infos = [list(map(int, input().split())) for _ in range(n)]

# 도미노판 구현- 파란 보드는 i, j 뒤집어서 생각하기
green = [[0]* 4 for _ in range(6)]
blue = [[0]* 4 for _ in range(6)]

score = 0
# 주어진 블럭 개수만큼 진행
for _ in range(n):
    b, si, sj = map(int, input().split())
    move(b, si, sj)
    check()
    check_pastel()

res = 0
for r in range(6):
    res += sum(green[r])
    res += sum(blue[r])
print(score, res, sep='\n')
