import sys

sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)]

choice = [0] * 7
def subset(si, cnt, ssum):
    if cnt == 7:
        if ssum == 100:
            res = list(arr[i] for i in choice)
            for elem in res: print(elem)
            return True
        return False
    for i in range(si, 9):
        choice[cnt] = i
        subset(i+1, cnt+1, ssum+arr[i])
        choice[cnt] = 0

subset(0, 0, 0)