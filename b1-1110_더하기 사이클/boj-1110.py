import sys

sys.stdin = open('sample_input.txt')

for _ in range(7):
    N = int(input())
    cnt = 0
    num = N
    while True:
        a = num // 10
        b = num % 10
        c = (a+b) % 10
        num = (b*10) + c
        cnt += 1
        if num == N:
            break
    print(cnt)

# N = sys.stdin.readline().rstrip()

# if len(N) < 2:
#     S = 0
#     E = int(N)
# else:
#     S = int(N[0])
#     E = int(N[1])
#
# new_s, new_e = E, int(str(S+E)[-1])
# cnt = 1
# while not (new_s == S and new_e == E):
#     tmp = new_s + new_e
#     new_s = new_e
#     new_e = int(str(tmp)[-1])
#
#     cnt += 1
# print(cnt)


