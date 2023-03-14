# print(2**15 - 22077)  # 10691

# 이번 칸에 넴모를 놓는 경우
    # - 놓을 때 사각형이 그려지지 않는 지 확인이 되면 놓아야 함
# 이번 칸에 넴모를 놓지 않는 경우
    # - 안 놓고 그냥 다음 dfs로 넘어가면 됨


import sys

sys.stdin = open('input.txt')


def dfs(si, sj):
    global cnt
    if si == n+1 and sj == 1:
        cnt += 1
        # for elem in arr:
        #     print(elem)
        # print()
        return

    if sj == m:
        ni, nj = si + 1, 1
    else:
        ni, nj = si, sj + 1
    
    # 넴모를 이번 칸에 놓지 않고 다음 칸으로 이동
    dfs(ni, nj)

    # si, sj에 넴모를 놓아도 2*2 사각형이 안되는 경우
    if not arr[si-1][sj] or not arr[si-1][sj-1] or not arr[si][sj-1]:
        arr[si][sj] = 1
        dfs(ni, nj)
        arr[si][sj] = 0


n, m = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]
cnt = 0
dfs(1, 1)  # 1~n-1, 1~m-1까지만 보기 위해서
print(cnt)