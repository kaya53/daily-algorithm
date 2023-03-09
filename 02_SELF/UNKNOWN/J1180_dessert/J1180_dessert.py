import sys

sys.stdin = open('input.txt')


def calc(nums, choice):
    calc_stack = []
    opr_stack = []
    # print(choice)
    while choice:
        now_opr = choice.pop()
        num1 = nums.pop()
        # calc_stack.append(num1)
        if now_opr == '.':
            num2 = nums.pop()
            nums.append(int(str(num2)+str(num1)))
        else:
            opr_stack.append(now_opr)
            calc_stack.append(num1)
    calc_stack.append(nums.pop())
    # print(calc_stack, opr_stack)

    res = 0
    while opr_stack:
        val = 0
        num2 = calc_stack.pop()
        num1 = calc_stack.pop()
        opr = opr_stack.pop()
        if opr == '+':
            val = num1 + num2
        elif opr == '-':
            val = num2 - num1
        calc_stack.append(val)
    if not calc_stack[0]:
        return calc_stack[0]
    return -1


def dfs(idx):
    global cnt

    if idx == n-1:  # 0부터 시작-> n-2까지, 1부터 시작 -> n-1까지
        # 연산자 조합을 가지고 연산 시작
        # if choice == ['+']*4 + ['.']*2:
        if not calc(list(nums), list(choice)):
            cnt += 1
            if cnt > 20: return
            for i in range(n-1):
                print(nums[i], choice[i], end=' ')
            print(nums[-1])
        return

    for i in range(3):
        choice[idx] = opers[i]
        dfs(idx+1)
        choice[idx] = 0


n = int(input())  # 총 소의 마리수
opers = ['+', '-', '.']
nums = list(range(1, n+1))
choice = [0] * (n-1)
cnt = 0
dfs(0)
print(cnt)
# print(3**14)  # 4,782,969 - 0.4초 정도 소요