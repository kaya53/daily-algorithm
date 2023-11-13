# 소요시간 24분 python 1364ms, pypy 420ms
# 문제를 잘 이해해야 하는 문제
# 길을 반드시 건너야만 만날 수 있는 소들이 몇 쌍인지
# => 길을 안건너고 상하좌우 인접한 곳으로 뻗어나가서 만날 수 있는 소의 쌍을 빼면 됨
# 길은 상하좌우 인접한 격자 사이에 나있음
import sys

sys.stdin = open('input.txt')


from collections import deque


def bfs(idx, si, sj, N, K, road, cows):
    q = deque([(si, sj)])
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            # 길이 있는 곳 pass
            if road.get((ci, cj)) and (ni, nj) in road[(ci, cj)]: continue
            # 가다가 다른 소를 만나면 cnt + 1 하기
            for k in range(idx+1, K):
                if (ni, nj) == cows[k]: cnt += 1
            q.append((ni, nj))
            visited[ni][nj] = 1
    return cnt


def solution():
    N, K, R = map(int, input().split())
    road = {}
    for _ in range(R):
        sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
        if road.get((sr, sc), -1) == -1:
            road[(sr, sc)] = [(er, ec)]
        else: road[(sr, sc)].append((er, ec))
        if road.get((er, ec), -1) == -1:
            road[(er, ec)] = [(sr, sc)]
        else: road[(er, ec)].append((sr, sc))

    cows = []
    for _ in range(K):
        coi, coj = map(lambda x: int(x)-1, input().split())
        cows.append((coi, coj))

    answer = (K*(K-1)) // 2
    for idx, cop in enumerate(cows):
        ci, cj = cop
        r = bfs(idx, ci, cj, N, K, road, cows)
        answer -= r
    return answer


print(solution())
