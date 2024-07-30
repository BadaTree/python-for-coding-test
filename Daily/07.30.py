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
    
# [ ] hash 응용 문제 3. 문자열 내 문자 빈도 수 
 