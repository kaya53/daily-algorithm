### 함수 3 - 재귀 함수

## 형성 평가 1
# n = int(input())
# arr = []
#
# while n >= 1:
#     arr.append(n)
#     n //= 2
# print(*arr[::-1])

## 형성 평가 2
# n = int(input())
# if n % 2:
#     for i in range(1, n+1, 2):
#         print(i, end=' ')
# else:
#     for j in range(2, n+1,2):
#         print(j, end=' ')

## 연습 문제 3
# n = int(input())
#
# def fact(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     return N * fact(N-1)
#
#
# print(fact(n))

## 자가 진단 3
# n = int(input())
#
# def sum_recur(N):
#     if N == 1: return 1
#     return N + sum_recur(N-1)
#
# print(sum_recur(n))

## 연습 문제 4
# n = int(input())
#
# def dice_recur(level, arr):
#     if level == 3:
#         print(*arr)
#         return
#     for i in range(1, 7):
#         dice_recur(level+1, arr+[i])
#
# dice_recur(0, [])


## 형성 평가 3
# n, m = map(int, input().split())
#
#
# def dice_recur(level, ssum, arr):
#     if level == n:
#         if ssum == m:
#             print(*arr)
#         return
#     if ssum + ((n - level) * 6) < m:  # 가지 치기 ; before 183ms, after 143ms
#         return
#     for i in range(1, 7):
#         dice_recur(level+1, ssum+i, arr+[i])
#
#
# dice_recur(0, 0, [])

## 형성 평가 4
n = int(input())
dic = {}

def recur(n):
    if n in dic:
        return dic[n]

    if n == 1:
        dic[0] = 0
        return 1
    if n == 2:
        dic[1] = 1
        return 2
    dic[n] = (recur(n-1) * recur(n-2)) % 100
    return dic[n]

print(recur(n))