# TODO: 스택 자료 구조
#[x]: 먼저 들어온 데이터가 나중에 나가는 자료구조
#Python에서는 list의 .append, pop을 이용해서 스택 구현 가능
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