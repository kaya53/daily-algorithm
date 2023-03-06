### J1141 불쾌한 날과 스택 사용하는 로직이 유사
import sys
from collections import deque

sys.stdin = open('input.txt')

init = input()

res = deque()
opr = deque()
opr_dict = {'+' : 1, '-': 1, '*' : 2, '/': 2}

# line 23 else문 정리 전
# for elem in init:
#     if elem.isalpha():  # 숫자이면
#         res.append(elem)  # 결과 스택에 무조건 넣기
#     else:
#         if not opr:  # 연산자 스택이 비었으면
#             opr.append(elem)  # 일단 더해주기
#         else:
#             # 연산자 스택에 있는 애의 우선 순위가 들어올 연산자의 우선순위보다 낮으면 더하기
#             if opr_dict[opr[-1]] < opr_dict[elem]:
#                 opr.append(elem)
#             else:  # 우선순위가 작거나 같으면 pop
#                 # while opr:  ### 다 털어버려서 생기는 문제; 나보다 우선 순위가 큰 애가 없을 때까지만 털면 됨
#                 while opr and opr_dict[opr[-1]] >= opr_dict[elem]:
#                     res.append(opr.pop())
#                 # 내 우선순위가 가장 작을 때까지 빼주고 연산자 넣기
#                 opr.append(elem)
# while opr:  # 스택에 남은 연산자들 털어주기
#     res.append(opr.pop())
#
# print(''.join(map(str, res)))


for elem in init:
    if elem.isalpha():  # 숫자이면
        res.append(elem)  # 결과 스택에 무조건 넣기
    else:
        if not opr:  # 연산자 스택이 비었으면
            opr.append(elem)  # 일단 더해주기
        else:  # 연산자 스택이 차있으면
            # 나보다 작거나 같은 연산자가 나오면 빼서 res로 보내기
            while opr and opr_dict[opr[-1]] >= opr_dict[elem]:
                res.append(opr.pop())
            # 다 빼주고 일단 들어온 연산자는 더해주기
            opr.append(elem)
while opr:  # 스택에 남은 연산자들 털어주기
    res.append(opr.pop())

print(''.join(map(str, res)))