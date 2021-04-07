num = int(input())
line = 0 # 대각선
max_num = 0 # 대각선중 가장 큰 수
while num > max_num:
    line += 1
    max_num += line
gap = max_num - num # 입력받은 수와 차이
if line % 2 == 1:
    top = gap + 1
    bottom = line - gap
else:
    top = line - gap
    bottom = gap + 1
print(top,bottom,sep='/')