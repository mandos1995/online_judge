'''
문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
        472 --------(1)
      X 385 --------(2)
-----------------------
       2360 --------(3)
      3776  --------(4)
     1416   --------(5)
-----------------------
    181720  --------(6)
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
'''

# solution
num1 = int(input())
num2 = int(input())
print(num1*(num2%10)) # num2의 1의 자리
print(num1*((num2%100)//10)) # num2의 10의 자리
print(num1*(num2//100)) # num2dml 100의 자리
print(num1*num2)