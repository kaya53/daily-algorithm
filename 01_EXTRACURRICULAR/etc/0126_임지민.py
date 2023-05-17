### 리스트 3
## 형성평가 1
n = int(input())
res = ['No.'+str(i) for i in range(1, n+1)]
print(res)

# 형성 평가 2
n, m = map(int, input().split())
res = [bool(not(i%m)) for i in range(n)]
print(res)

# 형성 평가 3
arr = list(map(int, input().split()))
kkey = [i for i in range(1, 7)]
dice = dict.fromkeys(kkey, 0)
for i in arr:
    dice[i] += 1
for i in range(1, 7):
    print(f'{i} : {dice[i]}')

# 형성 평가 4
arr = list(map(int, input().split()))
dic = {}
for num in arr:
    score = num // 10
    kkey = score*10
    if dic.get(kkey):
        dic[kkey] += 1
    else:
        dic[kkey] = 1
for i in sorted(list(dic.keys()), reverse=True):
    print(f'{i} : {dic[i]} person')

# 형성 평가 5
n, m = map(int, input().split())
arr = [n, m]
for i in range(2, 10):
    res = (arr[i-2]+arr[i-1]) % 10
    arr.append(res)
print(*arr)

# 형성 평가 6
a = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
ssum = 0
for i in range(4):
    print(*a[i])
    for j in range(3):
        ssum += a[i][j]
print(ssum)

# 형성 평가 7
res = []
for i in range(1, 5):
    msg = str(i)+'class? '
    nums = list(map(int, input(msg).split()))
    res.append(sum(nums))
for j in range(4):
    print(f'{j+1}class : {res[j]}')

# 형성 평가 8
arr = [[0 for _ in range(7)] for _ in range(5)]
arr[0][1] = arr[0][3] = arr[0][5] = 1

for i in range(1, 5):
    if not (i % 2): k = 1
    else: k = 2
    for j in range(k, 6, 2):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

for i in range(5):
    print(*arr[i][1:6])

# 형성 평가 9
arr = [[] for _ in range(2)]
for i in range(2):
    if i == 0: print('first array')
    if i == 1: print('second array')
    for _ in range(2):
        arr[i].append(list(map(int, input().split())))
# print(arr)
res =[[None for _ in range(3)] for _ in range(2)]
for i in range(2):
    for j in range(3):
        res[i][j] = arr[0][i][j] * arr[1][i][j]
for elem in res:
    print(*elem)

## 형성 평가 10
import math
arr = [[]*2 for _ in range(4)]
for i in range(4):
    nums = list(map(int, input().split()))
    arr[i] = nums

# 가로 평균
for elem in arr:
    print(math.trunc(sum(elem) / 2), end=' ')
print()
# # 세로 평균
whole_sum = 0
for i in range(2):
    ssum = 0
    for j in range(4):
        ssum += arr[j][i]
    whole_sum += ssum
    print(math.trunc(ssum / 4), end=' ')
print()
print(math.trunc(whole_sum / 8))

# 형성 평가 11
n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    arr[i][0] = 1
    arr[i][i] = 1
# print(arr)
for i in range(2, n):
    for j in range(1, n-1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for elem in arr[::-1]:
    for num in elem:
        if num != 0:
            print(num, end=' ')
    print()


# 형성 평가 12
arr = [[] for _ in range(3)]
for i in range(3):
    strs = input().split()
    arr[i] = strs
# print(arr)
for elem in arr:
    for alp in elem:
        print(alp.lower(), end=' ')
    print()


## 함수 1
# 형성 평가 1
def call_at():
    return '@' * 10

for elem in ['first', 'second', 'third']:
    print(elem)
    print(call_at())

# 형성 평가 2
def sum_to_n(n):
    ssum = 0
    for i in range(1, n+1):
        ssum += i
    return ssum


n = int(input())
print(sum_to_n(n))

## 형성 평가 3
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end=' ')
    print()

# 형성 평가 4
def squares(n, m):
    if n > m :
        n, m = m, n
    return m*m - n*n


n, m = map(int, input().split())
print(squares(n,m))

## 형성 평가 5
arr = [[] for _ in range(4)]
for i in range(3):
    scores = list(map(int, input().split()))
    arr[i].extend(scores)
    arr[i].append(sum(scores))

for j in range(4):
    ssum = 0
    for k in range(3):
        ssum += arr[k][j]
    arr[3].append(ssum)

for elem in arr:
    print(*elem)
