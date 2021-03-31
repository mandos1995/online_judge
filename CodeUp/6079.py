sum = 0
num = int(input())
for i in range(1,num+1):
    sum += i
    if sum >= num:
        print(i)
        break