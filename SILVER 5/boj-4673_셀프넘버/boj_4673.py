def d(n):
    ssum = n
    for i in range(len(str(n))):
        ssum += (n % 10)
        n %= 10

    return ssum

for i in range(1, 11):
    print(d())