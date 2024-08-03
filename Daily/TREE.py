# [ ] Tree 개념 
# https://blog.naver.com/zzzxxx3166/223533254579

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

    def insert_left(self, current_node, new_value):
        if current_node.left is None:
            current_node.left = Node(new_value)
        else:
            new_node = Node(new_value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        if current_node.right is None:
            current_node.right = Node(new_value)
        else:
            new_node = Node(new_value)
            new_node.right = current_node.right
            current_node.right = new_node

    def get_root(self):
        return self.root

    def traverse_preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

# Example usage
tree = BinaryTree(1)
root = tree.get_root()
tree.insert_left(root, 2)
tree.insert_right(root, 3)
tree.insert_left(root.left, 4)
tree.insert_right(root.left, 5)
tree.insert_left(root.right, 6)
tree.insert_right(root.right, 7)

# Traverse the tree in preorder to verify the structure
tree.traverse_preorder(tree.get_root())  # Output: 1 2 4 5 3 6 7
        
# [1]전위 순회(Preorder Traversal)
def pre_order(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order(tree.get(node.left_node))
        pre_order(tree.get(node.right_node))

# 입력 받기
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
            
    tree[data] = Node(data, left_node, right_node)

# [2] 중위 순회(Inorder Travelsal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data,end = ' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
# [3] 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data,end=' ')
    
    
# 'A' 노드를 루트로 하는 전위 순회
pre_order(tree['A']) 
print()
in_order(tree['A'])
print()
post_order(tree['A'])




# from collections import deque

# def levelOrder(root):
#     if root is None :
#         return 0
#     visited = []
#     q = deque()
#     q.append(root)
    
#     while q:
#         cur_node = q.popleft()
#         visited.append(cur_node.value)
        
#         if cur_node.left:
#             q.append(cur_node.left)
#         if cur_node.right:
#             q.append(cur_node.right)
#     return visited

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
