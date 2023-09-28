# 소요시간: 40분 pypy 648ms, python 시간 초과

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input().rstrip())
word_dict = {}
for _ in range(N):
    inp = input().rstrip()
    if word_dict.get(inp[0], -1) == -1:
        word_dict[inp[0]] = [1, [(len(inp), inp)]]
    else:
        word_dict[inp[0]][0] += 1
        word_dict[inp[0]][1].append((len(inp), inp))

# print(word_dict)

res = 0
res_a = ''
res_b = ''
for L, val in word_dict.values():
    if L < 2: continue
    for i in range(L):
        me_l, me = val[i]
        for j in range(i+1, L):
            you_l, you = val[j]
            if me == you: continue
            idx = 0
            while idx < min(me_l, you_l):
                if me[idx] == you[idx]: idx += 1
                else: break
            if res < idx:
                res = idx
                res_a, res_b = me, you
print(res_a, res_b, sep='\n')


