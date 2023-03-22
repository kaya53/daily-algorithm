import sys

sys.stdin = open('input.txt')

from collections import deque
import heapq

n = int(input())  # 공간의 크기
arr = [list(map(int, input().split())) for _ in range(n)]  # arr[i][j][0]: 공간의 상태, arr[i][j][1]: 방문 표시
visited = [[-1] * n for _ in range(n)]
    
shark = 2  # 아기 상어의 원래 크기는 2임
# 상어 초기 위치 찾기
si = sj = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i, j
            visited[i][j] = 0  # 초기 위치 방문 표시

# time = 0
# 거리, 상어 출발 위치, 도착 위치
q = deque([[0, si, sj]])
fish = []  # heapq 사용
while q:
    # time += 1  # 시간 경과
    dist, ci, cj = q.popleft()

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = ci + di, cj + dj
        # 인덱스 밖, 방문한 적이 있으면 continue;
        # 크기가 같은 경우는 방문 표시 x
        # 크기가 큰 경우는 큐에 넣지 말기
        if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
        if not visited[ni][nj] and arr[ni][nj]:
            q.append((dist + 1, ni, nj))
        if 0 < arr[ni][nj] < shark:  # 지나갈 수 있는 곳
            heapq.heappush(fish, (dist+1, ni, nj))
            visited[ni][nj] = dist+1



# time - 1
for elem in arr:
    print(elem)
