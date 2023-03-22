import sys

sys.stdin = open('input.txt')

## 틀린 이유
# 처음에 틀린 이유
# 1. 문제를 제대로 읽지 않음
    # - 문제에서 방향을 줄 때 북-동-남-서 순서대로 줬는데, 북-서-남-동 순으로 놓고 풀어서 문제가 생김
# 2. if not arr[ni][nj]:  DFS(ni, nj, k, arr)
    # 이 부분에서 한 번 청소를 했으면 그 다음 방향을 봐야 하는데 재귀를 호출하고 return을 안해줘서 문제가 생겼음

def DFS(si, sj, dir):
    global cnt

    if not arr[si][sj]:
        cnt += 1  # 청소했음
        arr[si][sj] = 2

    flag = 0
    for k in range(dir + 7, dir + 3, -1):
        k %= 4
        ni, nj = si + di[k], sj + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= M : continue
        if not arr[ni][nj]:  # 현재 칸 중심으로 사방탐색을 하다가 청소 안한 칸이 있으면
            DFS(ni, nj, k)  # 그 방향으로 방향을 바꾸고 다시 dfs
            flag = 0  # 사방 확인을 위한 플래그 -> 청소 안한 칸이 하나라도 있으면 0
            return
        else:
            flag = 1

    # 사방이 벽이거나 청소를 마친 경우
    if flag:
        ni, nj = si - di[dir], sj - dj[dir]
        if arr[ni][nj] == 1:
            return

        DFS(ni, nj, dir)


# for _ in range(3):
N, M = map(int, input().rstrip().split())
si, sj, dir = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북동남서

cnt = 0
DFS(si, sj, dir)
print(cnt)
