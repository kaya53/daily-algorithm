# 소요시간 40분 python 3888ms
# 문제는 어렵지 않으나
# - nums의 input 처리가 까다롭고
# - 마지막 답을 str로 변환해서 제출해야 하는 문제였음
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(func, nums):
    leng = len(func)
    pIdx = 0
    for i in range(leng):
        if func[i] == 'R':
            if not pIdx: pIdx = -1
            else: pIdx = 0
            continue
        if nums:
            nums.pop(pIdx)
        else:
            return 'error'
    if pIdx == -1:
        return '['+ ','.join(map(str, nums[::-1])) + ']'
    return '['+ ','.join(map(str, nums)) + ']'


T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = []
    for k in input().rstrip()[1:-1].split(','):
        if k.isdigit(): nums.append(int(k))
    print(solution(p, nums))
