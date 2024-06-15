# # # TODO : 간단하게 코드 사용할 때 사용하는 메모장 노트

# # # import sys

# # input = sys.stdin.read
# # data = input().split()

# # data = list(map(int,data[1:]))

# # data.sort()

# # for i in data :
# #     print(i)

# # # 백준 1427
# # N = list(input())

# # N.sort(reverse=True)

# # print(''.join(N))

# # 백준 2720

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


# 백준 1979

# N = int(input())
# nums = list(map(int,input().split()))

# print(sum([1 for num in nums if len([i for i in range(2, num) if num % i == 0]) == 0 and num > 1]))


# 백준 2581
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

from collections import Counter

x_list = []
y_list = []
for i in range(3):
    x,y = input().split(" ")

    x_list.append(x)
    y_list.append(y)

x_Count = Counter(x_list)
y_Count = Counter(y_list)

print(next(x for x in x_Count if x_Count[x]==1),next(y for y in y_Count if y_Count[y]==1))