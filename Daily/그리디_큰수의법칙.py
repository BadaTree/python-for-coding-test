N,M,K = map(int, input().split()) 
data = []
k = 0
sum = 0

for _ in range(N):
    data.append(int(input()))
data.sort(reverse=True)

for _ in range(0,M):
    if not(k > K):
        sum += data[0]
        k += 1
    else:
        k = 0
        sum += data[1]
print(sum)
         
            
# NOTE: 큰 수의