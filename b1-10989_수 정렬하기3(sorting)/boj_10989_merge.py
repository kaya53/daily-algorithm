import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 머지 소트
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 정렬 시작
    merged_arr = []
    l = r = 0  # l : 왼쪽 배열을 훑을 인덱스, r: 오른쪽 배열을 훑을 인덱스
    while l < len(left) and r < len(right):  # l, r을 0부터 1씩 증가시키면서 볼 것 -> 왼쪽, 오른쪽 중 하나라도 끝까지 가면 이 반복문 종료
        if left[l] < right[r]:
            merged_arr.append(left[l])  # 둘 중 작은 애를 먼저 merged_arr에 넣고,
            l += 1  # 넣은 후 인덱스 하나 올리기
        else:  # 위랑 반대로
            merged_arr.append(right[r])
            r += 1

    # 반복이 종료된 후에 왼쪽이든 오른쪽이든 배열에 남은 원소가 있으면
    # 그건 크기가 가장 크기 때문에 남은 거니까 merged_arr에 바로 넣어주기
    merged_arr += left[l:]
    merged_arr += right[r:]

    # 그리고 나서 merged_arr을 리턴
    return merged_arr

res = merge_sort(arr)
for i in res:
    print(i)


