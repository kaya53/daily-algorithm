import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

# input
change = {0: [1, 3], 1: [2, 0], 2: [3, 1], 3: [0, 2]}
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# for _ in range(3):
n = int(input())  # 보드 크기
arr = [[0] * n for _ in range(n)]
k = int(input())  # 사과 개수
for _ in range(k):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 'a'
l = int(input())
infos = deque()
for _ in range(l):
    x, c = input().split()
    infos.append((int(x), c))


snake = deque()
snake.append((0, 0))  # 뱀 초기 위치
arr[0][0] = 1
direction = 3
time = 0
change_t, change_str = infos.popleft()

while True:
    time += 1
    head_i, head_j = snake[-1]  # 뱀의 머리 부분

    # 뱀이 스르륵
    ni, nj = head_i + delta[direction][0], head_j + delta[direction][1]
    # 인덱스 밖이거나 머리랑 꼬리가 부딪힌 경우
    if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 1: break
    snake.append((ni, nj))  # 머리 붙이기
    tmp = arr[ni][nj]
    arr[ni][nj] = 1
    if tmp != 'a':
        ii, jj = snake.popleft()  # 꼬리 떼기
        arr[ii][jj] = 0
    # else:  # 사과가 있는 경우
    #     arr[ni][nj] = 1

    # change_t가 끝난 이후에 회전시키는 것
    if time == change_t:  # 방향 전환을 할 시간이고, (infos가 있으면=> 이 조건을 여기에 넣으니까 마지막 info일 때 방향 전환을 못함)
        if change_str == 'L':
            direction = change[direction][0]
        elif change_str == 'D':
            direction = change[direction][1]
        if infos: change_t, change_str = infos.popleft()  # 다음 걸로 갱신, (그래서 infos가 있으면 빼주면 조건을 여기로 옮김

print(time)