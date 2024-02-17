def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    stack.append(0)
    for i in range(1, n):
        curr = numbers[i]
        while stack:
            # 뒤 큰 수 찾음
            if numbers[stack[-1]] < curr:
                answer[stack.pop()] = curr
            else:
                break
        stack.append(i)

    return answer