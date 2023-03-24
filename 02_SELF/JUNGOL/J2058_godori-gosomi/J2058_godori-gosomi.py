import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline


def check(bi, bj, gi, gj, s):
    ls = []
    for di, dj in delta:
        nbi, nbj = bi + di, bj + dj
        # 인덱스 밖, 웅덩이, 고돌이가 방문한 적 있으면 건너뛰기
        if nbi < 0 or nbi >= n or nbj < 0 or nbj >= n or arr[nbi][nbj] or visited[nbi][nbj][0]: continue

        for ddi, ddj in delta:
            ngi, ngj = gi + ddi, gj + ddj
            if ngi < 0 or ngi >= n or ngj < 0 or ngj >= n: continue
            if arr[ngi][ngj] or visited[ngi][ngj][1]: continue
            flag = False
            for tdi, tdj in delta:  # 고소미가 움직인 8방향 내에 있는 지 없는 지
                if (ngi == nbi and ngj == nbj) or (ngi + tdi == nbi and ngj + tdj == nbj):
                    flag = True
                    break
            if not flag:
                if s == '0':
                    ls.append((bi, bj, ngi, ngj))
                    visited[ngi][ngj][1] = 1
                elif s == '1':
                    ls.append((nbi, nbj, gi, gj))
                    visited[nbi][nbj][0] = 1
                elif s == '2':
                    ls.append((nbi, nbj, ngi, ngj))
                    visited[nbi][nbj][0] = visited[ngi][ngj][1] = 1

    return ls


def bfs(q):
    time = 0
    godori = gosomi = False
    while q:
        time += 1
        for _ in range(len(q)):
            bi, bj, gi, gj = q.popleft()

            if bi == ebi and bj == ebj:
                godori = True
            if gi == egi and gj == egj:
                gosomi = True

            if godori and gosomi:
                print('all', time)
                return

            if not godori and not gosomi:
                ls = check(bi, bj, gi, gj, '2')
            elif not godori and gosomi:  # 고소미는 도착
                ls = check(bi, bj, egi, egj, '1')
            elif godori and not gosomi:  # 고돌이는 도착
                ls = check(ebi, ebj, gi, gj, '0')
            q += ls

    return -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
n = int(input())
sbi, sbj, ebi, ebj = map(lambda x: x-1, map(int, input().split()))
sgi, sgj, egi, egj = map(lambda x: x-1, map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0, 0] for _ in range(n)] for _ in range(n)]

q = deque()
q.append((sbi, sbj, sgi, sgj))
visited[sbi][sbj][0] = visited[sgi][sgj][1] = 1
res = bfs(q)
# print(res)