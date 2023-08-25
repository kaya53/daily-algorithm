MIN = int(input())
MAX = int(input())

OVER_MAX = MAX + 1
can_be = [0] * OVER_MAX
can_be[0] = can_be[1] = 1

# 소수 걸러내기
for k in range(2, OVER_MAX):
    for n in range(k+k, OVER_MAX, k):
        can_be[n] = 1

# 소수인 수만 담은 리스트
candidate = [idx for idx, c in enumerate(can_be) if c == 0]

res = [0] * (MAX - MIN + 1)
for n1 in candidate:
    for n2 in candidate:
        if n1 > n2: continue  # 문제 조건 상 n2가 n1보다 커야 함
        calc = n1 * n2
        if MIN <= calc <= MAX:
            res[calc-MIN] += 1
# 소수끼리의 곱 중에서 유일하게 되는 것만 걸러내기
print(res.count(1) + 1)  # 과연 +1을 하는 게 답일까..? 맞다면 왜 해야 할까
