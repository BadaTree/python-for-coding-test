# n = int(input())
# list = input().split()
# v = int(input())
# count = 0
# for i in range(n):
#     list[i] = int(list[i])
#     if v == list[i]:
#         count += 1
# print(count)

N, X = input().split()
N = int(N)
X = int(X)
num = input().split()
final = []

for i in range(N):
    if int(num[i])< X:
        final.append(int(num[i]))
print(*final)