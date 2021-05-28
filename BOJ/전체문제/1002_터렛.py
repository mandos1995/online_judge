import math
n = int(input())

for _ in range(n):
    # 원의 방정식을 이용해 두 터렛의 거리를 구함
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 중심거리와 두 원의 위치 관계식을 이용하여 두 원의 접점 개수를 알아낸다.
    if distance == 0 and r1 == r2: # 두 원이 동심원이고 반지름이 같을때
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: # 내접, 외접일 때
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2): # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    else:
        print(0)