n = input()
sort_num = []
for i in n:
    sort_num.append(i)
sort_num.sort(reverse=True)
print(''.join(sort_num))