n = int(input())
time = 3600 * (n + 1)
hour = time // 3600
count = 0
for i in range(time):
    hour = i // 3600
    min = (i % 3600) // 60
    sec = (i % 3600) % 60
    if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
        count += 1
    print(hour, min, sec)
print(count)