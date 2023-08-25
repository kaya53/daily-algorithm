# 소요시간 30분
# 문제에서 하라는 대로만 하면 되는 문제!
import sys

sys.stdin = open('input.txt')


def queueing(now):
    bigger = max(queue)
    bigger_idx = -1
    for z in range(len(queue)):
        if now < queue[z] <= bigger:
            bigger = queue[z]
            bigger_idx = z
    return bigger_idx


P = int(input())
for _ in range(P):
    bundle = list(map(int, input().split()))

    queue = []
    cnt = 0
    for i in range(1, len(bundle)):
        now_student = bundle[i]
        if i == 1:
            queue.append(now_student)
            continue
        for k in queue:
            if k > now_student:
                insert_idx = queueing(now_student)
                cnt += len(queue) - insert_idx  # 삽입하는 부분 다음부터 뒤로 밀려난다!
                queue.insert(insert_idx, now_student)
                break
        else:  # 내 앞은 다 나보다 작음
            queue.append(now_student)
        # print(queue, cnt)
    print(bundle[0], cnt)
