def solution(board, moves):
    stack = [0]
    moves = list(map(lambda x : x - 1 , moves))
    answer = 0
    for i in range(len(moves)):
        point = moves[i]
        for j in range(len(board)):
            if board[j][point] == 0:
                continue
            else:
                stack.append(board[j][point])
                board[j][point] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer