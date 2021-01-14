'''
문제
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
'''

# solution
num1, num2, num3 = map(int, input().split())
print((num1+num2)%num3)
print(((num1%num3)+(num2%num3))%num3)
print((num1*num2)%num3)
print(((num1%num3)*(num2%num3))%num3)