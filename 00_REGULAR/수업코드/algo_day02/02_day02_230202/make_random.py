import random

A = random.random()
B = random.randint(1, 10)
C = random.sample(range(1, 11), 10)  # 뽑는 개수가 population 개수보다 클수 없다
D = random.choice(range(1, 10))
print(A, B, C, D)

help(random.choice)


def unpack_example():
    A = [[1, 2], [3, 4]]
    for x in A:
        L, R = x
        print(x, L, R)
    # [1, 2] 1 2
    # [3, 4] 3 4

    A = [[1, 2], [3, 4]]
    for L, R in A:
        print(L, R)
    # 1 2
    # 3 4

    A = [[1, 2], [3, 4]]
    for i, x in enumerate(A, start=1):
        print(i, x)

    # 1 [1, 2]
    # 2 [3, 4]

    A = [[1, 2], [3, 4]]
    for i, (L, R) in enumerate(A, start=1):
        print(i, L, R)

    # 1 1 2
    # 2 3 4