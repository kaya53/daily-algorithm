import sys
from copy import deepcopy

# sys.stdin = open('input.txt')
input = sys.stdin.readline



def shoot_enemy(mtx, choice, num, enemies):
    # 0. 적을 배치한다.
    for en in en_dict:
        if not en_dict[en]: continue
        mtx[en_dict[en][0]][en_dict[en][1]] = en
    # for xx in mtx:
    #     print(xx)
    # print()
    turn_cnt = 0
    while num > 0:
        # 1. 거리를 측정해 죽일 적을 고른다
        killed = [0] * 3
        # print(enemies)

        for z in range(3):  # choice 불변
            pi, pj = choice[z]
            min_dist = d+1
            min_loc = (n, m)
            for no in enemies:  # en_dict 변함
                if not enemies[no]: continue
                ei, ej = enemies[no]
                dist = abs(pi - ei) + abs(pj - ej)
                if dist > d: continue
                if min_dist > dist:
                    min_dist = dist
                    min_loc = (ei, ej)
                elif min_dist == dist and min_loc[1] > ej:
                    min_loc = (ei, ej)
            if min_loc != (n, m):
                killed[z] = min_loc

        # 2. 공격한다.
        for ki in killed:
            if not ki: continue
            ii, jj = ki
            if mtx[ii][jj]: # 아직 안죽었으면
                enemies[mtx[ii][jj]] = 0
                mtx[ii][jj] = 0
                turn_cnt += 1
                num -= 1

        # 3. 적이 남하한다. - 남하하다가 가장 n행으로 가면 또 죽음; 여기서 제대로 남하가 안됨
        tmp = mtx[n]
        for t in mtx[n-1]:
            if t:
                enemies[t] = 0
                num -= 1

        # print(tmp)
        mtx = [[0]*m] + mtx[:n-1] + [tmp]
        # for mm in mtx:
        #     print(mm)

        for ci in range(n):
            for cj in range(m):
                if mtx[ci][cj]:
                    enemies[mtx[ci][cj]] = (ci, cj)
        # print(enemies)
    return turn_cnt



def comb(idx, si, enemy, mtx):
    global mmax
    if idx == 3:
        ccnt = shoot_enemy(mtx, choice, enemy, deepcopy(en_dict))
        if mmax < ccnt:
            mmax = ccnt
        return

    for i in range(si, m):
        mtx[n][i] = -3
        choice[idx] = (n, i)
        comb(idx+1, i+1, enemy, mtx)
        mtx[n][i] = -2
        choice[idx] = 0


# for _ in range(10):
n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] + [[-2]*m]

# 적의 수 세기
enemy = 0
en_dict = {}
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            enemy += 1
            en_dict[enemy] = (i, j)

mmax = 0
choice = [0] * 3
comb(0, 0, enemy, arr)
print(mmax)
