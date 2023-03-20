import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

def bfs(q):
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            now_no = q.popleft()
            si, sj, ei, ej = bus_info[now_no]  # 현재 버스가 갈 수 있는 구간

            if now_no in end_no: return cnt

            for next_no in range(1, k+1):
                if next_no in visited: continue  # 이렇게 가면 최소가 아님
                nsi, nsj, nei, nej = bus_info[next_no]
                if (nsi <= ei <= nei or si <= nei <= ei) and (nsj <= ej <= nej or sj <= nej <= ej):
                    visited.add(next_no)
                    q.append(next_no)


c, r = map(int, input().split())
k = int(input())
bus_info = [[] for _ in range(k+1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    if y1 > y2: y1, y2 = y2, y1
    if x1 > x2: x1, x2 = x2, x1
    bus_info[b] = [y1, x1, y2, x2]
# print(bus_info)

sj, si, ej, ei = map(int, input().split())

end_no = set()
visited = set()
q = deque()
for no in range(1, k+1):
    bsi, bsj, bei, bej = bus_info[no]
    if bsi <= si <= bei and bsj <= sj <= bej:  # 출발지의 좌표가 어떤 버스의 경로와 겹치면 큐에 넣기
        q.append(no)
        visited.add(no)
    if bsi <= ei <= bei and bsj <= ej <= bej:  # 도착지의 좌표가 어떤 버스의 경로와 겹치면 큐에 넣기
        end_no.add(no)

print(bfs(q))
