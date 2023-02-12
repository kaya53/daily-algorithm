import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs():
    while q:
        now, dir = q.popleft()

        visited[now] = 1  # 다 돌리고 방문 표시
        if dir == -1:  # 반시계 방향
            wheels[now] = wheels[now][1:] + [wheels[now][0]]
        elif dir == 1:  # 시계 방향
            wheels[now] = [wheels[now][-1]] + wheels[now][:7]

        # 다음 돌릴 애들 추가
        for elem in graph[now]:
            if dir and not visited[elem]:
                if elem > now:
                    next_dir = can_rotate[now]
                else:
                    next_dir = can_rotate[elem]
                if next_dir:  # 두 바퀴의 맞닿은 극이 다르다는 의미
                    q.append((elem, dir * (-1)))


# for _ in range(4):
wheels =[[0]] + [list(map(int, input())) for _ in range(4)]
K = int(input())  # 회전 횟수
rotate_info = [tuple(map(int, input().split())) for _ in range(K)]
graph = [0, [2], [1,3], [2,4], [3]]  # 톱니 간 연결 상태 표현


for i in range(K):  # 회전 한 사이클
    # 어느 바퀴들이 극이 서로 같고 다른지
    can_rotate = [False] * 4  # 매 턴마다 이 부분을 초기화를 해줘야 하는데 하지 않아서 틀렸음
    if wheels[1][2] != wheels[2][6]: can_rotate[1] = True
    if wheels[2][2] != wheels[3][6]: can_rotate[2] = True
    if wheels[3][2] != wheels[4][6]: can_rotate[3] = True

    # 돌리기
    visited = [0] * 5  # 해당 톱니바퀴를 돌렸는 지 보기 위해
    q = deque()
    q.append(rotate_info[i])
    bfs()

res = 0
for i in range(1, 5):
    if wheels[i][0] == 1:
        res += 2**(i-1)
print(res)