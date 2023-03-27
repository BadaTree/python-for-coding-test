n = int(input())
list = input().split()
v = int(input())
count = 0
for i in range(n):
    list[i] = int(list[i])
    if v == list[i]:
        count += 1
print(count)
