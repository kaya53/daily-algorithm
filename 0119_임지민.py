# 1. 위와 같은 결과가 나오도록 구구단을 출력하세요.
for i in range(1, 10):  # 곱해지는 수
    for j in range(2, 10): # 구구단 단 수
        print(f'{j}*{i} = {j*i:2d}', end = '  ')
    print()
# 2. 3의 배수의 단만 구구단을 출력하세요
for i in range(1, 10):
    print(f'{3}*{i} = {3*i:2d}')

# 3. 1번처럼 구구단을 출력하는데 연산 결과값이 60을 초과하는 처음 연산이 나오는 경우 출력을 멈추세요
# 반복을 두 번 나오는 것이 포인트
for i in range(2, 10):  # 곱해지는 수
    for j in range(1, 10): # 구구단 단 수
        print(f'{i}*{j} = {j*i:2d}', end = '  ')
        if i*j > 60:
            break
    print()
    if i*j > 60:
        break

# 문자열 1 - 형성평가 1
str = input()
flip = str.split(' ')[::-1]
print(*flip)

# 문자열 2 - 형성평가 2
a, b, c = map(int, input().split())
print(((a+b)*c/2))

# 문자열 3 - 형성평가 3
a = input()
b = input()
c = input()
d = input()

print(f'{a}: {b} \n{c}: {d}')

# 문자열 4 - 형성평가 4
lb = round(float(input('LB? ')), 1)
kg = round(0.45*lb, 1)
print(f'{lb}LB is {kg}KG.')

# 문자열 1 - 자가진단 7
name = input()
no = int(input())
avg = round(float(input()), 2)
print(f'I am {name}(IdNo. {no}). I got {avg:.2f} in my midterm exam.')

# 문자열 1 - 형성평가 5
name, height, weight = input().split()
print(f'{name}의 키는 {height}cm이며, 몸무게는 {round(float(weight), 1)}kg입니다.')

# 리스트 1 - 형성평가 1
arr = [-1, -2, -3, -4, -5]
print(arr)

# 리스트 1 - 형성평가 2
arr = []
for _ in range(2):
    num, cnt = map(int, input().split())
    arr += ([num]*cnt)
print(arr)

# 리스트 1 - 형성평가 3
arr_c = []
arr_a = []
for _ in range(4):
    color, animal = input('Input? ').split()
    arr_c.append(color)
    arr_a.append(animal)
print(f'Color: {arr_c}\nAnimal: {arr_a}')

# 리스트 1 - 형성평가 4
str = input()[::-1]
arr = [i for i in str]
print(arr)

# 리스트 1 - 형성평가 5
nums = input().split()
arr = []
for idx, num in enumerate(nums, 1):
    if not (idx % 3):
        arr.append(str(num))
print(arr)

# 리스트 1 - 형성평가 6
a = input().split()[::-1]
print(a[1:-1])

# 선택제어문 - 형성평가 1
a, b = map(int, input().split())
if a > b:
    print(a-b)
else:
    print(b-a)

# 선택제어문 - 형성평가 2
num = int(input())
if num < 0 :
    print('minus')
elif num == 0:
    print('zero')
else:
    print('plus')

# 선택제어문 - 형성평가 3
yr = int(input())
msg = "common year"
if not (yr % 400):
    msg = "leap year"
if (not (yr % 4)) and (yr % 100):
    msg = "leap year"
print(msg)

# 선택제어문 - 형성평가 4
dict = { 1 : 'dog', 2 : 'cat', 3 : 'chick'}
num = int(input('Number? '))
print(dict.get(num, 'I don\'t know.'))

# 선택제어문 - 형성평가 5
num = int(input())
if num in [1,3,5,7,8,10,12]:
    print(31)
elif num == 2:
    print(28)
else:
    print(30)

# 반복제어문 - 형성평가 1
N = int(input())
for i in range(1, N+1):
    print(i, end=' ')

# 반복 제어문 - 형성평가 2
odd, even = 0, 0
while True:
    num = int(input())
    if num == 0 :
        print(f'odd : {odd}')
        print(f'even : {even}')
        break
    else:
        if num % 2: odd += 1
        else: even += 1

# 반복 제어문 - 형성평가 3
ssum, total = 0, 0
while True:
    num = int(input())
    if (num < 0) or (num > 100):
        print(f'sum : {ssum}')
        print(f'avg : {round(ssum / total, 1)}')
        break
    else:
        ssum += num
        total += 1

# 반복 제어문 - 형성평가 4 => 다시보기
res = 0
while True:
    num = int(input())
    if num == 0 :
        print(res)
        break
    else:
        if (num % 3) and (num % 5):
            res += 1

# 반복 제어문 - 자가 진단 5
while True:
    num = int(input())
    if num == -1 : break
    if not num % 3 :
        print(num // 3)

# 반복 제어문 - 자가 진단 5
# 종료 조건: continue? y
while True:
    width = int(input())
    height = int(input())
    print(f'Width = Height = Triangle Area = {(width*height)*0.5}')

    if input('Continue? ').lower() != 'y':
        break

# 반복 제어문 2 - 형성 평가 1
n = int(input())
for i in range(n):
    print('JUNGOL')

# 반복 제어문 2 - 형성 평가 2
n, m = map(int, input().split())
if n > m:
    n, m = m, n
for i in range(n, m+1):
    print(i, end=' ')

# 반복 제어문 2 - 형성 평가 3
n = int(input())
res = 0
for i in range(0, n+1, 5):
    res += i
print(res)

# 반복 제어문 2 - 형성 평가 4
n = list(map(int, input().split()))
res = sum(n) / len(n)
print(f'{res:.2f}')

# 반복 제어문 2 - 형성 평가 5
arr = list(map(int, input().split()))
even, odd = 0,0
for i in arr:
    if i % 2: odd += 1
    else: even += 1
print(f'even : {even}\nodd : {odd}')

# 반복 제어문 2 - 형성 평가 6
n, m = map(int, input().split())
if n > m : n, m = m, n

ssum, total = 0, 0
for i in range(n, m+1):
    if not (i % 3) or not (i % 5):
        ssum += i
        total += 1
print(f'sum : {ssum}\navg : {ssum / total:.1f}')

# 반복 제어문 2 - 형성 평가 7
n = int(input())
org = n
for i in range(10):
    print(n, end=' ')
    n += org

# 반복 제어문 2 - 형성 평가 8
n, m = map(int, input().split())
for i in range(1, n+1):
    org = i
    for j in range(m):
        print(i, end=' ')
        i += org
    print()

# 반복 제어문 3 - 형성 평가 9
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f'({i}, {j})', end=' ')
    print()

# 반복 제어문 3 - 형성 평가 10
a, b = map(int, input().split())
if a > b:
    arr = [i for i in range(a, b-1, -1)]
else:
    arr = [i for i in range(a, b+1)]
# print(arr)

for i in range(1, 10):
    for j in arr:
        print(f'{j} * {i} = {i*j:2d}', end='   ')
    print()

#  반복 제어문 3 - 형성 평가 1
for i in range(48, 91):
    print(f'{i} - {chr(i)}')

#  반복 제어문 3 - 형성 평가 2
# print(chr(97), chr(122))
n = int(input())
for i in range(1, 27):
    if not (i % n):
        print(chr(i+96), end='')

# 반복 제어문 3 - 형성 평가 3
n = int(input())
for i in range(1, n+1):
    print('*' * i)
for j in range(n-1, 0, -1):
    print('*' * j)

# 반복 제어문 3 - 연습문제 4
n = int(input())
space = ' '
ast = '*'
for i in range(n-1, -1, -1):
    print(f'{space * i}{ast * (n-i)}')

# 반복 제어문 3 - 자가 진단 4
n = int(input())
space = ' '
ast = '*'
for i in range(n):
    print(' '* i + '*' * (n - i))

# 반복 제어문 3 - 형성 평가 4
n = int(input())
# arr = [ i for i in range(n+2, 0, -2) ]
# print(list(enumerate(arr)))
#
# for i, j in enumerate(arr):
#     print((' ' * i) + ('*' * j) + (' ' * i))
for i in range(n, 1, -1):
    print(' '*(n-i), '*'*(2*i-1), ' '*(n-i), sep = '')
for i in range(1, n+1):
    print(' '*(n-i), '*'*(2*i-1), ' '*(n-i), sep = '')

# 반복 제어문 3 - 형성 평가 5
n = int(input())
std = 2*n - 1
for i in range(1, std + 1, 2):
    # print(i)
    print(' ' * (std - i) + '*' * i)

# 반복 제어문 3 - 형성 평가 6
n = int(input())
for i in range(1, n+1):
    print('  ' * (n - i), end='')
    for j in range(1, i+1):
        print(j, end=' ')
    print()


# 반복 제어문 3 - 연습 문제 6
n = int(input())

res = 64  # 아스키코드를 이용해야 하므로 초기값이 64
for i in range(1, n+1):  # 1부터 n까지 순회
    for j in range(1, i+1):  # i행이면 i개의 요소를 출력해야 하므로 이렇게 for문 구성
        res += 1  # res는 하나씩 올려준다
        print(chr(res), end='')
    print()


# ⭐⭐⭐⭐ 반복 제어문 3 - 형성 평가 7
n = int(input())

first = 64
second = -1
for i in range(n, 0, -1):
    # 알파벳에 대한 for문
    for j in range(i, 0, -1):
        first += 1
        print(chr(first), end=' ')
    # 숫자에 대한 for문
    for k in range(n-i):
        second += 1
        print(second, end=' ')
    # 알파벳과 숫자가 한 줄에 나와야 하므로 두 for문이 끝나면 엔터 치기
    print()

# 반복 제어문 3 - 형성 평가 8
n = int(input())

res = 0
# 숫자가 역순으로 출력되므로 range도 역순으로
for i in range(n, 0, -1):
    # 공백 출력하기
    # 주어진 수와 출력되는 수의 차이만큼 공백 출력
    print('  ' * (n - i), end='')

    #  숫자 출력하기
    for j in range(i):
        res += 1
        print(res, end=' ')
    # 한 줄 끝내기
    print()

# 반복 제어문 3 - 형성 평가 9
n = int(input())

# 정방향 출력
for i in range(1, n+1):
    # for j in range(1, i+1):
    print('# ' * i)
# 역방향 출력
for ii in range(n-1, 0, -1):
    print('  ' * (n - ii) + '# ' * ii)

# 반복 제어문 3 - 형성 평가 10
n = int(input())
arr = [ i for i in range(1, 10, 2) ]
# print(arr)

cnt = 0
while cnt < n*n:
    for i in arr:
        if cnt == n*n:
            break
        if not (cnt % n):
            print()
        print(i, end=' ')
        cnt += 1
