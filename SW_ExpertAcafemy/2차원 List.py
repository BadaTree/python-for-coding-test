# TODO : 2차원 list

arr = [1,2,3]*3
print(f"1차원: {arr}")

arr = [[1,2,3]]*3 
print(f"2차원: {arr}")

arr1 = [i for i in range(8) if i%2==0 ]

brr = [[1,2,3] for i in range(3)]
brr1 = [[i,j] for i in range(3) for j in range(2)]
print(brr1)