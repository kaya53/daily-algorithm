import sys

sys.stdin = open('input.txt')

while True:
    a, b, c = map(int, input().split())
    if not a and not b and not c: break

    if a == b == c: print('Equilateral')
    elif (a+b <= c) or (a+c <= b) or (b+c <= a):
        print('Invalid')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('Isosceles')
    elif a != b != c: print('Scalene')

