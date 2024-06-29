import math

def find_point(x,y,xt,yt,r):
    R = math.sqrt((xt-x)**2+(yt-y)**2)
    if R == r :
        return True 
    else :
        return False
    
x1_set = set()
x2_set = set()

T = int(input()) 
x1,y1,r1,x2,y2,r2 = map(int,input().split(' '))
print(x1,y1,r1,x2,y2,r2)

# 조규현 - 류재명 거리로 찾은 예산 위치 
for i in range(-10000,10001):
    for j in range(-10000,10001):
        if find_point(x1,y1,i,j,r1):
            x1_set.add((i,j))
    

# 백승환 - 류재명 거리로 찾은 예산 위치
for i in range(-10000,10001):
    for j in range(-10000,10001):
        if find_point(x2,y2,i,j,r2):
            x2_set.add((i,j))

# 두 Set의 교집합 즉 류재명 가능 위치 수 출력
print(len(x1_set&x2_set))