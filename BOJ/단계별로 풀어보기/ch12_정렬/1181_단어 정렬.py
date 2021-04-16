n = int(input())
word = []
for _ in range(n):
    word.append(input())
word = list(set(word))
word.sort(key=str.lower)
word.sort(key=lambda x:len(x))
for i in range(len(word)):
    print(word[i])