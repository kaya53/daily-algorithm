import sys

sys.stdin = open('input.txt')


def move(direction, top):
    global ci, cj
    top_idx = next_idx = eastwest.index(top)  # 주사위 인덱스 탐색
    if direction < 3:
        if direction == 1:
            # 지도 밖으로 나가면 걍 리턴
            cj += 1
            if ci < 0 or ci >= n or cj < 0 or cj >= n: return -1
            # 인덱스 내부
            next_idx = (top_idx + 1) % 3
        elif direction == 2:  # west
            cj -= 1
            if ci < 0 or ci >= n or cj < 0 or cj >= n: return -1
            next_idx = (top_idx - 1) % 3
        if not arr[ci][cj]:
            arr[ci][cj] = dice[7 - eastwest[next_idx]]
        else:
            dice[7 - eastwest[next_idx]] = arr[ci][cj]
            arr[ci][cj] = 0
        return dice[eastwest[next_idx]]

    if 2 < direction < 5:
        if direction == 3:  # north
            ci -= 1
            if ci < 0 or ci >= n or cj < 0 or cj >= n: return -1
            next_idx = (top_idx + 1) % 4
        elif direction == 4:  # south
            ci += 1
            if ci < 0 or ci >= n or cj < 0 or cj >= n: return -1
            next_idx = (top_idx - 1) % 4

        if not arr[ci][cj]:
            arr[ci][cj] = dice[7 - northsouth[next_idx]]
        else:
            dice[7 - northsouth[next_idx]] = arr[ci][cj]
            arr[ci][cj] = 0
        return dice[northsouth[next_idx]]


n, m, ci, cj, k = map(int, input().split())  # k: 명령의 개수
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
eastwest = [1, 3, 4]  # 서쪽은 그 반대로
northsouth = [1, 2, 6, 5]  # 남쪽은 그 반대로
dice = [0] * 7  # 주사위에 적혀있는 숫자; 인덱스는 1부터 보기
# top = 1

# 명령에 맞게 움직인다.
for d in order:
    # if d == 1:
    res = move(d, 1)
    if res != -1:  # 좌표 밖인 경우는 출력도 안되도록
        print(res)
