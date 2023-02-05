a = list(map(lambda x: x.upper(), input())) # 여서 문제고: Map + string 연산 유의하기
b = list(set(a))  # z
c = [0] * len(b)  # [0]

# 데이터 채워넣기
for x in range(len(b)):  # 0
    for y in a:  # y: z
        if y == b[x]: # True
            c[x] += 1 # c = [1]

# 최댓값 찾아봐
for i in range(len(c)):  # 1
    for j in range(i+1, len(c)):  # 2, 1
        if c[j] < c[i]:
            c[i], c[j] = c[j], c[i]
            b[i], b[j] = b[j], b[i]

# 최댓값이 중복이면
if c[-1] == c[-2]: print("?")
else: print(b[-1])