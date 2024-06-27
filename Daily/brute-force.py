# TODO: 부루트 포스, 완전 탐색을 공부해보자

# [ ] 프로그래머스 소수 찾기 
# https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 1차 시도 10,11,12에서 시간 초과가 뜨고, 효율성도 시간초과... ㅋㅋ
# 

# 1,자기 자신을 제외한 약수가 발견되면 answer +1 , break 
def is_prime(i):
    result = 1
    for j in range(2,i):
            if i % j == 0 :
                result = 0
                break
    return result


def solution(n):
    result = 0
    # 2 부터 n까지 소수인지 체크 %1은 소수가 아님
    for i in range(2,n+1):
        result += is_prime(i)
    return result