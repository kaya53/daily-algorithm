import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def dfs(ci, cj, cnt):
    global mmax

    if cnt == 26:
        mmax = 26
        return True

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[arr[ni][nj]]: continue
        now = arr[ni][nj]
        visited[now] = 1
        if dfs(ni, nj, cnt+1): return True
        visited[now] = 0
    # 다음 최댓값을 찾아볼 여지가 있는 상태 => return False 해줘서 더 찾을 수 있게
    # 이 부분을 위로 올릴 수 있을까
    else:  
        mmax = max(mmax, cnt)
        return False


# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(lambda x: ord(x)-65, input())) for _ in range(N)]

visited = [0] * 26  # 알파벳에 대한 visited
visited[arr[0][0]] = 1
mmax = 0
dfs(0, 0, 1)
print(mmax)
