# 230523 python 104ms => sys.stdin.readline 안하면 528ms
# 주의할 점
# 1. 블럭 놓을 때 인덱스 에러
# 2. 블럭이 사라져서 빈 블럭이 내려올 때 배열 복사 주의
import sys

sys.stdin = open('input.txt')


def put_zero(ci, cj):
    # 초록 보드 시작점
    gi, gj = 0, cj
    while gi < 5 and green[gi+1][gj] == 0:
        gi += 1
    green[gi][gj] = 1
    # 파랑 보드 시작점
    bi, bj = 0, ci
    while bi < 5 and blue[bi+1][bj] == 0:
        bi += 1
    blue[bi][bj] = 1


def put_one(ci, cj):
    # 초록
    gi, gj = 0, cj
    while gi < 5 and (green[gi+1][gj] == 0 and green[gi+1][gj+1] == 0):
        gi += 1
    green[gi][gj] = green[gi][gj+1] = 1
    
    # 파랑
    bi, bj = 1, ci
    while bi < 5 and blue[bi+1][bj] == 0:
        bi += 1
    blue[bi-1][bj] = blue[bi][bj] = 1


def put_two(ci, cj):
    # 초록
    gi, gj = 1, cj
    while gi < 5 and green[gi+1][gj] == 0:
        gi += 1
    green[gi-1][gj] = green[gi][gj] = 1

    # 파랑
    bi, bj = 0, ci
    while bi < 5 and (blue[bi+1][bj] == 0 and blue[bi+1][bj+1] == 0):
        bi += 1
    blue[bi][bj] = blue[bi][bj+1] = 1


def get_score():
    global green, blue

    cnt = 0
    # 초록
    for gi in range(6):
        if sum(green[gi]) == 4:
            green = [[0]*4] + green[:gi] + green[gi+1:]
            cnt += 1

    # 파랑
    for bi in range(6):
        if sum(blue[bi]) == 4:
            blue = [[0]*4] + blue[:bi] + blue[bi+1:]
            cnt += 1

    return cnt


# 연한 부분의 수만큼 아래 행이 사라짐
def remove_pastel():
    global green, blue

    # 초록
    g_cnt = 0
    for gi in range(2):
        for gb in green[gi]:
            if gb:
                g_cnt += 1
                break
    green = [[0]*4 for _ in range(g_cnt)] + green[:6-g_cnt]

    # 파랑
    b_cnt = 0
    for bi in range(2):
        for bb in blue[bi]:
            if bb:
                b_cnt += 1
                break
    blue = [[0]*4 for _ in range(b_cnt)] + blue[:6-b_cnt]
    # print(g_cnt, b_cnt)


# for _ in range(7):
N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
zeros = [0]*4

score = 0
for _ in range(N):
    block, si, sj = map(int, input().split())
    if block == 1: put_zero(si, sj)
    elif block == 2: put_one(si, sj)
    elif block == 3: put_two(si, sj)

    score += get_score()  # 윗 행부터 순회하면서 보기
    remove_pastel()

# output
ssum = 0
for gl in green:
    ssum += sum(gl)
for bl in blue:
    ssum += sum(bl)
print(score, ssum, sep='\n')
