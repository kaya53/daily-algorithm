def to_minute(str):
    tmp = str.split(':')
    return int(tmp[0]) * 60 + int(tmp[1])


def solution(book_time):
    answer = 0
    book_time.sort()
    rooms = []
    for a, b in book_time:
        start = to_minute(a)
        end = to_minute(b)
        # print(a, start)
        # print(b, end)
        for i in range(len(rooms)):
            if start >= rooms[i][1] + 10:
                rooms[i] = [start, end]
                break
        else:
            rooms.append([start, end])
        # print(rooms)

    return len(rooms)