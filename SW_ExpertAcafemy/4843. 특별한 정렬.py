# TODO: 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 

'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''

case = int(input())

for i in range(1,case+1):
    n = int(input())
    result = []
    numList = list(map(int,input().split(' ')))
    
    for j in range(n):
        if j % 2 == 0 : # 홀수번 인덱스에는 가장 큰 수 
            max_num = max(numList) # 리스트의 가장 큰 수 찾기
            result.append(max_num) # 결과 리스트에 추가
            numList.remove(max_num) # 정렬한 값은 리스트에서 삭제 
        else: 
            min_num = min(numList) # 리스트의 가장 큰 수 찾기
            result.append(min_num) # 결과 리스트에 추가
            numList.remove(min_num) # 정렬한 값은 리스트에서 삭제
    print(f"#{i} {' '.join(map(str,result))}")