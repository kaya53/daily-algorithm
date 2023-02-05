import sys

sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     res = [0] * (N-M+1)
#     for i in range(0, N-M+1):
#         ssum = 0
#         for k in range(M):
#             ssum += arr[i+k]
#         res[i] = ssum
#         # res.append(ssum)  # append를 하기보다 배열의 크기를 정해놓고 하는 것을 권장
#
#     # min, max 함수는 안쓰는 게 효율이 좋을 수 있음
#     mmax = 0
#     mmin = 1000000
#     for elem in res:
#         if elem > mmax:
#             mmax = elem
#         if elem < mmin:
#             mmin = elem
#     print(f'#{tc} {mmax- mmin}')


### 슬라이딩 윈도우 기법
# t = int(input())
#
#
# for i in range(1,t+1):
#     n, m = map(int, input().split())
#     lst = list(map(int, input().split()))
#     cnt = sum(lst[:m])
#     mxnum = cnt
#     minum = cnt
#     for j in range(m, n):
#         if cnt > mxnum:
#             mxnum = cnt
#         elif cnt < minum:
#             minum = cnt
#         cnt += lst[j] - lst[j - m]
          # 💡💡 뒤에 것을 하나 더하고 가장 앞의 것을 빼서 다음 턴의 구간합을 구한다
#     if cnt > mxnum:
#         mxnum = cnt
#     elif cnt < minum:
#         minum = cnt
#     print(f'#{i} {mxnum - minum}')


### 내 코드에 슬라이딩 윈도우 기법 적용
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ssum = sum(arr[:M])
    mmax = mmin = ssum
    for i in range(M, N):
        ssum += arr[i] - arr[i-M]
        if ssum > mmax:
            mmax = ssum
        if ssum < mmin:  # 여기를 elif로 처리하면 값이 1개인 경우, 첫 값이 minimum인 경우 제대로 출력이 안됨
            mmin = ssum  # if ~ if 구조로 해야함 ; else를 써도 되는 지 잘 모르겠으면 메모리가 더 써져도 안쓰는 게 안전함

    print(f'#{tc} {mmax - mmin}')