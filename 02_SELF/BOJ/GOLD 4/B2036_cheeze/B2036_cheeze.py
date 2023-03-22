import sys

sys.stdin = open('input.txt')

from collections import deque


def find_air(si, sj):
    q = deque([(si, sj)])
    arr[si][sj] = 2
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if not arr[ni][nj]:
                arr[ni][nj] = 2  # 공기 부분임을 표시; 구멍이랑 구분하기 위해 2로 일단 세워 놓음
                q.append((ni, nj))
            

def check():
    global cheeze
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            # 사방이 1로 둘러싸인 치즈 -> 다음 턴에 남아 있는 칸이 있으므로 진행해야 함
            if arr[i][j] == 1: 
                if arr[i+1][j] + arr[i-1][j] + arr[i][j+1] + arr[i][j-1] == 4:
                    return False
                else:  # 사방에 0이 최소한 1개는 존재하는 상태
                    cheeze += 1
    return True


n, m = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
# 아래는 한 시간에 일어나는 일
time = 0
while True:
    # 4. 다 없어지기 직전인지 체크 -- 여기를 가장 처음에 놓아야 1시간 지나면 다 녹는 판을 판별해 낼 수 있다.
    cheeze = 0
    if check(): break

    time += 1  # 이번 판에 다 녹지 않으면 시간 늘리기 시작
    # 1. 순회하면서 바깥의 공기부분만 찾기 - bfs로 찾기
    find_air(0, 0)

    # 2. 2인 부분을 순회하면서 근처에 1이 있으면 그 1을 녹일 칸에 넣어준다.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                    if arr[ni][nj] == 1:
                        arr[ni][nj] = 0  # 녹이기
    # 3. 2로 바꿨던 공기를 다시 0으로 바꿔준다.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2: arr[i][j] = 0


print(time+1)
print(cheeze)
