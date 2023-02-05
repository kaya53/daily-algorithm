def d(n):
    ssum = n
    std = n  # 오히려 얘를 쓰는게 메모리를 덜 쓴다
    for i in range(len(str(std)) - 1):
        ssum += (n % 10)
        n //= 10

    return ssum + n


arr = [0] * 10001  # 생성자를 담는 배열
for i in range(10001):
    if d(i) <= 10000:
        arr[d(i)] += 1

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)
