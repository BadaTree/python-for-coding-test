# TODO : 0717 백준 풀이

# [ ] 백준 2559 수열 

import sys

data = sys.stdin.read().strip().splitlines()
N,K = map(int,data[0].split(' '))
nums = list(map(int,data[1].split(' ')))
max_sum = 0

for t in range(N):
    temp = sum(nums[t:t+K])
    if max_sum < temp :
        max_sum = temp
print(max_sum)

import sys

input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
K = int(data[1])
nums = list(map(int, data[2:]))

# 첫 번째 K일의 합을 초기 최대 합으로 설정
current_sum = sum(nums[:K])
max_sum = current_sum

# 슬라이딩 윈도우 기법으로 최대 합 계산
for i in range(K, N):
    current_sum += nums[i] - nums[i - K]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)