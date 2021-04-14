'''
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

# solution
C = int(input())
ratio = []
for i in range(C):
    N = list(map(int,input().split()))
    score = 0
    avg = 0
    count = 0
    for j in range(1,len(N)):
        score += N[j]
    avg = score/N[0]
    for k in range(1,len(N)):
        if avg < N[k]:
            count += 1
    ratio.append(count/N[0]*100)
for list in ratio:
    print("%.3f%%" % list)