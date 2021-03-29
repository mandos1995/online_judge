a, b, c = map(int,input().split())
sum = a + b + c
avg = round((sum / 3), 2)
print("%d %.2f"% (sum,avg))