# [ ] Graph에 대해 이해해보자 

'''
# 깊이 우선 탐색 스택으로 구현 (선입후출) # 1 2 7 6 8 3 4 5
            
def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            DFS(graph,i,visited)
            
from collections import deque

def BFS(graph,v,visited):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
    ]

visited = [False] * 9
visited_bfs = [False] * 9 

DFS(graph,1,visited)
print()
BFS(graph,1,visited_bfs)
'''

# [1] 7576번: 토마토 (골드 5)
# https://www.acmicpc.net/problem/7576

# [2] 2606번: 바이러스 (실버 3)
# https://www.acmicpc.net/problem/2606
'''
V = int(input())
E = int(input())


def DFS(graph,v,visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i] :
            DFS(graph,i,visited)
    return sum(visited) - 1

graph = [[] for i in range(V+1)]
# DFS로 연결된 컴퓨터 끝까지 탐색하여 카운트

# Graph 그리기 
for i in range(E):
    a,b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    
visited =[False]*(V+1)

print(DFS(graph,1,visited))
'''
# [3] 1012번: 유기농 배추 (실버 2)
# https://www.acmicpc.net/problem/1012
# 행 N(y),열 M(x)


import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    points[x][y] = False  # 방문 처리하기
    for j in range(4):
        temp_x = x + x_move[j]
        temp_y = y + y_move[j]
        
        if 0 <= temp_x < N and 0 <= temp_y < M:
            if points[temp_x][temp_y]:  # 인접한 배추가 있다면!
                DFS(temp_x, temp_y)  # 인접 배추 위치로 이동

# 테스트 케이스 개수
Case = int(input().strip())

for _ in range(Case):
    M, N, K = map(int, input().strip().split())

    points = [[False] * M for _ in range(N)]
    spots = []

    x_move = [-1, 1, 0, 0]
    y_move = [0, 0, -1, 1]

    count = 0

    # 배추가 심어져 있는 땅 표시
    for i in range(K):
        y, x = map(int, input().strip().split())
        points[x][y] = True
        spots.append([x, y])

    # 배추 새로운 묶음 위치 찾기
    for spot in spots:
        if points[spot[0]][spot[1]]:
            DFS(spot[0], spot[1])
            count += 1  # 인접한 배추 모음 1개 카운트  

    print(count)
     
                

# [4] 2178번: 미로 탐색 (실버 1)
# https://www.acmicpc.net/problem/2178

# [5] 2667번: 단지번호붙이기 (실버 1)
# https://www.acmicpc.net/problem/2667




