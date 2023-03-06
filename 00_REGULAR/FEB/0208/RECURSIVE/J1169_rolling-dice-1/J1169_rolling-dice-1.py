def dice_1(cnt):
    if cnt == n:
        print(' '.join(map(str, choice)))
        return
    for i in range(1, 7):
        choice[cnt] = i
        dice_1(cnt+1)


def dice_2(cnt, ci):
    if cnt == n:
        print(' '.join(map(str, choice)))
        return
    for i in range(ci, 7):
        choice[cnt] = i
        dice_2(cnt+1, i)


def dice_3(cnt, arr):
    if cnt == n:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, 7):
        if i not in arr:  # 얘를 해줘야 해서 부득이하게 arr을 데리고 다녀야 함
            dice_3(cnt+1, arr+[i])


n, m = map(int, input().split())
choice = [0] * n

if m == 1: dice_1(0)
elif m == 2: dice_2(0, 1)
else: dice_3(0, [])