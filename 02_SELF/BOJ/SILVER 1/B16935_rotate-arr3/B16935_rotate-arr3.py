import sys

sys.stdin = open('input.txt')

# 연산 1. 상하 반전
def up_and_down(arr):
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

# 연산 2. 좌우 반전
def left_and_right(arr):
    for j in range(m // 2):
        for i in range(n):
            arr[i][j], arr[i][m - j - 1] = arr[i][m - j - 1], arr[i][j]
    return arr

# 연산 3. 오른쪽으로 90도 회전
def right_90(arr):
    flipped = list(zip(*arr))
    for idx, elem in enumerate(flipped):
        flipped[idx] = list(elem)[::-1]
    return flipped

# 연산 4. 왼쪽으로 90도 회전
def left_90(arr):
    return list(map(list, zip(*map(reversed, arr))))  # 내부 각 요소가 튜플이어서 list로 바꿔줌

def clockwise(arr):
    new_arr = [[0] * m for _ in range(n)]
    ki, kj = n // 2, m // 2
    start = [(0, 0), (0, kj), (ki, kj), (ki, 0)]
    dir_ls = [(0, kj), (ki, 0), (0, -kj), (-ki, 0)]
    for k in range(4):
        si, sj = start[k]
        di, dj = dir_ls[k]
        for i in range(ki):
            for j in range(kj):
                new_arr[si+i+di][sj+j+dj] = arr[si+i][sj+j]
    return new_arr


def counter_clockwise(arr):
    new_arr = [[0] * m for _ in range(n)]
    ki, kj = n // 2, m // 2
    dir_ls = [(ki, 0), (0, -kj), (-ki, 0), (0, kj)]
    start = [(0, 0), (0, kj), (ki, kj), (ki, 0)]
    for k in range(4):
        si, sj = start[k]
        di, dj = dir_ls[k]
        for i in range(ki):
            for j in range(kj):
                new_arr[si + i + di][sj + j + dj] = arr[si + i][sj + j]
    return new_arr


# for _ in range(7):
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
infos = list(map(int, input().split()))  # 어떤 연산을 할 지에 대한 정보

for info in infos:
    if info == 1:
        arr = up_and_down(arr)
    elif info == 2:
        arr = left_and_right(arr)
    elif info == 3:
        arr = right_90(arr)
    elif info == 4:
        arr = left_90(arr)
    elif info == 5:
        arr = clockwise(arr)
    else:
        arr = counter_clockwise(arr)
    # n, m이 다르면 가로, 세로 길이가 바뀌기 때문에 매 턴이 끝날 때마다 가로, 세로 길이를 갱신해줘야 함
    n = len(arr)
    m = len(arr[0])

for elem in arr:
    print(' '.join(map(str, elem)))