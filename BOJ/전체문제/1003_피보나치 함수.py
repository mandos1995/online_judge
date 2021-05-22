def fibonacci(n):
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 1)
    else:
        temp = 0
        current = 1
        before = 0
        for i in range(n - 1):
            temp = current
            current = before + temp
            before = temp

        print(before, current)

t = int(input())
for _ in range(t):
    num = int(input())
    fibonacci(num)

