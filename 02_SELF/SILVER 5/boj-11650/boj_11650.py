import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]

# sorted() 활용 -> pass
# for elem in sorted(arr):
#     print(*elem)

# 버블 소트 활용하기 -- 시간 초과 fail
# N = 5
# arr = [5,156,78,3,1]

def bubble_sort(arr, s, e, k): # 정렬할 배열, 인덱스 시작점, 인덱스 끝 점, x/y 좌표
    for i in range(s, e+1):
        mmin = i
        for j in range(i+1, e+1):
            if arr[j][k] < arr[mmin][k]:
                mmin = j
        arr[i], arr[mmin] = arr[mmin], arr[i]

    return arr


arr = bubble_sort(arr,0, N-1, 0)
# y좌표 비교

idx_i = idx_j = 0
while idx_j < N - 1 :
    while arr[idx_j][0] == arr[idx_j + 1][0]:
        idx_j += 1
        if idx_j == N - 1:
            break
    bubble_sort(arr, idx_i, idx_j, 1)
    idx_j += 1
    idx_i = idx_j

for elem in arr:
    print(*elem)




