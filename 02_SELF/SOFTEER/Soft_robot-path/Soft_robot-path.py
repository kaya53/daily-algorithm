# 230804 287ms, 39mb => 2시간 소요
import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open('input.txt')

def choose_start():
    now_mmin = int(1e9)
    ri, rj, rd, r_order = -1, -1, -1, []
    for si, sj in can_start:
        for z in range(4):
            res = bfs(si, sj, z, now_mmin)
            if res:
                # print(res)
                ri, rj, rd, r_order = res
                if now_mmin > len(r_order): now_mmin = len(r_order)
    return ri, rj, rd, r_order


def bfs(si, sj, sd, mmin):
    q = deque([(si, sj, sd, 1, [], [(si, sj)])])

    time = -1
    while q:
        time += 1
        if time >= mmin: return False
        for _ in range(len(q)):
            ci, cj, cd, ccnt, order, visited = q.popleft()

            # 여러 번 돌아서 직진했을 때 어느 곳을 가는 것은 무조건 최적이 될 수 없다
            # 그래서 한번 돌았으면 그 다음에는 직진이 나오는 것이 무조건 최적이다
            # 4칸에 대해서 A가 있는 지 확인하면 시간 초과가 나온다
            if len(order) > 1 and 'A' not in order[-1:-3:-1]: continue
            if ccnt == total:
                return si, sj, sd, order

            for k in range(3):
                if k == 0:
                    bni, bnj = ci + delta[cd][0], cj + delta[cd][1]
                    ni, nj = ci + (2 * delta[cd][0]), cj + (2 * delta[cd][1])
                    if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                    if arr[bni][bnj] == '.' or arr[ni][nj] == '.': continue
                    if (bni, bnj) in visited or (ni, nj) in visited: continue
                    q.append((ni, nj, cd, ccnt + 2, order + ['A'], visited+[(bni, bnj), (ni, nj)]))
                elif k == 1:
                    if len(order):
                        q.append((ci, cj, (cd-1)%4, ccnt, order+['R'], visited + []))
                else:
                    if len(order):
                        q.append((ci, cj, (cd+1)%4, ccnt, order+['L'], visited + []))


delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
result_delta = ['^', '<', 'v', '>']
# for _ in range(2):
N, M = map(int, input().split())
arr = []
can_start = []
for i in range(N):
    inp = list(input())
    arr.append(inp)
    for j in range(M):
        if inp[j] == '#':
            can_start.append((i, j))

total = len(can_start)
ti, tj, td, t_order = choose_start()
print(ti+1, tj+1)
print(result_delta[td])
print(''.join(map(str, t_order)))
