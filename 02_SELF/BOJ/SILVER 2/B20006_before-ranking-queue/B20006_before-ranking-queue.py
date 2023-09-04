# 소요시간 30분 python 52ms
# 구현 문제
import sys

sys.stdin = open('input.txt')

P, M = map(int, input().split())
room = []
# rid = 0
for _ in range(P):
    level, name = input().split()
    # print(level, name, rid)
    level = int(level)
    if not room:
        room.append([(level, name)])
    else:
        for rid in range(len(room)):
            now = room[rid]
            if len(now) < M and now[0][0] - 10 <= level <= now[0][0] + 10:
                now.append((level, name))
                break
        # 들어갈 방이 없음
        else:
            room.append([(level, name)])


for r in room:
    r.sort(key=lambda x: x[1])
    if len(r) == M:
        print('Started!')
        for res in r:
            print(*res)
    else:
        print('Waiting!')
        for res in r:
            print(*res)
