import sys

sys.stdin = open('input.txt')


def rotate(cnt, flag, arr):
    if flag == 'f':
        # ran: ls를 탐색할 range의 list
        for _ in range(cnt):
            first = [arr[ii][jj] for ii, jj in ls[0]]
            for k in range(4):
                cur = ls[k]
                # 첫번째 것은 미리 빼놓는다.
                if k == IDX-2: cur = cur[::-1]
                if k == IDX-1:
                    for d in range(n):
                        arr[cur[d][0]][cur[d][1]] = first[d]
                    continue
                # 지금 거를 그 다음 턴에서 가져온다.
                aft = ls[(k + 1) % IDX]
                for d in range(n):  # ls[k]를 순회하면서 인덱스를 가져온다.
                    arr[cur[d][0]][cur[d][1]] = arr[aft[d][0]][aft[d][1]]
    else:
        for _ in range(cnt):
            last = [arr[ii][jj] for ii, jj in ls[-1]]
            for k in range(3, -1, -1):
                # 마지막 것은 미리 빼놓는다.
                # 지금 거를 그 다음 턴에서 가져온다.
                cur = ls[k]
                if k == IDX-1: cur = cur[::-1]
                if k == 3:
                    for d in range(n):
                        arr[cur[d][0]][cur[d][1]] = last[d]
                    continue
                aft = ls[(k - 1) % IDX]
                # print(cur, aft)
                for d in range(n):  # ls[k]를 순회하면서 인덱스를 가져온다.
                    arr[aft[d][0]][aft[d][1]] = arr[cur[d][0]][cur[d][1]]


t = int(input())
for _ in range(1, t+1):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    IDX = n-1
    flag = 'f' if d < 0 else 'z'
    if abs(d) == 360:
        for elem in arr:
            print(' '.join(map(str, elem)))
        continue
    ls = [[] for _ in range(4)]
    for i in range(n):
        for j in range(n):
            if i == j:
                ls[0].append((i, j))
            if j == n//2:
                ls[1].append((i, j))
            if i+j == IDX:
                ls[2].append((i, j))
            if i == n//2:
                ls[3].append((i, j))
            # ls[3] = ls[3]
    rotate(abs(d)//45, flag, arr)
    for elem in arr:
        print(' '.join(map(str, elem)))