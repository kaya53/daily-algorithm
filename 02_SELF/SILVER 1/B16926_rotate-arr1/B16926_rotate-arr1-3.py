import sys

sys.stdin = open('input.txt')

# for _ in range(12):
n, m, r = map(int, input().split())  # 행, 열, 회전 횟수
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    s = min(n, m) // 2  # 사각형 갯수
    for j in range(s):  # 사각형 개수만큼 돌린다.
        si, sj = j, j
        pre = arr[si][sj]  # 돌릴 시작점

        for i in range(si+1, n-j):  # 윗변 돌리기
            tmp = arr[i][j]  # 시작점 다음 좌표
            arr[i][j] = pre  # 다음 좌표의 값은 이전 좌표에서 가져온다
            pre = tmp
        for i in range(sj+1, m-j):  # 오른쪽 변 돌리기
            tmp = arr[n-j-1][i]  # 오른쪽 변의 시작 좌표
            arr[n-j-1][i] = pre
            pre = tmp

        for i in range(n-j-2, j-1, -1):  # 아래쪽 변 돌리기
            tmp = arr[i][m-1-j]
            arr[i][m-1-j] = pre
            pre = tmp
        for i in range(m-j-2, j-1, -1):
            tmp = arr[j][i]
            arr[j][i] = pre
            pre = tmp
for elem in arr:
        print(' '.join(map(str, elem)))