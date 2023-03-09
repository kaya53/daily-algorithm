import sys

sys.stdin = open('input.txt')


def myOperator(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2

def dfs(index, value):
    global result

    if index == n - 1:
        result = max(result, value)
        return

    if index + 2 < n:
        res = myOperator(value, s[index + 1], int(s[index + 2]))
        dfs(index + 2, res)

    # 4개까지만 보는 이유는 더 이상을 보면 어차피 그 나머지 반에서 보기 때문에 굳이 그럴 필요가 없음
    if index + 4 < n:
        res = myOperator(value, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4])))
        dfs(index + 4, res)

for _ in range(6):
    n = int(input())
    s = input()
    result = -1 * sys.maxsize


    dfs(0, int(s[0]))
    print(result)