import sys

sys.stdin =  open('input.txt')


def move(si, sj, res):
    cnt = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = si + di, sj + dj
        # 인덱스 밖, 이미 방문한 곳, 차이가 1이 아닌 경우는 갈 수 없음
        if ni < 0 or ni >= n or nj < 0 or nj >= n or (arr[ni][nj] - arr[si][sj] != 1):
            cnt += 1
            continue
        # 갈 수 있는 칸
        move(ni, nj, res+1)
    if cnt == 4:  # 4방향 어디도 갈데가 없으면
        ls.append((res, arr[ci][cj]))
        return
        

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ls = []
    for i in range(n):
        for j in range(n):
            # visited를 굳이 둘 필요가 없음
            # 모든 방 번호가 다르고, 두 방 숫자간 차도 절댓값이 아니라 양수 1이어야 하니까
            ci, cj = i, j
            # 지금 방도 간 거니까 1부터 시작
            move(i, j, 1)
    e = sorted(ls, key=lambda x: (-x[0], x[1]))
    print(f'#{tc} {e[0][1]} {e[0][0]}')