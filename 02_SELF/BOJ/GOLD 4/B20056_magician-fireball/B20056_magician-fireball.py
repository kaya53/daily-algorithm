import sys

sys.stdin = open('input.txt')

from collections import deque


def fireball():
    cnt = 0
    while cnt < k:
        cnt += 1
        # 1. 모든 파이어볼 이동시키기
        while info:
            ci, cj, m, s, d = info.popleft()
            ni = (ci + dir[d][0]*s) % n
            nj = (cj + dir[d][1]*s) % n
            # flag = 0
            # print(ci, cj, ni, nj)
            if arr[ni][nj]:  # 이동한 곳에 파이어볼이 있으면
                arr[ni][nj][0] += m  # 질량 더해주기
                arr[ni][nj][1] += s  # 속력 더해주기
                arr[ni][nj][-1] += 1  # 파이어볼 개수 더해주기
                # 방향 처리; 다 더해서 나머지가 0/1만 따지면 1,3,2,4와 같은 경우는 거르지 못한다
                # 같으면 0 
                # 여태까지 같았는 데 이번에 다르면 1로 바꾼다
                # 1로 바뀌었다면 이 if문은 실행되지 않음
                prev_d = arr[ni][nj][2]
                prev_flag = arr[ni][nj][3]
                if not prev_flag and (prev_d % 2 != d % 2):
                    arr[ni][nj][3] = 1

            else:  # 파이어볼이 없는 빈칸
                arr[ni][nj] = [m, s, d, 0, 1]
                arr[ci][cj] = 0  # 이동하고 원래 자리는 초기화

        # 2. 파이어볼이 두개 이상 있는 칸에서 일어나는 일
        for i in range(n):
            for j in range(n):
                if arr[i][j] and arr[i][j][-1] >= 2:
                    # if arr[i][j][0]:
                    new_m = arr[i][j][0] // 5
                    new_s = arr[i][j][1] // arr[i][j][-1]
                    # start = 1
                    # if not arr[i][j][2] % 2: start = 0
                    start = arr[i][j][3]
                    if new_m:  # 질량이 0이면 파이어볼 소멸
                        for new_d in range(start, start+7, 2):
                            info.append((i, j, new_m, new_s, new_d))
                    arr[i][j] = 0
        if cnt == k:
            print(info)
            for elem in arr:
                print(elem)
            print('----------')
            return


for _ in range(4):
    n, m, k = map(int, input().split())
    info = deque([list(map(int, input().split())) for _ in range(m)])
    for y in range(m):
        info[y][0] -= 1
        info[y][1] -= 1

    arr = [[0]*n for _ in range(n)]
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


    fireball()