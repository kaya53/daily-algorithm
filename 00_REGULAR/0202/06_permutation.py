# n개의 순열 구하기
# a = [1, 2, 3, 4]
res = []
# def permutation_01():
#     for i in a:
#         for j in a:
#             for k in a:
#                 if not ((i == j) or (j == k) or (i == k)):
#                     res.append([i, j, k])
#     return res
#
# print(permutation_01())

a= [7,8,5,2]
N = len(a)
def combination_01():
    for i in range(N):
        for j in range(i+1, N):
            res.append((a[i], a[j]))
    return res
def combination_01_b():
    for i in range(N):
        for j in range(i+1, N-1):
            # if i == j: continue
            for k in range(j+1, N):
                # if j == k: continue
                res.append((a[i], a[j], a[k]))
    return res



# print(combination_01())
print(combination_01_b())