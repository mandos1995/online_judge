board = [['W','F','W','F','W','F','W','F'],
         ['F','W','F','W','F','W','F','W'],
         ['W','F','W','F','W','F','W','F'],
         ['F','W','F','W','F','W','F','W'],
         ['W','F','W','F','W','F','W','F'],
         ['F','W','F','W','F','W','F','W'],
         ['W','F','W','F','W','F','W','F'],
         ['F','W','F','W','F','W','F','W'],]

chess = []
count = 0
for _ in range(8):
    chess.append(input())

for i in range(8):
    for j in range(8):
        if board[i][j] == 'W' and chess[i][j] == 'F':
            count += 1
print(count)
