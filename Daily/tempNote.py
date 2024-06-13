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


while True:
    n,m = input().split(' ')
    n,m = int(n), int(m)
    if n == 0 or m == 0:
        break
    check = max(n,m) % min(n,m) == 0 
    if not check :
        print("neither")
    elif n < m and check:
        print("factor")
    else:
        print("multiple")