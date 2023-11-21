import sys

def get_value(x, y):
  if y == 1: return x % INF
  elif not y % 2:
    res = get_value(x, y/2)
    return (res**2) % INF
  else:
    res = get_value(x, (y-1)/2)
    return (res*res*x) % INF

cnt = 0
K, P, N = map(int, input().split())
INF = 1000000007

a = K%INF
b = get_value(P, 10*N) % INF
print((a*b)%INF)