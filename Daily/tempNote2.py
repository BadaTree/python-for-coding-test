# [ ] 백준 1002 
'''
import math

def isPossible(x,y,xt,yt,r):
    R = math.sqrt((xt-x)**2+(yt-y)**2)
    return R == r 

def find_poits(x,y,r):
    result = set()
    
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if isPossible(x,y,i,j,r):
                result.add((i,j))
    return result
# 교집합 원소를 찾으면 되니까 조규현의 가능 좌표들만 체크 
def find_poits2(x,y,r,points):
    result = set()
    
    for px,py in points:
        if isPossible(x,y,px,py,r):
                result.add((px,py))
            
    return result

x1_set = set()
x2_set = set()

T = int(input()) 

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 조규현 - 류재명 거리로 찾은 예산 위치 
    x1_set = find_poits(x1,y1,r1)
        
    # 백승환 - 류재명 거리로 찾은 예산 위치
    x2_set = find_poits2(x2,y2,r2,x1_set)

    # 두 Set의 교집합 즉 류재명 가능 위치 수 출력
    print(len(x2_set))

import math

def find_intersection_count(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이의 거리
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # 동일한 중심
    if d == 0:
        if r1 == r2:
            return -1  # 무한히 많은 교점
        else:
            return 0  # 교점 없음
    
    # 두 원이 서로 만나지 않는 경우
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0  # 교점 없음
    
    # 외접하거나 내접하는 경우
    if d == r1 + r2 or d == abs(r1 - r2):
        return 1  # 한 개의 교점
    
    # 그 외의 경우 (두 개의 교점)
    return 2

# 입력 처리
T = int(input())
results = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    results.append(find_intersection_count(x1, y1, r1, x2, y2, r2))

# 결과 출력
for result in results:
    print(result)
'''

    
# [ ] 백준 5597
'''
import sys

students = sys.stdin.read().splitlines()

set_stud = set(list(map(int,students)))
set_nums = set([i for i in range(1,31)])

# 제출하지 않은 학생의 출석번호 구하기
result = list(set_nums - set_stud)

# 오름차순으로 정렬
result.sort()

[print(n) for n in result]
'''
'''
N,M = map(int,input().split(' '))

print((N-1) + N*(M-1))

'''

# [ ] 백준 3052
'''
import sys

nums = sys.stdin.read().splitlines()
result = set()

for num in nums:
    result.add(int(num)%42)
    
print(len(result))

'''

# [ ] 백준 1546
'''
N = int(input())

scores = map(int,input().split(' '))
best = max(scores)

NewScores = [ score / best*100 for score in scores]

print(round(sum(NewScores)/len(NewScores),6))
'''

# [ ] 백준 27433

'''
N = int(input())
answer = 1

for n in range(1,N+1):
    answer *= n

print(answer)
'''

N = int(input())
result = [0,1]

def fibo(i):
    result.append(result[i-1] + result[i-2])
i = 2

while i <= N:
    fibo(i)
    i += 1
    
print(result[N])
    