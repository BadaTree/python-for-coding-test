# TODO: DFS & BFS


#[ ] 스택 자료 구조
#[x]: 먼저 들어온 데이터가 나중에 나가는 자료구조 (선입 후출)
# Python에서는 list의 .append, pop을 이용해서 스택 구현 가능
# 박스를 쌓아올리는 모습 상상하기!

list = []

list.append(5)
list.append(2)
list.append(3)
list.append(7)
list.pop()
list.append(1)
list.append(4)
list.pop()

print(list[::-1]) # 최상단 원소부터 출력
print(list) #최하단 원소부터 출력


# [ ] 큐 자료구조
#[x]: 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다.
# 대기열에 줄 선대로 차례대로 나가는 모습 상상!

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제 - 삽입(1) - 삽입(4) - 삭제 ()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 들어온 순서대로
queue.reverse
print(queue) # 나중에 들어온 순서대로 출력

