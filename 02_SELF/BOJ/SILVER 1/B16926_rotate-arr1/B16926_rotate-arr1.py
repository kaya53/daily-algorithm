import sys

sys.stdin = open('input.txt')

for _ in range(12):
    # 행, 열 중 더 작은 수는 무조건 짝수
    n, m, r = map(int, input().split())  # 행, 열, 회전 횟수
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 오른쪽 - 아래쪽 - 왼쪽 - 위쪽
    dir_ls = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 사각형 크기
    w = min(n, m) // 2  # 문제 1: 사각형의 크기 기준을 n 기준으로만 잡음
    for i in range(w):  # n: 5, m: 4일 때 ;; i: 0, 1
        lenS = ((n-2*i)*2) + ((m-2*i)*2) - 4
        rot = r % lenS  # 문제 2: r을 갱신하면 다른 턴에서 어그러질 수 있어서 다른 변수에 담아서 해야 한다.
        for _ in range(rot): # r번 회전
            # 반시계 방향 회전
            # 이번 사각형의 크기
            si, sj = i, i+1  # 달팽이처럼 돌자-- 이렇게 하니까 시간 초과남
            k = 0
            tmp = arr[i][i+1]
            while True:
                if si == i and sj == i:
                    arr[si][sj] = tmp
                    break
                ni, nj = si + dir_ls[k][0], sj + dir_ls[k][1]
                if ni < i or ni >= n-i or nj < i or nj >= m-i:
                    k = (k+1) % 4
                    continue
                arr[si][sj] = arr[ni][nj]
                si, sj = ni, nj


    for elem in arr:
        print(' '.join(map(str, elem)))
    print()