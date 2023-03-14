import sys

sys.stdin = open('sample_input.txt')


def check(now, count):
    if now == 0:
        if count[now] and count[now+1] and count[now+2]:
            return True
    elif now == 9:
        if count[now-2] and count[now-1] and count[now]:
            return True
    else:
        if count[now] and count[now+1] and count[now+2]:
            return True
        if count[now-2] and count[now-1] and count[now]:
            return True
        if count[now - 1] and count[now] and count[now+1]:
            return True
    return False

t = int(input())
for tc in range(1, t+1):
    inp = list(map(int, input().split()))
    player1 = inp[::2]
    player2 = inp[1::2]

    count1 = [0] * 10
    count2 = [0] * 10
    res1 = res2 = 0
    for i in range(6):
        now1, now2 = player1[i], player2[i]  # 현재 숫자
        count1[now1] += 1
        count2[now2] += 1
        # 1번이 먼저 가져가기 때문에 1번이 먼저 run, triplet이 나오면 무조건 이김
        if count1[now1] >= 3 or check(now1, count1):
            res1 = 1
            break
        if count2[now2] >= 3 or check(now2, count2):
            res2 = 2
            break

    if not res1 and not res2:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {res1 if res1 else res2}')