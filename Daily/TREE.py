# [ ] Tree 개념 
# https://blog.naver.com/zzzxxx3166/223533254579
# [나동빈 트리 핵심 요약 & 구현](https://www.youtube.com/watch?v=i5yHkP1jQmo)
# [이진트리의 구현 및 순회 알고리즘]


# # [ ] 트리의 순회 구현하기
# class Node:
#     def __init__(self,data,left_node,right_node):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node
        
# # 전위 순회(Preorder Traversal) 부모 -> 왼쪽자식 -> 오른자식
# def pre_order(node):
#     print(node.data,end=' ')
#     if node.left_node != None :
#         pre_order(tree[node.left_node])
#     if node.right_node != None:
#         pre_order(tree[node.right_node])
        
# # 중위 순회(Inorder Traversal) 왼쪽자식 -> 부모 -> 오른자식
# def in_order(node):
#     if node.left_node != None:
#         in_order(tree[node.left_node])
#     print(node.data,end=' ')
#     if node.right_node !=None:
#         in_order(tree[node.right_node])

# # 후위 순회(Postorder Traversal) 왼쪽자식 ->  오른자식 부모 ->
# def post_order(node):
#     if node.left_node != None:
#         post_order(tree[node.left_node])
#     if node.right_node != None:
#         post_order(tree[node.right_node])
#     print(node.data, end=' ')
    
# n = int(input())
# tree = {}

# for i in range(n):
#     data, left_node, right_node = input().split()
#     if left_node == "None":
#         left_node = None
#     if right_node == "None":
#         right_node = None
#     tree[data] = Node(data,left_node,right_node)

# '''
# # 트리구조를 저장한 Tree 딕셔너리의 모습 
# {
#     1: Node(1, 2, 3),
#     2: Node(2, 4, 5),
#     3: Node(3, None, None),
#     4: Node(4, None, None),
#     5: Node(5, None, None)
# }

# '''
    
# pre_order(tree['A'])
# print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])

# [ ] 실습
# Node 클래스 생성
class Node:
    def __init__(self,data, left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        

def pre_order(node):
    print(node.data,end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.left_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None :
        in_order(tree[node.left_node])
    print(node.data, end =' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node :
        post_order(tree[node.right_node])
    print(node.data,end=' ')
    
N = int(input())
tree = {}
# 노드들의 객체를 생성하고, 노드가 이어진 트리를 딕셔너리로 구현 
for i in range(N):
    value,left_node, right_node = input().split(' ')
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[value] = Node(value,left_node,right_node)
    
pre_order(tree['A']) # 시작은 항상 루프 노드에서    
print()
in_order(tree['A'])
print()
post_order(tree['A'])


# [ ] Class 기본 개념 및 생성 해보기
# https://blog.naver.com/zzzxxx3166/223538539678

# Q. 'Student' 클래스를 생성하여, name, age, student_id, courses 속성을 저장하고, 아래 메서드를 정의.
# 'enroll': courses을 등록하는 메서드, 'list_courses' : self.courses를 출력하는 메서드, 
# 'introduce': f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."를 출력하는 메서드

'''
class student:
    # 생성자 메서드
    def __init__(self, name, age,student_id):
        self.name = name # 속성
        self.age = age # 속성
        self.student_id = student_id # 속성
        self.course = []# 속성
        
    # 메서드들
    def eroll(self,course):
        self.course.append(course)
        print(f"{self.name} has enrolled in {course}")

    def list_courses(self):
        return self.course
    
    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."
    
# 객체 생성
alice = student("alice", 15, 1729)
tom = student("tom", 16,134)

# 수업 등록 
alice.eroll("History 101")
tom.eroll("math 201")

# 수업 리스트 출력
print(alice.list_courses())
print(tom.list_courses())

# 자기소개 
print(alice.introduce())
print(tom.introduce())

'''
# [ ] 트리 관련 코테 문제

# [1] 트리 순회(백준 1991, 실버 1)
# https://www.acmicpc.net/problem/1991

# [2] 트리 부모 찾기 (백준 11725, 실버2)
# https://www.acmicpc.net/problem/11725

# [3] 트리의 지름 (백준 1167, 골드 2)
# https://www.acmicpc.net/problem/1167

# [4] 트리의 지름 (백준 1967, 골드 4)
# https://www.acmicpc.net/problem/1967

# [5] 트리(백준 1068, 골드 5)
# https://www.acmicpc.net/problem/1068

# [6] 이진 검색 트리 (백즌 5639, 골드4)
# https://www.acmicpc.net/problem/5639

# [7] 상근이의 여행 (백준 9372, 실버4)
# https://www.acmicpc.net/problem/9372

# [8] 전화번호 목록 (백준 5051, 골드4)
# https://www.acmicpc.net/problem/5052

# [9] 트리의 순회 (백준 2263, 골드 1)
# https://www.acmicpc.net/problem/2263
