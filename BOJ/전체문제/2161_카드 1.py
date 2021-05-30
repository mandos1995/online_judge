from collections import deque
n = int(input())
card = deque()
deleteCard = []
for i in range(1,n + 1):
    card.append(i)
while True:
    if len(card) == 1:
        break
    deleteCard.append(card.popleft())
    card.append(card.popleft())
deleteCard.append(card[0])
print(*deleteCard)