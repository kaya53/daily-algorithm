import sys

sys.stdin = open('input.txt')


def calc(choice):
    res = nums[0]
    for i in range(n-1):  # choice 배열 크기만큼 순회
        opr = choice[i]
        std = nums[i+1]
        if opr == 0:
            res += std
        elif opr == 1:
            res -= std
        elif opr == 2:
            res *= std
        else:
            if (res < 0 and std < 0) or (res > 0 and std > 0):
                res //= std
            else:
                if res < 0 and std > 0:
                    res *= (-1)
                elif res > 0 and std < 0:
                    std *= (-1)
                res //= std
                res *= (-1)
    return res

def backtrack(idx):
    global mmax, mmin
    # 종료 조건: 연산자를 모두 쓰면
    if idx == ops_num:
        # 이 choice 배열을 가지고 연산하기
        val = calc(choice)
        if mmax < val:
            mmax = val
        if mmin > val:
            mmin = val
        # 최댓값 최소값 갱신
        return

    for i in range(4):  # i: 연산자 번호
        if ops[i]:
            choice[idx] = i  # 연산자 번호 등록
            ops[i] -= 1  # 연산자 하나 빼주기
            backtrack(idx+1)
            choice[idx] = -1  # 원상 복구
            ops[i] += 1


#for _ in range(8):
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
# ops[0]: 덧셈 개수, ops[1]: 뺄셈 개수, ops[2]: 곱셈 개수, ops[3]: 나눗셈 개수

ops_num = n-1
# res = nums[0]  # 처음 숫자
mmax = -int(1e9)
mmin = int(1e9)
choice = [-1] * ops_num
backtrack(0)
print(mmax, mmin, sep='\n')

# print(26//4)

# 백트래킹하면서 연산하는 방식 -> 나눗셈때문에 값이 어그러질 것 같음
# def backtrack(idx):
#     global res
#     # 종료 조건: 연산자를 모두 쓰면
#     if idx == n-1:
#         return
#     # for j in range(idx+1, n):
#     for i in range(4):  # i: 연산자 번호
#         if ops[i]:  # 해당 연산자가 있으면
#             if i == 0:
#                 res += nums[idx+1]
#                 ops[i] -= 1
#                 backtrack(idx+1)
#                 res -= nums[idx+1]
#                 ops[i] += 1
#             elif i == 1:
#                 res -= nums[idx + 1]
#                 ops[i] -= 1
#                 backtrack(idx + 1)
#                 res += nums[idx + 1]
#                 ops[i] += 1
#             elif i == 2:
#                 res *= nums[idx + 1]
#                 ops[i] -= 1
#                 backtrack(idx + 1)
#                 res //= nums[idx + 1]
#                 ops[i] += 1
#             else:
#                 res //= nums[idx + 1]
#                 ops[i] -= 1
#                 backtrack(idx + 1)
#                 res *= nums[idx + 1]
#                 ops[i] += 1