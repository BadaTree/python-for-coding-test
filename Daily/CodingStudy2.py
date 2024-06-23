# TODO: 24.5.25.토 코테

# [1] 카드2 
'''
https://www.acmicpc.net/problem/2164
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

출력
첫째 줄에 남게 되는 카드의 번호를 출력한다.
'''
from collections import deque


queue = deque()
N = int(input())

for i in range(1,N+1):
    queue.append(i)


while len(queue) > 1:
    queue.popleft() # 짝수번째 단순 삭제

    if len(queue) == 1 :
        break
    queue.append(queue.popleft()) #홀수 번째 선입 삭제 후 맨 뒤에 추가
    
# 큐에 남은 마지막 원소를 출력
print(queue[0])




# [2] 빈도 정렬
'''
https://www.acmicpc.net/problem/2910
위대한 해커 창영이는 모든 암호를 깨는 방법을 발견했다. 그 방법은 빈도를 조사하는 것이다.

창영이는 말할 수 없는 방법을 이용해서 현우가 강산이에게 보내는 메시지를 획득했다. 이 메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 창영이는 이 숫자를 자주 등장하는 빈도순대로 정렬하려고 한다.

만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다.

이렇게 정렬하는 방법을 빈도 정렬이라고 한다.

수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.

입력
첫째 줄에 메시지의 길이 N과 C가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ C ≤ 1,000,000,000)

둘째 줄에 메시지 수열이 주어진다.

출력
첫째 줄에 입력으로 주어진 수열을 빈도 정렬한 다음 출력한다.

'''

# 빈도 수 


# 입력 받기
num, max_n = map(int, input().split())
numList = list(map(int, input().split()))

# 딕셔너리 생성 및 각 수의 빈도수 카운트
countDict = {}
for num in numList:
    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1

# 딕셔너리를 값 기준으로 정렬
sortedDict = sorted(countDict.items(), key=lambda x: (-x[1], numList.index(x[0])))

# 결과 생성
result = ' '.join([str(key) for key, _ in sortedDict for _ in range(countDict[key])])

# 결과 출력
print(result)



# [3] 괄호
'''
https://www.acmicpc.net/problem/9012
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
'''


N = int(input())

for _ in range(N):
    parens = list(input())
    # ( 와 )의 수가 같을 때 즉, VPS일 때
    if parens.count('(') == (len(parens)- parens.count('(')):
        paren = []
        # ( 와 )의 순서 체크 ( 다음 )가 왔을 때만 한 개의 괄호로 인정
        for i in parens:
            if i == '(' :
                paren.append('(')
            elif i == ')' and len(paren)>=1: 
                paren.pop()
        if len(paren) == 0:
            print("YES")
        else :
            print("NO") # 괄호 순서가 잘못된 경우 예: )))(((
    else:
        print('NO') # 괄호가 쌍으로 존재하지 않는 경우 예: (()))
        
        
        
# TODO: 5.25일 스터디 문제를 복습해보자 

'''
제로: https://www.acmicpc.net/problem/10773

도키도키 간식드리미: https://www.acmicpc.net/problem/12789

최소직사각형: https://school.programmers.co.kr/learn/courses/30/lessons/86491

막대기: https://www.acmicpc.net/problem/17608

프린터 큐: https://www.acmicpc.net/problem/1966

더 맵게: https://school.programmers.co.kr/learn/courses/30/lessons/42626

달팽이: https://www.acmicpc.net/problem/1913
'''


# [1] 

# [2] 

# [3] 

# [4]

# [5]

# [6]

# [7]
