# 구현 : 머릿 속에 있는 알고리즘을 소스코드로 바꾸는 과정
# ex: problem -> thinking -> solution

# 구현 문제란??
# 풀이는 떠올리기 쉬우나 소스 코드로 옮기는게 어려운 문제

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용됩니다.

for i in range(5):
    for j in range(5):
        print('(',i,',',j, ')', end ='')
    print()

# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.
# 동, 북, 서 , 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx,ny)

