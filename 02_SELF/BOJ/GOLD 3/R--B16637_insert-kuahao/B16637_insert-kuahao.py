import sys

sys.stdin = open('input.txt')

# import math

def calc(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2


def dfs(idx, value):
    global mmax

    if idx == n - 1: # 끝까지 다 연산했으면
        if mmax < value:
            mmax = value
        return

    if idx + 2 < n:  # 2칸 간 게 인덱스 안일 때만
        print(calc(value, line[idx+1], int(line[idx+2])))
        dfs(idx+2, calc(value, line[idx+1], int(line[idx+2])))

    if idx + 4 < n:
        tmp = calc(int(line[idx+2]), line[idx+3], int(line[idx+4]))
        print(calc(value, line[idx+1], tmp))
        dfs(idx+4, calc(value, line[idx+1], tmp))


# 이렇게 comb를 짜면 주어진 숫자의 순서가 움직이지는 않음 
# but 괄호가 여러개여야 하는 데 이건 어떡하징

# for _ in range(6):
n = int(input())
line = input()
mmax = (2**31)*(-1)

cnt = 0
# 가능한 숫자 순서
dfs(0, int(line[0]))
print(mmax)