# 230526 python 136ms => 1시간 소요
# 유의할 점
# 1. break하는 시점
# - 주어진 인풋에서 이미 답을 충족할 수 있으므로 가장 처음에 체크해준다.
# 2. time: 0초부터 시작한다.
import sys

sys.stdin = open('input.txt')


def sort_arr(row, col):
    max_length = 0
    new = [[] for _ in range(row)]
    for i in range(row):
        line = []
        count = [0] * 101
        ls = []
        for j in range(col):
            if arr[i][j] == 0: continue
            if count[arr[i][j]] == 0:
                ls.append(arr[i][j])
            count[arr[i][j]] += 1
        for l in ls:
            line.append((l, count[l]))
        line.sort(key=lambda x: [x[1], x[0]])
        now_len = len(line)*2
        if max_length < now_len: max_length = now_len
        while line:
            for _ in range(now_len//2):
                l1, l2 = line.pop(0)
                line += [l1, l2]
            break
        new[i] = line
    for ii in range(row):
        new[ii] = new[ii] + [0]*(max_length-len(new[ii]))
    return new


# for _ in range(3):
R, C, K = map(int, input().split())
inp_arr = [list(map(int, input().split())) for _ in range(3)]

N, M = 3, 3
arr = inp_arr
for time in range(101):
    # 정렬하기
    if (0 < R <= N and 0 < C <= M) and arr[R-1][C-1] == K:
        print(time)
        break

    if N >= M:
        arr = sort_arr(N, M)
    else:
        arr = list(map(list, zip(*arr)))
        arr = list(map(list, zip(*sort_arr(M, N))))

    N = len(arr)
    M = len(arr[0])

    if N > 100:
        arr = arr[:100]
    elif M > 100:
        for i in range(N):
            target = arr[i]
            arr[i] = arr[i][:100]

else:
    print(-1)