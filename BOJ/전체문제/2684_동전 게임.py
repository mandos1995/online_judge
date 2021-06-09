p = int(input())
result = [0] * 8
for i in range(p):
    coin = input()
    result = [0] * 8
    for j in range(38):
        if coin[j:j+3] == 'TTT':
            result[0] += 1
        elif coin[j:j+3] == 'TTH':
            result[1] += 1
        elif coin[j:j + 3] == 'THT':
            result[2] += 1
        elif coin[j:j+3] == 'THH':
            result[3] += 1
        elif coin[j:j+3] == 'HTT':
            result[4] += 1
        elif coin[j:j+3] == 'HTH':
            result[5] += 1
        elif coin[j:j+3] == 'HHT':
            result[6] += 1
        elif coin[j:j+3] == 'HHH':
            result[7] += 1
    print(*result)
