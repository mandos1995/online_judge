n, m = map(int, input().split())
card = list(map(int,input().split()))
card_sum = []

for i in range(n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            card_sum.append(card[i] + card[j] + card[k])
data = [m] * len(card_sum)

for i in range(len(data)):
    data[i] -= card_sum[i]
    if data[i] < 0:
        data[i] = 300001

print(m - min(data))