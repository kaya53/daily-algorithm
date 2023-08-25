# 230804 112ms 37mb => 1시간 반 소요
# 메시지를 나누는 부분 문제를 잘못 이해해서 틀렸었음
import sys

sys.stdin = open('input.txt')


def devide_key():
    mtx = [[0] * 5 for _ in range(5)]
    check = [0] * 26
    # i, j = 0, 0
    k = z = 0
    for i in range(5):
        for j in range(5):
            while k < len(kkey) and check[ord(kkey[k])-65]:
                k += 1
            if k < len(kkey):
                mtx[i][j] = kkey[k]
                check[ord(kkey[k])-65] = 1
                continue

            while check[z] or z == 9: z += 1
            mtx[i][j] = chr(z+65)
            check[z] = 1
    return mtx


def devide_msg():
    msg_ls = list(msg)
    i = 0
    while i < len(msg_ls)-1:
        if msg_ls[i] == msg_ls[i+1]:
            if msg_ls[i] != 'X': msg_ls.insert(i+1, 'X')
            else: msg_ls.insert(i+1, 'Q')
        i += 2

    if len(msg_ls) % 2: msg_ls.append('X')
    return msg_ls


def find_location(char):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == char: return i, j

def secure():
    res = []
    for k in range(0, len(devided),  2):
        i1, j1 = find_location(devided[k])
        i2, j2 = find_location(devided[k+1])
        if i1 == i2:
            j1, j2 = (j1+1) % 5, (j2+1) % 5
        elif j1 == j2:
            i1, i2 = (i1+1) % 5, (i2+1) % 5
        else:
            j1, j2 = j2, j1
        res += [arr[i1][j1], arr[i2][j2]]
    return res

# for _ in range(3):
msg = input()
kkey = input()
arr = devide_key()
devided = devide_msg()
ans = secure()
print(''.join(map(str, ans)))