import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

def merge_sort(arr):
    # 분할 종료 조건
    if len(arr) < 2:
        return arr

    # 종료되지 않는 배열은 다시 또 분할
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 분할했다면 정렬하기
    l = r = 0
    sorted_arr = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[r])
            r += 1

    sorted_arr.extend(left[l:])
    sorted_arr.extend(right[r:])
    return sorted_arr

for elem in merge_sort(arr):
    print(elem)
