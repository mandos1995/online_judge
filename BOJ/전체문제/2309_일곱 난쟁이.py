people_9 = [0] * 9
for i in range(9):
    people_9[i] = int(input())
sum = sum(people_9)
people1 = 0
people2 = 0

for i in range(8):
    for j in range(i + 1, 9):
        if sum - (people_9[i] + people_9[j]) == 100:
            people1 = people_9[i]
            people2 = people_9[j]
people_9.remove(people1)
people_9.remove(people2)
people_9.sort()

for i in range(len(people_9)):
    print(people_9[i])
