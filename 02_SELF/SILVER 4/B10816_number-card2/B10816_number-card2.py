import sys
from collections import Counter
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
compared = list(map(int, input().split()))
res = Counter(cards)

for com in compared:
    if res.get(com):
        print(res[com], end=' ')
    else:
        print(0, end=' ')