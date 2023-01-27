## 함수 2

# 형성 평가 1
N = int(input())
arr = list(map(int, input().split()))


def sorting(ls):
    return sorted(ls, reverse=True)


print(*sorting(arr))

# 형성 평가 2
import math


def func(n, m):
    if n > m : n, m = m, n
    n, m = math.sqrt(n), math.sqrt(m)
    n = math.ceil(n)
    m = math.ceil(m)

    return len(range(n, m))


n, m = map(float, input().split())
print(func(n, m))

# 형성 평가 3
arr = list(map(int, input().split()))
print(sum(map(abs, arr)))

# 형성 평가 4
n = int(input())


def expo(n):
    exponent = 1
    for _ in range(n):
        exponent *= 2
    return exponent


print(expo(n))


# 형성 평가 5
def func1(*args):
    avg = sum(args) / len(args)
    return round(avg)


def func2(*args):
    ssum = 0
    for num in args:
        ssum += round(num)
    return round(ssum / len(args))


n, m, k = map(float, input().split())
print(func1(n, m, k))
print(func2(n, m, k))

# 형성 평가 6
def bubble(arr, k):
    for i in range(6-k):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


arr = list(map(int, input().split()))
for k in range(3):
    bubble(arr, k)
print(*arr)


## 기타 자료형
# 형성 평가 1
n, m, k = map(float, input().split())
print(f'({round(n+m+k, 3)}, {round(n*m*k, 3)})')

# 형성 평가 2
n = int(input())
arr = []
for _ in range(n):
    att, level = input().split()
    arr.append((att, level))
print(arr)

# 형성 평가 3
arr = input().split()
res = set(arr)
print(*sorted(res))
print(len(res))

# 형성 평가 4
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
for elem in arr1:
    if elem not in arr2:
        res.append(elem)
print(*sorted(set(res)))

# 형성 평가 5
n = int(input())
dic = {}
for i in range(n):
    k, v = input().split()
    dic[k] = v

target = input()
print(dic[target])

# 형성 평가 6
arr = input().split()
dic = {}
for elem in arr:
    if dic.get(elem):
        dic[elem] += 1
    else:
        dic[elem] = 1
# print(dic)

mmin = min(list(dic.values()))
for k, v in dic.items():
    if v == mmin:
        print(k)
print(mmin)
