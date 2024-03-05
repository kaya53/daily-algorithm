# pypy 860ms
# 가능한 자리 조합을 모두 구한 후 그 자리들이 연결되어 있는 지 본다
import sys

sys.stdin = open('input.txt')

from collections import deque


def is_connected(choice):
    # try:
    for i in range(7):
        choice[i] = divmod(choice[i], 5)
    # except: print(choice)
    q = deque([choice[0]])
    visited = [choice[0]]

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= 5 or nj < 0 or nj >= 5 or (ni, nj) in visited: continue
            if (ni, nj) not in choice: continue
            visited.append((ni, nj))
            q.append((ni, nj))
    if len(visited) == 7: return True
    return False


def backtrack(depth, ci, s_cnt, choice, board):
    global answer

    if depth == 7:
        if s_cnt >= 4 and is_connected(choice[:]):
            answer += 1
        return

    for ni in range(ci+1, 25):
        if choice[depth] > -1: continue
        r, c = divmod(ni, 5)
        choice[depth] = ni
        backtrack(depth+1, ni, s_cnt+1 if board[r][c]=='S' else s_cnt, choice, board)
        choice[depth] = -1


def solution(board):
    backtrack(0, -1, 0, [-1]*7, board)


answer = 0
solution([list(input().rstrip()) for _ in range(5)])
print(answer)