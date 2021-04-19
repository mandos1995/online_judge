n = int(input())
input_n_list = list(map(int, input().split()))
m = int(input())
input_m_list = list(map(int, input().split()))

for i in range(m):
    if input_m_list[i] in input_n_list:
        print(1)
    else:
        print(0)