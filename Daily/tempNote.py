# # # TODO : 간단하게 코드 사용할 때 사용하는 메모장 노트

# # import sys

# input = sys.stdin.read
# data = input().split()

# data = list(map(int,data[1:]))

# data.sort()

# for i in data :
#     print(i)

# [ ] 백준 1427
# N = list(input())

# N.sort(reverse=True)

# print(''.join(N))

# [ ] 백준 2720

# N = int(input())
# moneys = [25,10,5,1]

# for i in range(N) :
#     pay = int(input())
#     result = []
#     for money in moneys :
#         result.append(str(int(pay / money)))
#         pay = pay % money
  
#     print(' '.join(result))


# while True:
#     n,m = input().split(' ')
#     n,m = int(n), int(m)
#     if n == 0 or m == 0:
#         break
#     check = max(n,m) % min(n,m) == 0 
#     if not check :
#         print("neither")
#     elif n < m and check:
#         print("factor")
#     else:
#         print("multiple")

# N,K = map(int,input().split(' '))
# factor = [i for i in range(1,N+1) if N%i == 0]

# print(factor[K-1] if len(factor)>= K else 0)

# while True:
#     N = int(input())
#     if N == -1 :
#         break
#     factor = [i for i in range(1,N) if N%i == 0]
#     if N == sum(factor): # 완전수라면
#         print( f"{N} = " + " + ".join(map(str, factor)))
#     else :
#         print(f"{N} is NOT perfect.")


#[ ] 백준 1979

# N = int(input())
# nums = list(map(int,input().split()))

# print(sum([1 for num in nums if len([i for i in range(2, num) if num % i == 0]) == 0 and num > 1]))


#[ ] 백준 2581
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# N = int(input())
# M = int(input())
# result = [num for num in range(N, M + 1) if is_prime(num)]

# print(f"{sum(result)}\n{min(result)}") if result else print(-1)

# print(4 ** 0.5,sqrt(4))

# x, y, w, h = map(int,input().split(' '))
# point=[(x,0),(0,y),(x,h),(w,y)]

# print(int(min([(((x-i)**2+(y-j)**2)**0.5) for i,j in point])))

# from collections import Counter

# x_list = []
# y_list = []
# for i in range(3):
#     x,y = input().split(" ")

#     x_list.append(x)
#     y_list.append(y)

# x_Count = Counter(x_list)
# y_Count = Counter(y_list)

# print(next(x for x in x_Count if x_Count[x]==1),next(y for y in y_Count if y_Count[y]==1))

# [ ] 백주 9063
# N = int(input())

# max_x = -100000
# min_x = 100000
# max_y = -100000
# min_y = 100000


# for i in range(N):
#     if N == 1:
#         break
    
#     x,y = map(int,input().split(' '))
#     if x > max_x:
#         max_x = x
#     if x < min_x:
#         min_x = x
#     if y > max_y:
#         max_y = y
#     if y < min_y:
#         min_y = y

# print((max_x-min_x)*(max_y-min_y) if N != 1 else 0)

# [ ] 백준 5073

# import sys

# data = sys.stdin.read().split()
# set_tri = set()

# for i in range(0,len(data),3):
#     triangle = [int(data[i]),int(data[i+1]),int(data[i+2])]
  
#     if triangle == [0,0,0]:
#         break
#     else:
#         # 삼각형의 조건을 만족하지 못할 때
#         if max(triangle) >= (sum(triangle)-max(triangle)):
#             print("Invalid")
#         else :
#             set_tri = set(triangle)
#             if len(set_tri) == 1:
#                 print("Equilateral")
#             if len(set_tri) == 2:
#                 print("Isosceles")
#             if len(set_tri) == 3:
#                 print("Scalene")

# import sys

# input_data = sys.stdin.read().strip().splitlines()

# for line in input_data:
#     a, b, c = map(int, line.split())
    
#     if a == 0 and b == 0 and c == 0:
#         break
    
#     sides = [a, b, c]
#     sides.sort()  # 세 변의 길이를 오름차순으로 정렬
    
#     if sides[2] >= sides[0] + sides[1]:
#         print("Invalid")
#     elif a == b == c:
#         print("Equilateral")
#     elif a == b or b == c or c == a:
#         print("Isosceles")
#     else:
#         print("Scalene")

# nums = list(map(int,input().split(' ')))
# nums.sort(reverse = True)

# # 삼각형의 조건을 만족할 때
# if nums[0]< nums[1]+nums[2] :
#     print(sum(nums))
# else :
#     print((nums[1]+nums[2])*2 -1)

# import sys


# a,b,c= map(int,sys.stdin.read().splitlines())

    
# if sum([a,b,c]) != 180 :
#     print("Error")
# elif a == b == c :
#     print("Equilateral")
# elif a==b or b==c or c==a:
#     print("Isosceles")
# else:
#     print("Scalene")
    
# n = int(input())
# print(2 *( n + 2))


import sys

N = int(input())

scores = []
for i in range(N):
    score = input()
    scores.append(int(score))

scores.sort()
for i in scores:
    print(i)