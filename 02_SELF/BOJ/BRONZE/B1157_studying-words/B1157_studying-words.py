# 소요시간 15분
import sys

sys.stdin = open('input.txt')

# for _ in range(4):
STR = input()

cnt_ls = [0] * 26

# print(ord('A'), ord('Z'), ord('a'), ord('z'))

for s in STR:
    num = ord(s)
    if num <= 90: num -= 65
    elif num <= 122: num -= 97
    cnt_ls[num] += 1

mmax = -1
cnt = 0
max_num = 0
for r in range(0, 26):
    if mmax < cnt_ls[r]:
        mmax = cnt_ls[r]
        cnt = 0
        max_num = r + 65
    if mmax == cnt_ls[r]: cnt += 1
if cnt > 1: print('?')
else: print(chr(max_num))