def solution(board, moves):
    answer = 0
    stack = []

    for line in moves:
        for idx in range(len(board)):
            if board[idx][line-1] != 0:
                stack.append(board[idx][line-1])
                board[idx][line-1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
        #print(stack, answer)
    return answer