# 정렬이 필요한 지
# - 정렬 후에 불필요한 조건이 없기 때문에 정렬을 하는 것이 유리할 수 있음
# 잘려진 조각을 어떻게 관리할 지
#
import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
num = int(input())
i_ls = [0]
j_ls = [0]
for _ in range(num):
    s, e = map(int, input().split())
    if not s: i_ls.append(e)
    else: j_ls.append(e)

i_ls.append(N)
j_ls.append(M)
i_ls.sort()
j_ls.sort()
res = 0
for ii in range(len(i_ls)-1):
    for jj in range(len(j_ls)-1):
        width = i_ls[ii+1] - i_ls[ii]
        height = j_ls[jj+1] - j_ls[jj]
        res = max(res, width*height)
print(res)