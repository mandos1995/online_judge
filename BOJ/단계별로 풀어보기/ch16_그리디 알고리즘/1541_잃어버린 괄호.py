string = input().split('-')
sum = 0

# '-' 가 없이 '+'로만 이루어진 경우도 있을 수 있음
for i in string[0].split('+'):
    sum += int(i)
for i in string[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)