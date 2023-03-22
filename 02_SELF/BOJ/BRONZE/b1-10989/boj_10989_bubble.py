import sys

# sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
# print(arr)

# 메모리 제한에서 걸림
for i in range(N):
    for j in range(i, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
