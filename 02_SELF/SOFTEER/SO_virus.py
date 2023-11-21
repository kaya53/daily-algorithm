import sys


def get_value(p, n):
  if n == 1: return p % INF

  if not n%2:
    res = get_value(p, n/2)
    return (res*res) % INF
  else:
    res = get_value(p, (n-1)/2)
    return (res*res*p) % INF

K, P, N = map(int, input().split())
INF = 1000000007

a = K % INF
b = get_value(P, N)
print((a*b) % INF)