'''
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''

# solution
N = int(input())
nums = input()
sum = 0
for num in nums:
    sum += int(num)
print(sum)