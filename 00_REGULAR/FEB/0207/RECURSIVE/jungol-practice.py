## 함수 3 - 형성평가 3

# N, M = map(int, input().split())
#
# depth = 0
# def func(level, ssum, arr):
#     # global depth
#     # depth += 1
#     if level == N:
#         if ssum == M:
#             print(' '.join(map(str, arr)))
#         return  # 그냥 N번 연산만 했을 때
#
#     if ssum + ((N-level)*6) < M or ssum >= M:  # 뒤에 or ssum >=M을 넣어줬더니 호출 횟수가 36회 줄었음
#         return
#
#     for i in range(1, 7):
#         func(level+1, ssum+i, arr+[i])  # 이렇게 하면 arr을 가지고 다닐 수 있다..?
#
# func(0, 0, [])
# print(depth)

## 함수 3 -
# def fact(n):
#     if n == 1:
#         return n
#     return n * fact(n-1)

## 함수 3 - 연습문제 4:
# 반복문으로 풀기
# cnt = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         for k in range(1, 7):
#             print(i, j, k)
#             cnt += 1
# print(cnt)

N = int(input())
def dice_func(n, arr):
    if not n:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, 7):
        dice_func(n-1, arr+[i])  # arr+[i] : 새로운 객체를 만드는 작업이므로 메모리 낭비이다

# dice_func(N, [])

# 위 방법보다 메모리를 덜 쓰는 방법
choice = [0] * N
def dice_func_re(n):
    if not n:
        print(' '.join(map(str, choice)))
        return

    for i in range(1, 7):
        choice[n-1] = i
        dice_func_re(n-1)

dice_func_re(N)


## 주사위를 n번 던져서 나올 수 있는 모든 경우를 출력하되
## 중복되는 경우는 앞에서부터 작은 순으로 출력하는 프로그램
N = 3
choice = [0] * N
def dice_func_comb(n, ci):
    if not n:
        print(' '.join(map(str, choice)))
        return

    for ni in range(ci, 7):
        choice[N-n] = ni  # 호출할 때 N을 호출해서
        dice_func_comb(n-1, ni)
        # choice[N-n] = 0

dice_func_comb(N, 1)

