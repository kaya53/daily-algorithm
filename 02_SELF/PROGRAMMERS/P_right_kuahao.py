def solution(s):
    answer = True

    stack = []
    for char in s:
        if not stack:
            if char == ')':
                return False
            else:
                stack.append(char)
        else:
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
    if stack:
        return False
    return True