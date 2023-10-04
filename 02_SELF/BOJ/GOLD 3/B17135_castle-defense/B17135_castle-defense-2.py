# 소요시간 1시간 pypy 400ms
import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline


def comb(depth, cj, ls, n, m, d, arr):
    global answer
    if depth == 3:
        # print(ls)
        cnt = attack(ls, [a[:] for a in arr], n, m, d)
        if answer < cnt:
            answer = cnt
        return
    for nj in range(cj, m):
        if (n, nj) in ls: continue
        comb(depth+1, nj+1, ls+[(n, nj)], n, m, d, arr)


def attack(ls, board, n, m, d):
    cnt = 0
    while True:
        enemies = find_enemies(board, n, m)
        if not enemies: return cnt
        attack_ls = []
        for li, lj in ls:  # 궁수들
            dist = [0] * len(enemies)
            mmin = 50
            for k in range(len(enemies)):
                ei, ej = enemies[k]
                now = abs(ei-li) + abs(ej-lj)
                if now <= d:
                    dist[k] = now
                    if mmin > now: mmin = now
            if mmin != 50:
                attack_ls.append(enemies[dist.index(mmin)])

        # 공격하기
        for ai, aj in attack_ls:
            if board[ai][aj]:  # 중복으로 세지는 것 방지
                board[ai][aj] = 0
                cnt += 1
        # 나머지 남하
        board = [[0] * m] + board[:n-1]


def find_enemies(arr, n, m):
    enemies = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                enemies.append((i, j))
    return sorted(enemies, key=lambda x: x[1])


def solution():
    n, m, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    comb(0, 0, [], n, m, d, arr)


# for _ in range(6):
answer = 0
solution()
print(answer)