# 출력 - 형성평가 1
print('My name is Hong')

# 출력 - 형성평가 2
print('My hometown \nFlowering mountain')

# 출력 - 형성평가 3
for i in range(5):
    if i < 2:
        print('T'*10)
    else:
        print('    TT    ')

# 출력 - 형성평가 4
dic = { 'kor' : 90, 'mat' : 80, 'eng' : 100 }
key = list(dic.keys())
ssum = 0
for elem in key:
    print(f'{elem} {dic[elem]}')
    ssum += dic[elem]
print(f'sum {ssum}')
print(f'avg {ssum//3}')

# 변수와 입력 - 형성평가 1
a, b, c = 10, 20, 30
print(f'{a} + {b} = {c}')

# 변수와 입력 - 형성평가 2
a, b = 80.5, 22.34
print(f'{a} {b} {a+b}')

# 변수와 입력 - 형성평가 3
a, b= 10.5, 50
print(f'{a} * {b} = {a*b}')

# 변수와 입력 - 형성평가 4
a = int(input())
b = int(input())
c = int(input())

print(f'sum = {a+b+c}')
print(f'avg = {(a+b+c)//3}')

# 변수와 입력 - 형성평가 5
a = float(input('yard? '))
print(f'{a} yard = {a*91.44} cm')

# 연산자 - 형성평가 1
kor = int(input())
eng = int(input())
mat = int(input())
com = int(input())

print(f'sum {kor+eng+mat+com}')
print(f'avg {(kor+eng+mat+com)//4}')

# 연산자 - 형성평가 2
a = int(input())
b = int(input())
print(f'{a} / {b} = {a//b} ... {a%b}')

# 연산자 - 형성평가 3
width = int(input()) + 5
length = int(input()) * 2
print(f'width = {width}')
print(f'length = {length}')
print(f'area = {width*length}')

# 연산자 - 형성평가 4
a = int(input())
b = int(input())
a += 1
print(f'{a} {b}')
b -= 1
print(f'{a} {b}')


# 연산자 - 형성평가 5
bro = int(input('Brother? '))
sis = int(input('Sister? '))
if bro != sis: print(True)
else: print(False)

# 연산자 - 형성평가 6
m_height = int(input())
m_weight = int(input())
k_height = int(input())
k_weight = int(input())

if m_height > k_height and m_weight > k_weight : print(True)
else: print(False)

# 연산자 - 형성평가 7
a = input()
b = input()
print(f'{a} and {b}')
print(f'{a}&{b}')

# 연산자 - 형성평가 8
a = input()
b = input()
c = int(input())

print(f'{b*c}{a}')

