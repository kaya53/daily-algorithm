from collections import deque


def get_weight():
    arr = [[100] * 10 for _ in range(10)]
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    for i in range(4):
        for j in range(3):
            if board[i][j] == -1: continue
            q = deque([(i, j, 0)])  # 시작점, 가중치
            num = board[i][j]
            arr[num][num] = 1  # 자기 자신의 가중치

            while q:
                ci, cj, cost = q.popleft()

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= 3 or nj < 0 or nj >= 3 or board[ni][nj] == -1: continue
                    next_num = board[ni][nj]
                    if num and next_num < num: continue

                    if arr[num][next_num] > cost + 2:
                        arr[num][next_num] = cost + 2
                        arr[next_num][num] = cost + 2
                        q.append((ni, nj, cost + 2))
                for ddi, ddj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nni, nnj = ci + ddi, cj + ddj
                    if nni < 0 or nni >= 3 or nnj < 0 or nnj >= 3 or board[nni][nnj] == -1: continue
                    next_num = board[nni][nnj]
                    if num and next_num < num: continue

                    if arr[num][next_num] > cost + 3:
                        arr[num][next_num] = cost + 3
                        arr[next_num][num] = cost + 3
                        q.append((nni, nnj, cost + 3))
    return arr


def solution(numbers):
    answer = 0
    n = len(numbers)
    numbers = list(map(int, numbers))
    weight = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3], [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
              [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
              [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
              [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]
    # print(weight)

    dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n)]
    sl, sr = 4, 6
    for i in range(n):
        num = numbers[i]
        if not i:
            dp[i][0] = [num, sr, weight[4][num]]
            dp[i][1] = [sl, num, weight[6][num]]
            continue

        target = numbers[i]
        before_left_weight = dp[i - 1][0][2]
        before_right_weight = dp[i - 1][1][2]
        # 왼쪽 손
        before_left_pos_l = dp[i - 1][0][0]
        before_right_pos_l = dp[i - 1][1][0]
        # 오른쪽 손
        before_left_pos_r = dp[i - 1][0][1]
        before_right_pos_r = dp[i - 1][1][1]
        # 1. 이번 차례에 왼쪽 손 쓰기
        if before_left_pos_l == target and before_right_pos_l == target:
            if before_left_weight < before_right_weight:
                dp[i][0] = dp[i - 1][0][:]
                dp[i][0][2] += 1
            else:
                dp[i][0] = dp[i - 1][1][:]
                dp[i][0][2] += 1
        elif before_left_pos_l == target:
            dp[i][0] = dp[i - 1][0][:]
            dp[i][0][2] += 1
        elif before_right_pos_l == target:
            dp[i][0] = dp[i - 1][1][:]
            dp[i][0][2] += 1
        else:
            if before_left_weight + weight[before_left_pos_l][target] < before_right_weight + \
                    weight[before_right_pos_l][target]:
                dp[i][0] = [target, before_left_pos_r, before_left_weight + weight[before_left_pos_l][target]]
            else:
                dp[i][0] = [target, before_right_pos_r, before_right_weight + weight[before_right_pos_l][target]]

        # 이번에 오른쪽 손 쓰기
        if before_left_pos_r == target and before_right_pos_r == target:
            if before_left_weight < before_right_weight:
                dp[i][1] = dp[i - 1][0][:]
                dp[i][1][2] += 1
            else:
                dp[i][1] = dp[i - 1][1][:]
                dp[i][1][2] += 1
        elif before_left_pos_r == target:
            dp[i][1] = dp[i - 1][0][:]
            dp[i][1][2] += 1
        elif before_right_pos_r == target:
            dp[i][1] = dp[i - 1][1][:]
            dp[i][1][2] += 1
        else:
            if before_left_weight + weight[before_left_pos_r][target] < before_right_weight + \
                    weight[before_right_pos_r][target]:
                dp[i][1] = [before_left_pos_l, target, before_left_weight + weight[before_left_pos_r][target]]
            else:
                dp[i][1] = [before_right_pos_l, target, before_right_weight + weight[before_right_pos_r][target]]

    # for i in range(n):
    #     print(i, '번째 dp, 누를 숫자: ', numbers[i])
    #     print('왼쪽', dp[i][0])
    # print('오른쪽', dp[i][1])

    return min(dp[-1][0][2], dp[-1][1][2])

