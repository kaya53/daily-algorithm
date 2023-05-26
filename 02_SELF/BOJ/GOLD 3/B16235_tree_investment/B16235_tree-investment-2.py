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
                while trees[i][j]:
                    size = len(trees[i][j])
                    for _ in range(size):
                        tage = trees[i][j].pop()
                        if nutrition[i][j] >= tage:
                            nutrition[i][j] -= tage
                            trees[i][j].appendleft(tage+1)
                        else:
                            dead += int(tage/2)
                            tree_cnt -= 1
                    break
                nutrition[i][j] += dead


def fw():
    global tree_cnt

    for i in range(N):
        for j in range(N):
            nutrition[i][j] += given[i][j]
            if trees[i][j]:
                for tage in trees[i][j]:
                    if tage % 5 == 0:
                        for di, dj in delta:
                            ni, nj = i + di, j + dj
                            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                            trees[ni][nj].append(1)
                            tree_cnt += 1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
# for _ in range(8):
N, M, K = map(int, input().split())
given = [list(map(int, input().split())) for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

tree_cnt = M
for _ in range(K):
    ss()
    fw()

print(tree_cnt)