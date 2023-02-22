import sys

sys.stdin = open('input.txt')

m, n = map(int, input().split())

whole = []
dic = {}
for _ in range(m):
    arr = list(set(map(int, input().split())))
    sort_arr = sorted(arr)
    lenS = len(sort_arr)

    i = {sort_arr[i]: i for i in range(lenS)}
    c = str([i[l] for l in arr])
    dic[c] = dic.get(c, 0) + 1
    print(i)
    print(c)
print(dic)