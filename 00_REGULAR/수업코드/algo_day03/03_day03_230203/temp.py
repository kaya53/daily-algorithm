A = '1234'
B = map(int, A)
print(B)

for x in B:
    print(x, end=' ')


A = [(1, 0), (2, 4), (3, 3), (3, 2), (5, 5), (5, 1)]
B = [[1, 0], [5, 5], [2, 4], [3, 3], [3, 2], [5, 1], [5, 3]]
C = sorted(B)
print(C)

def func1(k, sushi_dict, belt):
    cnt = 0
    for i in range(k):
        cnt += not sushi_dict[belt[i]]

def func2(k, sushi_dict, belt):
    cnt = 0
    for i in range(k):
        if sushi_dict[belt[i]] == 0:
            cnt += 1


import dis

dis.dis(func2)