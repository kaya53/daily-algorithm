t = int('68B46DDB9346F4', 16)
print((bin(t))[2:])

e = int('328D1AF6E4C9BB', 16)
e = list(map(int, bin(e)[2:]))
e = [0]*(56-len(e)) + e

for x in range(0, 50, 7):
    print(e[x:x+7])
    # 1 4 4 6 8 2 2 7

# print(e)
# lenb = len(bin(e)[2:])
# print(bin(e)[2:], type(bin(e)[2:]))
# for b in range(lenb):
#     pass
print()
t= int('1DB176C588D26EC', 16)
t = ''.join(map(str, bin(t)[2:]))
print(len(t), t)
# t = list(map(int, bin(t)[2:]))
# print(len(t))
# print(t.rstrip())
res = []
for s in '1DB176C588D26EC':
    x = int(s, 16)
    print(bin(x)[2:])
    res.append(bin(x)[2:])