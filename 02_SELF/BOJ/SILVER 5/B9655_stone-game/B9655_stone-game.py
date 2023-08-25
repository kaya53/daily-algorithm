# 소요시간: 20분
# 내가 풀었지만 풀고도 어이가 없다... 이게 뭐지
# 어려워 보이는데 생각해보면 쉬운 문제다
import sys

sys.stdin = open('input.txt')


N = int(input())
if N%2: print('SK')
else: print('CY')