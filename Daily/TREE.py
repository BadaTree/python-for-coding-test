# [ ] Tree 개념 
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
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
