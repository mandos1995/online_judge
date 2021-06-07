n = int(input())
people = [0] * 101
result = 0
input_data = list(map(int,input().split()))
for i in input_data:
    people[i] += 1
for i in range(101):
    if people[i] > 1:
        result += people[i] - 1
print(result)