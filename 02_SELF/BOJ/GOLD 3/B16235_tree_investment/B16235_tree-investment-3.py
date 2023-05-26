import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open('input.txt')


def ss():
    global tree_cnt

    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                dead = 0
                now_tree = sorted(trees[i][j].keys())
                now_dict = trees[i][j]
                now_nutri = nutrition[i][j]
                new_dict = {}
                for age in now_tree:
                    t_cnt = now_dict[age]
                    if now_nutri >= age*t_cnt:
                        now_nutri -= age*t_cnt
                        new_dict[age + 1] = t_cnt

                    else:
                        can_grow = now_nutri // age
                        will_dead = t_cnt - can_grow
                        if can_grow:
                            new_dict[age + 1] = can_grow
                        now_nutri -= age * can_grow
                        dead += ((age // 2) * will_dead)
                        tree_cnt -= will_dead
                nutrition[i][j] = dead + now_nutri
                trees[i][j] = new_dict


def fw():
    global tree_cnt

    for i in range(N):
        for j in range(N):
            nutrition[i][j] += given[i][j]
            if trees[i][j]:
                for tage in trees[i][j]:
                    amount = trees[i][j][tage]
                    if tage % 5 == 0:
                        for di, dj in delta:
                            ni, nj = i + di, j + dj
                            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                            next_tree = trees[ni][nj]
                            if next_tree.get(1): next_tree[1] += amount
                            else: next_tree[1] = amount
                            tree_cnt += amount


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
# for _ in range(8):
N, M, K = map(int, input().split())
given = [list(map(int, input().split())) for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]

trees = [[dict() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1][z] = 1

tree_cnt = M
for _ in range(K):
    ss()
    fw()

print(tree_cnt)