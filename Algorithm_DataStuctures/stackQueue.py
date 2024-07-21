# TODO : Stack과 Queue 

# 스택, 백준 10828 
# https://www.acmicpc.net/problem/10828
'''
import sys

def stack_fun(num_list, command):
    if command == "pop":
        return num_list.pop() if num_list else -1
    elif command == "size":
        return len(num_list)
    elif command == "empty":
        return 1 if not num_list else 0
    elif command == "top":
        return -1 if not num_list else num_list[-1]

input = sys.stdin.read().splitlines()
N = int(input[0])
num_list = []

for i in range(1, N + 1):
    command = input[i]
    if command.startswith("push"):
        _, num = command.split()
        num_list.append(int(num))
    else:
        result = stack_fun(num_list, command)
        print(result)

'''

# 단어 뒤집기, 백준 9093
# https://www.acmicpc.net/problem/9093
import sys
input = sys.stdin.readlines()

N = int(input[0])
for i in range(1,N+1):
    words = input[i].strip().split(' ')
    print(' '.join([word[::-1] for word in words]))

# 괄호, 백준 9012
# https://www.acmicpc.net/problem/9012

# 스택 수열, 백준 1874
# https://www.acmicpc.net/problem/1874

# 에디터, 백준 1406
# https://www.acmicpc.net/problem/1406

# 큐, 백준 10845
# https://www.acmicpc.net/problem/10845

# 요세푸스, 백준 1158
# https://www.acmicpc.net/problem/1158

# 덱, 백준 108866
# https://www.acmicpc.net/problem/10866