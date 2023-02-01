import sys

sys.stdin = open('input.txt')


# 버블 소트 적용 -- 52ms
arr = list(map(int, sys.stdin.readline().rstrip().split()))
N = len(arr)
k = N - 1
while k > 0:
    for i in range(k):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    k -= 1
    # if arr == [1,2,3,4,5] : break  # 이 코드 넣으니까 40ms로 줄어듦

# 버블 소트를 쓰다만 느낌인 코드 -- 36ms
while arr != [1, 2, 3, 4, 5]:
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)