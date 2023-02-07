import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    initial = input()
    N = len(initial)

    stick = sliced = i = 0
    while i < N:
        if initial[i] == '(':
            if initial[i+1] == '(':
                stick += 1
                i += 1
            elif initial[i+1] == ')':
                sliced += stick
                i += 2
        elif initial[i] == ')':
            if initial[i-1] == ')':
                stick -= 1
                sliced += 1
                i += 1
    print(f'#{tc} {sliced}')
    

## 스택을 이용하면 쉽게 풀리는 문제 - 나중에 열린 괄호가 먼저 닫히기 때문
# 스택 이용해서 풀어보기