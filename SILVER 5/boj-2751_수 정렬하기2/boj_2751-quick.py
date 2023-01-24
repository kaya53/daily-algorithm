import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 퀵 소트
# def quick_sort(arr):
    # 분할과 정렬을 구분하지 않은 코드 -- Runtime Error(Recursion Error 발생)

    # if len(arr) < 2:
    #     return arr
    #
    # pivot = arr[len(arr) // 2]
    # left, mid, right = [], [], []
    # for num in arr:
    #     if num < pivot:
    #         left.append(num)
    #     elif num > pivot:
    #         right.append(num)
    #     else:
    #         mid.append(num)
    #
    # return quick_sort(left) + mid + quick_sort(right)

# for elem in quick_sort(arr):
#     print(elem)


# 유튜브 보고 따라 치기 -- recursion error 발생
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1  # 피봇보다 작은 요소를 추적하는 커서
    j = l
    while j <= r - 1:  # 피봇 직전까지 순회
        if arr[j] <= pivot:
            i += 1  # j가 피봇보다 작으면 하나 증가
            arr[i], arr[j] = arr[j], arr[i]  # 
        j += 1

    arr[i + 1], arr[r] = arr[r], arr[i+1]
    return i + 1


def quick_sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, r)
        return arr


for elem in quick_sort(arr, 0, N-1):
    print(elem)


