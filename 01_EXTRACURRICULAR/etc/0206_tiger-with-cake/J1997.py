import sys

sys.stdin = open('input.txt')


def fibo(n):
    fibo_ls = [1, 1]
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        fibo_ls.append(fibo_ls[i-1] + fibo_ls[i-2])
    return fibo_ls

fibo_ls = fibo(30)

D, K = map(int, input().split())

x = 1
a = fibo_ls[D-3]
b = fibo_ls[D-2]
while True:
    tmp = (K-(a*x)) % b
    if not tmp:
        y = (K - (a * x)) // b
        if x <= y:
            print(x, y, sep='\n')
            break
    else:
        x += 1