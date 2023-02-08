n = int(input())

def fact(n):
    if n == 1:
        print(f'{n}! = {n}')
        return n
    print(f'{n}! = {n} * {n-1}!')
    return n * fact(n-1)


print(fact(n))