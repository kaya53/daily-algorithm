import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 단순 선택 정렬; 메모리 초과 
for i in range(N):
    mmin = i  # 현재 인덱스 중 최소 인덱스
    for j in range(i+1, N):
        if arr[mmin] > arr[j]:
            mmin = j
    arr[mmin], arr[i] = arr[i], arr[mmin]
    # i+1 ~ N에 대해서 모두 순회한 결과 최소값과 바꿔야 하므로 for j ..와 같은 라인에서 바꾼다.
for ii in arr:
    print(ii)