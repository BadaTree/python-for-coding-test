# TODO : 2024.06.01 코테스터디 해쉬 관련 자유 문제 


# [ ] 의상 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578 


# [ ] 메뉴 리뉴얼 (level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# [ ] 패션왕 신해빈 (실버 3, 백준)
# https://www.acmicpc.net/problem/9375


# TODO: Hash 관련 추천 문제를 풀어보자 

# [ ]나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

pocket_num = {}
pocket_name = {}

# 포켓몬 정보 받아 도감에 저장하기
index = 2
for i in range(1, N + 1):
    name = data[index]
    pocket_num[str(i)] = name
    pocket_name[name] = i
    index += 1

# 포켓몬 맞추기 : 숫자 -> 이름, 이름 -> 숫자
for i in range(M):
    info = data[index]
    index += 1
    # 포켓몬 번호가 들어왔을 때
    if info.isdigit():
        print(pocket_num.get(info))
    # 포켓몬 이름 들어올 때
    else:
        print(pocket_name.get(info))

# 2
# N,M = map(int, input().split(' '))
# pocket_list = []

# # 포켓몬 정보 받아 도감에 저장하기
# for i in range(1,N+1):
#     name = input()
#     pocket_list[i] = name

# # 포켓몬 맞추기 : 숫자 -> 이름, 이름 -> 숫자
# for i in range(M):
#     info = input()
#     # 포켓몬 번호가 들어왔을 떄
#     if info.isdigit() :
#         print(f"{pocket_list[info]}")
#     # 포켓몬 이름 들어올 때
#     else :
#         print(f"{pocket_list.index(info)}")

# [ ] 듣보잡
# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

dic1 = {}
dic2 = {}

# 듣도 못한 사람 저장
index = 2
for i in range(N):
    name = data[index]
    dic1[name] = name
    index += 1
    
# 보도 못한 사람 저장
index = N+3
for i in range(N):
    name = data[index]
    dic2[name] = name
    index += 1

# 듣도 보도 못한 사람 카운트
result = []
for v,w in dic1.items():
    if v in dic2:
        result.append(v)
print(f"{len(result)}")
print(f"{result}"+"\n")

# [ ] 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

# [ ] 순위 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/72412