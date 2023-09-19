# 소요시간 40분 => pypy 180ms, python 80ms
# 순서대로 연산할 때는 stack을 사용하자
import sys

sys.stdin = open('input.txt')


def calc(ls):
    nums = []
    oprs = []
    i = 0
    while i < 2*N - 1:
        curr = ls[i]
        if i % 2:
            if curr == '+' or curr == '-':
                oprs.append(curr)
                i += 1
            else:
                n1 = nums.pop()
                n2 = ls[i+1]
                nums.append(int(str(n1)+str(n2)))
                i += 2
        else:  # 숫자
            nums.append(curr)
            i += 1
    n1 = nums[0]
    for k in range(len(oprs)):
        n2 = nums[k+1]
        o = oprs[k]
        if o == '+': n1 += n2
        else: n1 -= n2
    if n1 == 0:
        print(''.join(map(str, ls)))


def dfs(idx, ls):
    if idx == N-1:
        # print(ls+[N])
        calc(ls+[N])
        return
    for opr in [' ', '+', '-']:
        dfs(idx+1, ls+[idx+1, opr])


T = int(input())
for _ in range(T):
    N = int(input())
    dfs(0, [])
    print()
