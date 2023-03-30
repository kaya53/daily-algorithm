import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def move(d, arr):
    if d < 2: # 위, 아래
        arr = list(map(list, zip(*arr)))
    res = slide(d, plus_block(d, slide(d, arr)))
    if d < 2:
        res = list(map(list, zip(*arr)))

    return res


def slide(d, arr):
    for i in range(N):
        nums = []
        zeros = []
        for j in range(N):
            if arr[i][j] > 0: nums.append(arr[i][j])
            else: zeros.append(0)
        if not d % 2:  # 위, 왼쪽
            arr[i] = nums + zeros
        else:
            arr[i] = zeros + nums
    return arr


def plus_block(d, arr):
    for i in range(N):
        if not d % 2:
            j = 0
            while j < N-1:
                if arr[i][j] and arr[i][j+1] and arr[i][j] == arr[i][j+1]:
                    arr[i][j] *= 2
                    arr[i][j+1] = 0
                    j += 2
                else: j += 1
        else:
            j = N-1
            while j > 0:  # 여기를 j > 1이라고 해서 11%에서 틀렸었음
                if arr[i][j] and arr[i][j-1] and arr[i][j] == arr[i][j-1]:
                    arr[i][j] *= 2
                    arr[i][j-1] = 0
                    j -= 2
                else: j -= 1
    return arr


def backtrack(idx, n, arr):
    global max_ans

    if idx == n:
        max_block = 0
        for a in arr:
            max_block = max(max_block, max(a))
        if max_ans < max_block:
            max_ans = max_block
        return
    for d in range(4):
        std = [x[:] for x in arr]
        arr = move(d, arr)
        backtrack(idx+1, n, arr)
        arr = std


# for _ in range(2):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_ans = 0
for k in range(1, 6):  # 최대 5까지 돌 수 있으니까 6까지!
    choice = [0] * k
    backtrack(0, k, arr)
print(max_ans)