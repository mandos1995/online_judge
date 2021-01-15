'''
문제
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
'''

# solution
word = input()
word = word.upper()
list_word = []
list_count = []
count = 0
for words in word:
    list_word.append(words)
for i in range(65, 91):
    list_count.append(list_word.count(chr(i)))
for j in list_count:
    if j == max(list_count):
        count += 1

if count > 1:
    print("?")
else:
    word_index = list_count.index(max(list_count))
    print(chr(word_index + 65))

