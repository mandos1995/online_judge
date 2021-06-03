while True:
    string = input()
    if string == '#':
        break
    else:
        list_string = list(string.split())
        for i in range(len(list_string)):
            print(list_string[i][::-1],end=' ')