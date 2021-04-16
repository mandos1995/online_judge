l = int(input())
alpha = input()
sum = 0
j = 0
for i in alpha:
    sum += (ord(i) - 96) * (31 ** (j))
    j += 1
print(sum % 1234567891)
