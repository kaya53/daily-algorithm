# 나의 풀이
# 1. 각 i 마다 왼손을 움직이는 경우, 오른손을 움직이는 경우로 나눈다.
# 2. 그리고 dp[i-1][0] = min(dp[i-1][0][2]+위치를 고려한 가중치, dp[i-1][1][2] + 위치를 고려한 가중치)
# 3. 같은 경우는 무조건 이 경우를 선택하고, 두 가중치가 같으면서 위치가 같으면 가중치가 더 작은 걸 택한다.

# 정답 풀이
# - 각 i마다 왼손 한 경우, 오른손 한 경우로 제한하는 것이 아니라 가능한 모든 경우를 해봐야 한다.
# - 그래서 매 i마다 가능한 경우의 수가 최대 2**i가지이다.

costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
    , [7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
    , [6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
    , [7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
    , [5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
    , [4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
    , [5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
    , [3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
    , [2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
    , [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]


def solution(numbers):
    now_weight = 0
    left_pos = 4
    right_pos = 6
    all_dict = {}
    finger_pos = (left_pos, right_pos)
    all_dict[finger_pos] = now_weight

    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger_pos, weight in all_dict.items():
            left_pos, right_pos = finger_pos
            if right_pos == num:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + 1:
                    curr_dict[(left_pos, num)] = weight + 1
            elif left_pos == num:
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + 1:
                    curr_dict[(num, right_pos)] = weight + 1
            else:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + costs[right_pos][
                    num]:
                    curr_dict[(left_pos, num)] = weight + costs[right_pos][num]
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + costs[left_pos][
                    num]:
                    curr_dict[(num, right_pos)] = weight + costs[left_pos][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))