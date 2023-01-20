# # 1. 위와 같은 결과가 나오도록 구구단을 출력하세요.
# for i in range(1, 10):  # 곱해지는 수
#     for j in range(2, 10): # 구구단 단 수
#         print(f'{j}*{i} = {j*i:2d}', end = '  ')
#     print()
# # 2. 3의 배수의 단만 구구단을 출력하세요
# for i in range(1, 10):
#     print(f'{3}*{i} = {3*i:2d}')

# # 3. 1번처럼 구구단을 출력하는데 연산 결과값이 60을 초과하는 처음 연산이 나오는 경우 출력을 멈추세요
# # 반복을 두 번 나오는 것이 포인트
# for i in range(2, 10):  # 곱해지는 수
#     for j in range(1, 10): # 구구단 단 수
#         print(f'{i}*{j} = {j*i:2d}', end = '  ')
#         if i*j > 60:
#             break
#     print()
#     if i*j > 60:
#         break

# # 문자열 1 - 형성평가 1
# str = input()
# flip = str.split(' ')[::-1]
# print(*flip)

# # 문자열 2 - 형성평가 2
# a, b, c = map(int, input().split())
# print(((a+b)*c/2))

# # 문자열 3 - 형성평가 3
# a = input()
# b = input()
# c = input()
# d = input()

# print(f'{a}: {b} \n{c}: {d}')

# # 문자열 4 - 형성평가 4
# lb = round(float(input('LB? ')), 1)
# kg = round(0.45*lb, 1)
# print(f'{lb}LB is {kg}KG.')

# # 문자열 1 - 자가진단 7
# name = input()
# no = int(input())
# avg = round(float(input()), 2)
# print(f'I am {name}(IdNo. {no}). I got {avg:.2f} in my midterm exam.')

# # 문자열 1 - 형성평가 5
# name, height, weight = input().split()
# print(f'{name}의 키는 {height}cm이며, 몸무게는 {round(float(weight), 1)}kg입니다.')

# # 리스트 1 - 형성평가 1
# arr = [-1, -2, -3, -4, -5]
# print(arr)

# # 리스트 1 - 형성평가 2
# arr = []
# for _ in range(2):
#     num, cnt = map(int, input().split())
#     arr += ([num]*cnt)
# print(arr)

# # 리스트 1 - 형성평가 3
# arr_c = []
# arr_a = []
# for _ in range(4):
#     color, animal = input('Input? ').split()
#     arr_c.append(color)
#     arr_a.append(animal)
# print(f'Color: {arr_c}\nAnimal: {arr_a}')

# # 리스트 1 - 형성평가 4
# str = input()[::-1]
# arr = [i for i in str]
# print(arr)

# # 리스트 1 - 형성평가 5
# nums = input().split()
# arr = []
# for idx, num in enumerate(nums, 1):
#     if not (idx % 3):
#         arr.append(str(num))
# print(arr)

# # 리스트 1 - 형성평가 6
# a = input().split()[::-1]
# print(a[1:-1])

# # 선택제어문 - 형성평가 1
# a, b = map(int, input().split())
# if a > b:
#     print(a-b)
# else:
#     print(b-a)

# # 선택제어문 - 형성평가 2
# num = int(input())
# if num < 0 :
#     print('minus')
# elif num == 0:
#     print('zero')
# else:
#     print('plus')

# # 선택제어문 - 형성평가 3
# yr = int(input())
# msg = "common year"
# if not (yr % 400):
#     msg = "leap year"
# if (not (yr % 4)) and (yr % 100):
#     msg = "leap year"
# print(msg)

# # 선택제어문 - 형성평가 4
# dict = { 1 : 'dog', 2 : 'cat', 3 : 'chick'}
# num = int(input('Number? '))
# print(dict.get(num, 'I don\'t know.'))

# 선택제어문 - 형성평가 5
num = int(input())
if num in [1,3,5,7,8,10,12]:
    print(31)
elif num == 2:
    print(28)
else:
    print(30)