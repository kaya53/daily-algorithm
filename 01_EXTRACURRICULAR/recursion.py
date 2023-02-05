# # ## 함수 3 - 재귀 함수
# #
# # # 형성 평가 1
# # n = int(input())
# # arr = []
# #
# # while n >= 1:
# #     arr.append(n)
# #     n //= 2
# # print(*arr[::-1])
# #
# # # 형성 평가 2
# # n = int(input())
# # if n % 2:
# #     for i in range(1, n+1, 2):
# #         print(i, end=' ')
# # else:
# #     for j in range(2, n+1,2):
# #         print(j, end=' ')
# #
# # # 연습 문제 3
# # n = int(input())
# #
# # def fact(N):
# #     if N == 1:
# #         return 1
# #     if N == 2:
# #         return 2
# #     return N * fact(N-1)
# #
# #
# # print(fact(n))
# #
# # # 자가 진단 3
# # n = int(input())
# #
# # def sum_recur(N):
# #     if N == 1: return 1
# #     return N + sum_recur(N-1)
# #
# # print(sum_recur(n))
# #
# # # 연습 문제 4
# # n = int(input())
# #
# # def dice_recur(level, arr):
# #     if level == 3:
# #         print(*arr)
# #         return
# #     for i in range(1, 7):
# #         dice_recur(level+1, arr+[i])
# #
# # dice_recur(0, [])
# #
# #
# # # 형성 평가 3
# # n, m = map(int, input().split())
# #
# #
# # def dice_recur(level, ssum, arr):
# #     if level == n:
# #         if ssum == m:
# #             print(*arr)
# #         return
# #     if ssum + ((n - level) * 6) < m:  # 가지 치기 ; before 183ms, after 143ms
# #         return
# #     for i in range(1, 7):
# #         dice_recur(level+1, ssum+i, arr+[i])
# #
# #
# # dice_recur(0, 0, [])
# #
# # # 형성 평가 4
# # n = int(input())
# # dic = {}
# #
# # def recur(n):
# #     if n in dic:
# #         return dic[n]
# #
# #     if n == 1:
# #         dic[0] = 0
# #         return 1
# #     if n == 2:
# #         dic[1] = 1
# #         return 2
# #     dic[n] = (recur(n-1) * recur(n-2)) % 100
# #     return dic[n]
# #
# # print(recur(n))
# #
# #
# # # 연습문제 5-2
# # n = int(input())
# # fibo = {}
# # def fibo_recur(n):
# #     if n in fibo:
# #         return fibo[n]
# #     if n == 1 or n == 2:
# #         fibo[n] = 1
# #         return 1
# #
# #     fibo[n] = fibo_recur(n-1) + fibo_recur(n-2)
# #     return fibo[n]
# #
# # print(fibo_recur(n))
# #
# #
# # # 자가진단 5
# # n = int(input())
# # ssum = {}
# #
# # def sum_recur(n):
# #     if n in ssum:  # memoization
# #         return ssum[n]
# #     if n == 1:
# #         ssum[n] = 1
# #         return 1
# #     ssum[n] = sum_recur(n // 2) + sum_recur(n - 1)
# #     return ssum[n]
# #
# # print(sum_recur(n))
# #
# #
# # # 연습문제 6
# # n = int(input())
# # def divide_recur(n):
# #     if n // 10 == 0 :
# #         return n % 10
# #     return divide_recur(n // 10) + (n % 10)
# #
# # print(divide_recur(n))
# #
# #
# # # 형성 평가 5
# # n = int(input())
# #
# # def devide_recur(n):
# #     if n == 1:
# #         return 0
# #     if n % 2:
# #         return devide_recur(n // 3) + 1
# #     else:
# #         return devide_recur(n // 2) + 1
# #
# # print(devide_recur(n))
# #
# #
# # # 형성 평가 6
# # n, m, k = map(int, input().split())
# #
# # def mul_recur(N):
# #     if N == 0:
# #         return 1
# #     if N // 10 == 0:
# #         return N
# #     if N % 10 :
# #         return mul_recur(N // 10) * (N % 10)
# #     else:
# #         return mul_recur(N // 10)
# #
# # print(mul_recur(n*m*k))
# #
# #
# # # 자가진단 6
# n = int(input())
#
#
# def square_recur(n):
#     if n // 10 == 0:
#         return n**2
#     res = square_recur(n // 10)  # 여기서도 제곱을 하면 더한 값이 제곱이 되어서 다음 재귀로 return 되므로
#                                  # 여기서는 그냥 원래 값을 리턴하고
#     return res + (n % 10)**2  # 여기서 제곱을 해줘야 함
#
#
# print(square_recur(n))
#
#
# ## 연습문제 1
# def print_recur(n):
#     if n == 0:
#         return
#     print('홍길동')
#     print_recur(n-1)
#
#
# print_recur(10)
#
#
# ## 자가진단 1
# n = int(input())
#
# def recur(n):
#     if n == 0:
#         return
#     print('recursive')
#     recur(n-1)
#
# recur(n)


## 연습 문제 2
# n = int(input())
#
# def num_recur(s, e):
#     if s > e:
#         return
#     print(s, end=' ')
#     num_recur(s+1, e)
#
# num_recur(1, n)


## 자가 진단 2
# n = int(input())
#
# def num_recur(n):
#     if n == 0:
#         return
#     print(n, end=' ')
#     num_recur(n-1)
#
# num_recur(n)