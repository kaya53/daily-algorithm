import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

def control_smell(smell):
    pop_ls = []
    for sm in smell:
        smell[sm][1] += 1
        if smell[sm][1] >= k: pop_ls.append(sm)  # 냄새 사라짐
    for p in pop_ls:  # 이렇게 안하면 중간에 딕셔너리 크기가 바뀌어서 에러 남
        smell.pop(p)
    return smell


def spread_smell(smell):
    for num in shark:
        shi, shj = shark[num][0], shark[num][1]
        # 냄새가 원래 존재하든 안하든 그냥 이렇게 해주면 됨
        smell[(shi, shj)] = [num, 0]
    return smell


def move_shark(smell):
    candidate = [[] for _ in range(m)]  # 상어가 이동할 후보 좌표 담아두기
    for sh_no in shark:
        si, sj, now_d = shark[sh_no]
        now_delta = delta[sh_no][now_d]
        # print(sh_no, shark[sh_no], now_delta)
        for d in now_delta:
            ni, nj = si + dir_ls[d][0], sj + dir_ls[d][1]
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            if smell.get((ni, nj), -1) == -1:  # 냄새가 없는 칸
                candidate[sh_no] = (ni, nj, d)
                break
            else:
                if candidate[sh_no]: continue
                if smell[(ni, nj)][0] == sh_no:
                    candidate[sh_no] = (ni, nj, d)
    # 상어 옮기기 => 여러 상어가 1칸에 있으면 숫자가 작은 상어만 남기고 없애기
    new_shark = {}
    for k in range(m):
        if not candidate[k]: continue
        ii, jj, d = candidate[k]
        if new_shark.get((ii, jj), -1) == -1:  # 겹치는 상어가 없는 경우
            shark[k] = candidate[k]
            new_shark[(ii, jj)] = k
        else:
            if new_shark[(ii, jj)] > k:  # 지금 들어온 상어가 더 작으면
                before = new_shark[(ii, jj)]
                shark[k] = candidate[k]
                shark.pop(before)  # 원래 상어 없애기
                new_shark[(ii, jj)] = k
            else:  # 지금 들어온 상어가 더 크면 지금 들어온 애는 상어에서 빼준다.
                shark.pop(k)
    

def solve():
    move = 0
    smell = {}  # (ci, cj) : (shark_no, time)
    while True:
        # 종료 조건
        if move > 1000:
            # print(shark)
            return -1
        # 1번 상어만 남아 있으면 끝
        # if len(shark) == 1 and shark.get(0, -1) != -1:
        if len(shark) == 1:  # 이렇게만 해줘도 됨
            # print(shark)
            return move

        # 1. 자신의 위치에 냄새 뿌리기
        smell = spread_smell(smell)
        # 2. 상어가 1칸씩 이동 => 한 칸
        move_shark(smell)
        move += 1
        # 3. 한 칸 이동했으면 냄새 + 1하고 k가 지난 건 사라지게
        smell = control_smell(smell)


# start
n, m, k = map(int, input().split())  # 격자 크기, 상어 수, 냄새가 사라지는 이동 횟수
shark = {}
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(n):
        if inp[j]:
            shark[inp[j]-1] = [i, j]

di = list(map(int, input().split()))
for v in range(m):
    shark[v].append(di[v]-1)


# 각 상어번호와 그 방향에 따른 방향 우선 순위
dir_ls = [(-1, 0), (1, 0), (0, -1), (0, 1)]
delta = [[[] for _ in range(4)] for _ in range(m)]
for no in range(m):
    for dd in range(4):
        inp = list(map(lambda x: x-1, map(int, input().split())))
        delta[no][dd] = inp

print(solve())

