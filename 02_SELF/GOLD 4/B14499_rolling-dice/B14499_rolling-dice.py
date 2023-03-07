import sys

sys.stdin = open('input.txt')


from collections import deque


def move(direction, arr, eastwest, northsouth, dice):
    global ci, cj  # 주사위의 지도 상 위치
    if direction == 1:  # east
        cj += 1
        if ci < 0 or ci >= n or cj < 0 or cj >= m:
            cj -= 1
            return -1
        popped = eastwest.pop()
        eastwest.appendleft(popped)
        northsouth[0] = eastwest[0] # ns 배열도 윗면 갱신
        northsouth[2], eastwest[2] = eastwest[2],  northsouth[2]

    elif direction == 2:
        cj -= 1
        if ci < 0 or ci >= n or cj < 0 or cj >= m:
            cj += 1
            return -1
        popped = eastwest.popleft()
        eastwest.append(popped)
        northsouth[0] = eastwest[0]
        northsouth[2], eastwest[1] = eastwest[1], northsouth[2]

    elif direction == 3:
        ci -= 1
        if ci < 0 or ci >= n or cj < 0 or cj >= m:
            ci += 1
            return -1
        popped = northsouth.popleft()
        northsouth.append(popped)
        eastwest[0] = northsouth[0]

    else:
        ci += 1
        if ci < 0 or ci >= n or cj < 0 or cj >= m:
            ci -= 1
            return -1
        popped = northsouth.pop()
        northsouth.appendleft(popped)
        eastwest[0] = northsouth[0]

    next_top = eastwest[0]
    if not arr[ci][cj]:
        arr[ci][cj] = dice[7-next_top]
    else:
        dice[7-next_top] = arr[ci][cj]
        arr[ci][cj] = 0

    return dice[eastwest[0]]


# for _ in range(4):
n, m, ci, cj, k = map(int, input().split())  # k: 명령의 개수
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
eastwest = deque([1, 3, 4])  # 서쪽은 그 반대로
northsouth = deque([1, 5, 6, 2])  # 남쪽은 그 반대로; 1, 5, 6, 2
dice = [0] * 7  # 주사위에 적혀있는 숫자; 인덱스는 1부터 보기
# std = 1

# 명령에 맞게 움직인다.
for d in order:
    # if d == 1:
    res = move(d, arr, eastwest, northsouth, dice)
    if res != -1:  # 좌표 밖인 경우는 출력도 안되도록
        print(res)
