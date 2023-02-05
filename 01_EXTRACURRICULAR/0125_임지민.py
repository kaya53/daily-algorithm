# # 문자열 2
# # 형성 평가 1
# strs = input().split('(space)')
# for elem in strs[::-1]:
#     print(elem.strip())
#
# # 2
# strs, n, m = input().split()
# n, m = int(n), int(m)
# for _ in range(m):
#     cutted = strs[:n]
#     res = strs[n:]
#     res += cutted
#     strs = res
#     print(res)
#
#
# # 3
# arr = input().split()
# print(sorted(arr)[0])
# print(sorted(arr)[-1])
#
#
# # 4
# a, b, n = input().split()
# n = int(n)
# A = a+b
# from_a = A[:n]
# from_b = b[n:]
# B = from_a + from_b
# print(A, B, sep='\n')
#
#
# # 6
# strs = input()
# msg = 'X'
# if strs.isnumeric():
#     msg = 'D'
# else:  # 숫자 + 문자 or 문자들
#     if strs.isupper():  # 모두 대문자인 문자열
#         msg = 'U'
#     elif strs.islower():  # 모두 소문자인 문자열
#         msg = 'L'
# print(msg)
# print(strs.upper())

# print(strs.upper())
#
#
# # 7
# strs = input()
# b, c = input().split()
# cnt = 0
# print(strs.count(b))
# print(strs.replace(b, c))
#
#
# # 리스트 2
# # 1
# res = []
# while (N := int(input())) != -1:
#     res.append(N)
# print(*res[-3:])
#
# # 2
# arr = list(map(float, input().split()))
# print(round(sum(arr)/len(arr), 1))
#
# # 3
# arr = ['J', 'U', 'N', 'G', 'O', 'L']
# n = input().upper()
# # print(n)
# msg = 'none'
# for i in range(len(arr)):
#     if arr[i] == n:
#         msg = i
# print(msg)
#
# # 4
# arr = list(map(int, input().split()))
# print(f'max : {max(arr)}\nmin : {min(arr)}')
#
# # 5
# arr = list(map(int, input().split()))
#
# cnt = 0
# ssum = 0
# for elem in arr:
#     if not (elem % 5):
#         cnt += 1
#         ssum += elem
# aavg = round(ssum / cnt, 1)
# print(f'Multiples of 5 : {cnt}\nsum : {ssum}\navg : {aavg}')
#
#
# # 6
# arr = list(map(int, input().split()))
# print(len(arr))
#
# for elem in arr:
#     if elem % 2:
#         print(elem*2, end=' ')
#     else:
#         print(elem//2, end=' ')
#
#
# # 7
# n = int(input())
# scores = list(map(int, input().split()))
# for elem in sorted(scores)[::-1]:
#     print(elem)
#
# # 8
# arr = ["flower", "rose", "lily", "daffodil", "azalea"]
# n = input().lower()
# cnt = 0
# for elem in arr:
#     if elem[1] == n or elem[2] == n:
#         print(elem)
#         cnt += 1
# print(cnt)
#
#
# # 9
# cnt = 0
# arr = []
# while (strs := input()) != '0':
#     cnt += 1
#     if "mo" in strs:
#         arr.append(strs)
# print(cnt)
# for elem in arr:
#     print(elem)
