a,b = input().split()

list_1 = [[]]
list_2 = [[]]
final_list = [[]]

for i in range(int(a)):
    temp_1 = []
    temp_1 = input().split()
    for j in range(int(b)):
        print(temp_1)
        list_1[i][j] = int(temp_1[j])
for i in range(int(a)):
    temp_1 = []
    temp_2 = []
    temp_1 = input().split()
    temp_2 = input().split()
    for j in range(int(b)):
        print(temp_1)
        list_1[i][j] = int(temp_1[j])
        list_2[i][j] = int(temp_2[j])
final_list[i][j] =  list_1[i][j] +  list_2[i][j]
print(final_list)
