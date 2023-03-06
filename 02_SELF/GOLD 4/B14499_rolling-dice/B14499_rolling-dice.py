import sys

sys.stdin = open('input.txt')


def move(direction):
    global ci, cj
    if direction == 1:  # east
        # 지도 밖으로 나가면 걍 리턴
        cj += 1
        if ci < 0 or ci >= n or cj < 0 or cj >= n: return False
        
    elif direction == 2: # west
        cj -= 1
        if ci < 0 or ci >= n or cj < 0 or cj >= n: return False
    elif direction == 3:  # north
        ci -= 1
        if ci < 0 or ci >= n or cj < 0 or cj >= n: return False
    else:  # south
        ci += 1
        if ci < 0 or ci >= n or cj < 0 or cj >= n: return False


n, m, ci, cj, k = map(int, input().split())  # k: 명령의 개수
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
eastwest = [1, 3, 4]  # 서쪽은 그 반대로
northsouth = [1, 2, 6, 5]  # 남쪽은 그 반대로
top = 1

# 명령에 맞게 움직인다.
for d in order:
    res = move(d)
    if res:  # 좌표 밖인 경우는 출력도 안되도록
        print(res)