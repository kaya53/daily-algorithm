import sys

sys.stdin = open('input.txt')

# 되는 조합 찾기
# 한 나라의 승/무/패를 결정하면
# 나머지 5나라 중 한 나라는 패/무/승이어야 한다.

# 가능한 총 경기의 경우의 수를 구한다
# 승 무 패 중 하나를 고른다. => 이에 대응되는 다른 나라를 고른다.
# 고른다.
# 고른 걸 취소한다.
# 이렇게 15번을 하면 끝?
# 경기 조합 구하기


def is_worldcup(idx, arr):  # idx, n번째 결과 현황판
    global flag
    if flag: return
    if idx == 15:
        for i in range(6):
            for j in range(3):
                if arr[i][j]: return
        else:
            flag = True
        return

    n1, n2 = res_ls[idx]
    for k in range(3):
        if not arr[n1][k]: continue
        arr[n1][k] -= 1
        arr[n2][winlose[k]] -= 1
        is_worldcup(idx+1, arr)
        arr[n1][k] += 1
        arr[n2][winlose[k]] += 1


# start
res_ls = []
for i in range(6):
    for j in range(i+1, 6):
        res_ls.append((i, j))

winlose = {0: 2, 1: 1, 2: 0}
# input
arr = [[] for _ in range(4)]
for x in range(4):
    flag = False
    inp = list(map(int, input().split()))
    for i in range(0, 16, 3):
        arr[x].append(inp[i:i+3])

    is_worldcup(0, arr[x])
    if flag:
        print(1, end=' ')
    else:
        print(0, end=' ')



