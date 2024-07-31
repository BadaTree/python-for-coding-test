# [ ] 백준 1009번
'''
import sys

input = sys.stdin.read().splitlines()
N = int(input[0])

for i in range(1, N + 1):
    a, b = map(int, input[i].split())
    result = pow(a, b, 10)

    print(10 if result == 0 else result)
'''

# [ ] hash 응용 문제 1. 점수 한 개 저장
'''
import sys

scores = {}
input = sys.stdin.read().splitlines()
N = int(input[0])

for i in range(1,N+1):
    name, score = input[i].split(' ')
    scores[name] = int(score)
    
print(scores)
'''
# [ ] hash 응용 문제 2. 점수 여러 개 저장
'''
import sys

scores = {}
input = sys.stdin.read().splitlines()
N = int(input[0])

for i in range(1,N+1):
    info = input[i].split(' ')
    scores[info[0]] = list(map(int,info[1:]))
    
print(sum(scores['bada'][:])//len(scores['bada'][:]))

# GPT 풀이
import sys

scores = {}
input = sys.stdin.read().splitlines()
N = int(input[0])

for i in range(1, N + 1):
    info = input[i].split()
    student_name = info[0]
    student_scores = list(map(int, info[1:]))
    scores[student_name] = student_scores

# 'bada' 학생의 점수 평균 계산
bada_scores = scores.get('bada', [])
if bada_scores:
    average_score = sum(bada_scores) // len(bada_scores)
    print(average_score)
else:
    print("No scores available for 'bada'")
'''

# [ ] hash 응용 문제 3. 문자열 내 문자 빈도 수 
# 특정 문장을 입력 받아 알파벳의 빈도 수 계산 및 각 알파벳 빈도 수 출력
'''
input_msg = input().strip()

alpha_freqency = {}

for alpha in input_msg:
    alpha_freqency[alpha]=alpha_freqency.get(alpha,0) + 1

print(alpha_freqency)
'''

# [ ] backjoon ZOAC 4 
'''
H,W,N,M = map(int,input().split())
current_W = 1
current_H = 1
countW = 1
countH = 1 

for i in range(1,W+1):
    if current_W+N+1 <= W :
        current_W += N+1
        countW += 1
for j in range(1,H+1):
    if current_H+ M+1 <= H:
        current_H += M+1  
        countH += 1  

print(countW*countH)

# 두번 째 방법
H, W, N, M = map(int, input().split())

# H에서 (N+1) 간격으로 배치 가능한 행의 수 계산
rows = (H // (N + 1)) + (1 if H % (N + 1) > 0 else 0)

# W에서 (M+1) 간격으로 배치 가능한 열의 수 계산
columns = (W // (M + 1)) + (1 if W % (M + 1) > 0 else 0)

# 전체 배치 가능한 사람 수는 열과 행의 곱
print(columns * rows)
'''