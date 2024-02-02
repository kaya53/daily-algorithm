def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])  # 시간 순 정렬
    plans = [[a, int(b[:2]) * 60 + int(b[3:]), int(c)] for a, b, c in plans]
    time = plans[0][1] - 1
    progress = []
    stop = []  # 스택
    while plans or progress or stop:
        time += 1
        # print(progress)
        if not progress:
            if plans and plans[0][1] == time:
                progress.append(plans.pop(0))
            elif stop:
                progress.append(stop.pop())
            else:
                continue  # 시간만 늘리기
        progress[0][2] -= 1  # 이 부분 playtime이 제대로 연산이 안되서 틀렸었음
        name, start, playtime = progress[0]

        if playtime == 0:
            progress.pop(0)
            answer.append(name)
            # print(answer)
        if plans and plans[0][1] == time:  # 시작할 과제가 있음
            if progress:
                stop.append(progress.pop(0))
            progress.append(plans.pop(0))
            # print(progress)
        # 시작할 과제가 없는데, 시간이 끝남; 이미 progress 비었음
        elif playtime == 0 and stop:
            progress.append(stop.pop())  # 최근에 들어온 것부터
    # print(plans, progress, stop)
    return answer