def char_to_num(char):
    if char == 'first': return 0
    elif char == 'second': return 1
    elif char == 'third': return 2
    elif char == 'fourth': return 3
    elif char == 'last': return -1  # 5번째 주가 될수도 있지만 4번째 주가 될 수도 있으므로 -1로 처리함


def mon_to_num(char):
    if char == 'january': return 1
    elif char == 'february': return 2
    elif char == 'march': return 3
    elif char == 'april': return 4
    elif char == 'may': return 5
    elif char == 'june': return 6
    elif char == 'july': return 7
    elif char == 'august': return 8
    elif char == 'september': return 9
    elif char == 'october': return 10
    elif char == 'november': return 11
    elif char == 'december': return 12


def day_to_num(char):
    if char == 'sunday': return 0
    elif char == 'monday': return 1
    elif char == 'tuesday': return 2
    elif char == 'wednesday': return 3
    elif char == 'thursday': return 4
    elif char == 'friday': return 5
    elif char == 'saturday': return 6


# 왜 res에 365/366일의 정보를 모두 담아놨냐면
# 인풋으로 주어진 요일 하나하나를 볼 때, 어차피 주어진 모든 요일이 같은 로직 그러니까 같은 해이기 때문에
# 한 번만 구해놓고, 인풋에 대해서는 하나하나 접근해서 찾는 게 더 효율적이고, 연산 횟수를 줄일 수 있다고 생각함
def get_days(is_yun):
    months = [31, 28, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]
    last_date = [0] * 12
    res = []
    for i in range(12):
        curr_date = (last_date[i-1] + 1) % 7 if i else jan_num  # 요일을 숫자로 변환한 것
        end = 29 if i == 1 and is_yun == 'leap' else months[i]  # 날짜
        d = 1  # 날짜
        now = {}
        while d <= end:
            if now.get(curr_date, -1) != -1: now[curr_date].append(d)
            else: now[curr_date] = [d]
            curr_date = (curr_date + 1) % 7
            d += 1
            if d == end: last_date[i] = curr_date
        res.append(now)
    return res


yun = input()
jan_first = input()
T = int(input())
days = [input().split() for _ in range(T)]

jan_num = day_to_num(jan_first)
std_dict = get_days(yun)
for day in days:
    nth = char_to_num(day[0])
    date = day_to_num(day[1])
    mon = mon_to_num(day[3])
    print(mon, std_dict[mon-1][date][nth])

