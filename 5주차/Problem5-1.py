def check(str):
    correct = True
    left = 0
    right = 0
    stack = []

    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            stack.append('(')
        else:
            right += 1
            if len(stack) == 0:
                correct = False
            else:
                stack.pop()

        if left == right:
            return i + 1, correct


def solution(p):
    if len(p) == 0:
        return p

    pos, correct = check(p)

    u = p[:pos]
    v = p[pos:]

    if correct:
        return u + solution(v)

    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer