import math
n1, n2 = map(int, input().split())
print(math.gcd(n1, n2))
print(n1 * n2 // math.gcd(n1, n2))
