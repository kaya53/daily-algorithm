import sys
from collections import deque

sys.stdin = open('input.txt')

def calc_postfix(opr, n1, n2):
    if opr == '+':
        return n2+n1
    if opr == '-':
        return n2-n1
    if opr == '*':
        return n2*n1
    if opr == '/':
        return n2//n1



for tc in range(1, 11):
    N = int(input())
    init = input()

    res = deque()
    opr = deque()
    opr_dict ={'+': 1, '-': 1, '*': 2, '/': 2}

    for elem in init:
        if elem.isdecimal():
            res.append(int(elem))
        else:  # 연산자이면
            if not opr:
                opr.append(elem)
            else:
                # 내 우선순위보다 작거나 같으면 못들어와
                while opr and opr_dict[opr[-1]] >= opr_dict[elem]:
                    # 여기서 연산을 해도 될 것 같다
                    now_opr = opr.pop()
                    num1 = res.pop()
                    num2 = res.pop()
                    ret = calc_postfix(now_opr, num1, num2)
                    res.append(ret)

                # 나보다 우선순위 작거나 같은 애들을 털어냈거나
                # 원래 있는 애가 나보다 우선순위가 작으면 여기로
                opr.append(elem)
    # 남은 연산자들과 수를 가지고 연산
    # print(res, opr)
    while opr:
        num1 = res.pop()
        num2 = res.pop()
        now_opr = opr.pop()
        ret = calc_postfix(now_opr, num1, num2)
        res.append(ret)
    print(f'#{tc} {res[0]}')