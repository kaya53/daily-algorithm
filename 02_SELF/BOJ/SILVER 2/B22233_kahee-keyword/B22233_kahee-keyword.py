# 소요시간 40분
# stdin.readline쓸 때는 반드시 모든 input에 rstrip 해주자ㅎㅎ
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

# for _ in range(2):
N, M = map(int, input().rstrip().split())
word_dict = {}
now = N

for _ in range(N):
    w = input().rstrip()
    word_dict[w] = 1

for _ in range(M):
    ls = input().rstrip().split(',')
    for s in ls:
        if word_dict.get(s):
            word_dict[s] -= 1
            now -= 1
    print(now)