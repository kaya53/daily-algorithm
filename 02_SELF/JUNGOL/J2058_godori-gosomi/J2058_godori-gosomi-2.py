import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline


def check(bi, bj, gi, gj, q, visited):
    if bi < 0 or bi >= n or bj < 0 or bj >= n: return
    if gi < 0 or gi >= n or gj < 0 or gj >= n: return
    if arr[bi][bj] or arr[gi][gj] or visited[bi][bj][gi][gj]: return

    if abs(bi-gi) <= 1 and abs(bj-gj) <= 1: return
    q.append((bi, bj, gi, gj))
    visited[bi][bj][gi][gj] = 1


def bfs(q, visited):
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            bi, bj, gi, gj = q.popleft()

            if (bi == ebi and bj == ebj) and (gi == egi and gj == egj):
                # print('all', time)
                return time

            for i in range(9):
                for j in range(9):
                    check(bi+delta[i][0], bj+delta[i][1], gi+delta[j][0], gj+delta[j][1], q, visited)

    return -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
# for _ in range(2):
n = int(input())
sbi, sbj, ebi, ebj = map(lambda x: x-1, map(int, input().split()))
sgi, sgj, egi, egj = map(lambda x: x-1, map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
q = deque()
q.append((sbi, sbj, sgi, sgj))
visited[sbi][sbj][sgi][sgj] = 1
res = bfs(q, visited)
print(res)

# for v in visited:
#     for c in v:
#         print(c)