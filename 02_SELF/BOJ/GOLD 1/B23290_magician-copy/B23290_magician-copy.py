import sys
from copy import deepcopy

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def move_fish():
    plus_ls = []
    moved_fish = {}
    for fish in fishes:
        fi, fj = fish
        for fd in fishes[fish]:
            ni, nj = fi + delta_8[fd][0], fj + delta_8[fd][1]
            std = fd  # 비교를 위한 변수
            # flag = False
            # 이 부분 for문으로 여덟번만 하도록 해도 됨
            while (ni < 0 or ni >= 4 or nj < 0 or nj >= 4) or ((ni, nj) == shark) or smell[ni][nj]:
                fd = (fd - 1) % 8
                ni, nj = fi + delta_8[fd][0], fj + delta_8[fd][1]
                if fd == std: # 이동할 곳이 없는 경우
                    plus_ls.append((fi, fj, std))
                    break
            else:  # 이동할 곳이 있는 경우
                plus_ls.append((ni, nj, fd))
    for pi, pj, pd in plus_ls:
        if moved_fish.get((pi, pj), -1) == -1:
            moved_fish[(pi, pj)] = [pd]
        else:  # 이동한 곳에 이미 물고기 존재
            moved_fish[(pi, pj)].append(pd)
    return moved_fish


def move_shark(now_fishes):
    global mmax, shark
    max_d = {}
    max_smell_ls = []
    next_shi, next_shj = shark
    shi, shj = shark
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                i1, j1 = shi + delta_4[d1][0], shj + delta_4[d1][1]
                if i1 < 0 or i1 >= 4 or j1 < 0 or j1 >= 4: continue
                i2, j2 = i1 + delta_4[d2][0], j1 + delta_4[d2][1]
                if i2 < 0 or i2 >= 4 or j2 < 0 or j2 >= 4: continue
                i3, j3 = i2 + delta_4[d3][0], j2 + delta_4[d3][1]
                if i3 < 0 or i3 >= 4 or j3 < 0 or j3 >= 4: continue

                now_killed, now_dict, now_smell_ls = out_and_smell(deepcopy(now_fishes), [(i1, j1), (i2, j2), (i3, j3)])
                if mmax < now_killed:
                    mmax = now_killed
                    max_d = now_dict
                    max_smell_ls = now_smell_ls
                    next_shi, next_shj = i3, j3
    # 상어 움직이기
    shark = (next_shi, next_shj)
    # 냄새 퍼트리기
    for smi, smj in max_smell_ls:
        smell[smi][smj] = 3
    return max_d


def out_and_smell(now_fishes, path_ls):

    killed = 0  # 격자 밖으로 나간 물고기
    remove_ls = set()
    smell_ls = []
    for pi, pj in path_ls:
        if (pi, pj) in now_fishes:
            # smell[pi][pj] = 2  # 2번 후에 냄새가 빠지니까
            smell_ls.append((pi, pj))
            remove_ls.add((pi, pj))
    for ri, rj in remove_ls:
        killed += len(now_fishes.pop((ri, rj)))

    return killed, now_fishes, smell_ls


def smell_minus():
    for i in range(4):
        for j in range(4):
            if smell[i][j]: smell[i][j] -= 1


def copy_fishes(turn_fishes):
    for tfish in turn_fishes:
        td_ls = turn_fishes[tfish]
        # print(tfish, td)
        if fishes.get(tfish, -1) == -1:
            fishes[tfish] = td_ls
        else:
            fishes[tfish] += td_ls


delta_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
delta_8 = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# for _ in range(8):
M, S = map(int, input().split())
fishes = {}
for _ in range(M):
    # x, y, d = map(lambda x:x-1, map(int, input().split()))
    x, y, d = map(lambda x: int(x)-1, input().split())
    if fishes.get((x, y), -1) == -1:
        fishes[(x, y)] = [d]
    else:
        fishes[(x, y)] += [d]
# shark = tuple(map(lambda x:x-1, map(int, input().split())))
shark = tuple(map(lambda x : int(x)-1, input().split()))


smell = [[0] * 4 for _ in range(4)]
for _ in range(S):
    mmax = -1  # 여기를 0으로 하면 max 값이 0인 경우는 제외된다
    now_fishes = move_fish()  # 현재 턴에서 사용할 물고기의 딕셔너리
    now_fishes = move_shark(now_fishes)
    smell_minus()
    copy_fishes(now_fishes)
res = 0
for f in fishes.values():
    res += len(f)
print(res)
