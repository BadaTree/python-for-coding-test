# TODO : DFS & BFS Algorithm

#[ ] DFS(Depth-Firsh Search), 스택 자료 구조
# 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.
# DFS는 스택자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 
# 있으면 그 노드를 스택에 넣고 방문 처리한다. 
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리 
    visited[v] = True
    print(v,end= ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i ,visited)
            
# 각 노드가 연결된 정보 표현 
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

# 각 노드가 방문된 정보를 표현
visited =[False]*9

# 정의된 BFS 함수 호출
dfs(graph,1,visited) #1->2->7->6->3->4->5
print("")

#[ ] BFS(Breadth-Firsh Search), 큐 자료 구조
# BFS는 너비 우선 탐색이라고하며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
# BFS는 큐 자료구조를 이용하며, 구체적인 동작은 다음과 같다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드를 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다. 


from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
                
# 각 노드가 연결된 정보 표현 
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

# 각 노드가 방문된 정보를 표현
visited =[False]*9

# 정의된 BFS 함수 호출
bfs(graph,1,visited) # 1->2->3->8 ->7->4 -> 5->6
print("")

# 각 노드가 연결된 정보 표현 
def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)
            
            
from collections import deque

def BFS(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True 



graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]


visited = [False]*9

BFS(graph,1,visited)
print("")
DFS(graph,1,visited)