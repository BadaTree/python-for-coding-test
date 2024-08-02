# [ ] 비트 연산에 대해 공부하고 문제를 풀어보자

# [1] 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
# https://www.youtube.com/watch?v=4BSrpZlGW4A

'''
비트 연산을 사용한 코드의 동작 방식을 좀 더 자세히 설명해드리겠습니다. 비트 연산을 이해하기 위해서는 먼저 2진수 표기법과 기본적인 비트 연산에 대해 알아야 합니다.

2진수와 비트 연산
2진수: 컴퓨터는 2진수(0과 1)로 데이터를 표현합니다. 예를 들어, 십진수 5는 2진수로 101입니다.
비트 연산: 비트 단위로 이루어지는 연산입니다. 여기에는 AND(&), OR(|), NOT(~), XOR(^), 왼쪽 시프트(<<), 오른쪽 시프트(>>) 등이 있습니다.
기본 비트 연산
AND 연산(&): 두 비트가 모두 1일 때만 1이 됩니다.
예: 1010 & 0110 = 0010
왼쪽 시프트(<<): 모든 비트를 왼쪽으로 이동시키고, 오른쪽에 0을 추가합니다.
예: 0001 << 1 = 0010 (십진수로 1을 2로 만듦)
예: 0010 << 1 = 0100 (십진수로 2를 4로 만듦)
코드의 동작 원리
이제 주어진 숫자 
𝑛
n 보다 크거나 같은 가장 가까운 2의 거듭제곱을 찾는 과정을 설명하겠습니다.

1. 입력 값 검증 및 초기 설정
python
코드 복사
def next_power_of_two(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # 이미 2의 거듭제곱인지 확인
    if (n & (n - 1)) == 0:
        return n
입력 값 
𝑛
n 이 양의 정수인지 확인합니다.
𝑛
n 이 2의 거듭제곱인지 확인합니다. 
𝑛
n 이 2의 거듭제곱이면, 
𝑛
n 은 하나의 1 비트만 가지고 있습니다. 예를 들어, 8은 1000(2)이고, 16은 10000(2)입니다.
𝑛
&
(
𝑛
−
1
)
n&(n−1) 연산은 
𝑛
n 의 가장 낮은 1 비트를 제거합니다. 예를 들어, 8 (1000) & 7 (0111) = 0입니다. 이 결과가 0이면 
𝑛
n 은 2의 거듭제곱입니다.
2. 가장 가까운 2의 거듭제곱 찾기
python
코드 복사
    power = 1
    while power < n:
        power <<= 1
power 변수를 1로 초기화합니다. 이는 2의 0제곱(1)입니다.
while 루프는 power 가 
𝑛
n 보다 작을 때까지 실행됩니다.
power <<= 1 은 power 의 비트를 왼쪽으로 한 칸 이동시킵니다. 이는 power 를 두 배로 만듭니다. 예를 들어, 1 (0001)을 왼쪽으로 한 번 이동시키면 2 (0010)가 되고, 또 한 번 이동시키면 4 (0100)가 됩니다.
3. 결과 반환
python
코드 복사
    return power
루프가 끝나면 power 는 
𝑛
n 보다 크거나 같은 가장 작은 2의 거듭제곱이 됩니다.
이 값을 반환합니다.
예시
주어진 숫자 30에 대해 이 과정이 어떻게 작동하는지 보겠습니다.

power = 1 초기화 (0001)
power < 30 조건 만족, power <<= 1 실행 (0010, 2)
power < 30 조건 만족, power <<= 1 실행 (0100, 4)
power < 30 조건 만족, power <<= 1 실행 (1000, 8)
power < 30 조건 만족, power <<= 1 실행 (10000, 16)
power < 30 조건 만족, power <<= 1 실행 (100000, 32)
power >= 30 조건 불만족, 루프 종료
power = 32 반환
결과적으로 30보다 크거나 같은 가장 가까운 2의 거듭제곱은 32입니다.

이 설명을 통해 비트 연산이 어떻게 동작하는지, 그리고 코드가 어떤 원리로 작동하는지 이해하는 데 도움이 되셨기를 바랍니다.

'''