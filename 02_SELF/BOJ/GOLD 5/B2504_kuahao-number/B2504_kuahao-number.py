# 소요시간 1시간 python 44ms
# indexError 이유
# - 3, 4번째 elif에서 stack[-1], stack[-2]를 보는데 
# 조건을 if stack으로만 줘서 발생함 => if len(stack) > 1로 바꾸니까 통과

# 풀이
# - 입력을 처음부터 하나씩 가서
# - 1. 스택이 비어 있으면 무조건 넣기
# - 2. 스택이 차 있으면
#   - (1)여닫는 괄호가 연속으로 나왔으면 숫자로 변환해서 스택으로 => 스택의 top이 수이면 더해서 넣기
#   - (2)괄호-숫자-괄호 순으로 나왔으면 숫자로 변환에서 스택으로 => 스택의 top이 수이면 더해서 넣기
#   - (1)(2) 모두 해당 사항이 없으면 스택에 넣기

import sys

sys.stdin = open('input.txt')


def solution(inp):
    stack = []
    # 연달아 나오는 것만 거름
    for now in inp:
        if not stack:
            stack.append(now)
        else:
            # 연속 괄호
            if stack[-1] == '(' and now == ')':
                stack.pop()
                if stack and type(stack[-1])==int:
                    stack.append(stack.pop() + 2)
                else:
                    stack.append(2)
            elif stack[-1] == '[' and now == ']':
                stack.pop()
                if stack and type(stack[-1])==int:
                    stack.append(stack.pop() + 3)
                else:
                    stack.append(3)
            elif now == ')' and len(stack) > 1 and type(stack[-1])==int and stack[-2] == '(':
                n = stack.pop()
                stack.pop()  # 여는 괄호
                if stack and str(stack[-1]).isdigit():
                    stack.append(stack.pop() + (n * 2))
                else:
                    stack.append(n * 2)
            elif now == ']' and len(stack) > 1 and type(stack[-1])==int and stack[-2] == '[':
                n = stack.pop()
                stack.pop()  # 여는 괄호
                if stack and type(stack[-1])==int:
                    stack.append(stack.pop() + (n * 3))
                else:
                    stack.append(n * 3)
            else:
                # print('그냥 더함')
                stack.append(now)
            # print('현재 문자열', now)
    if len(stack) == 1 and type(stack[-1]) == int: return stack[0]
    return 0


# for _ in range(4):
stra = list(input())
print(solution(stra))



