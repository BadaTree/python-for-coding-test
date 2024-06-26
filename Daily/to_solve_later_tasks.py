# TODO : 나중에 풀어야하는 문제 리스트

'''
[ 5. 18 (토) 스터디 문제 공유 ]

 
회전하는 큐: https://st-lab.tistory.com/216

 
요세푸스: https://www.acmicpc.net/problem/1158

 
암기왕: https://www.acmicpc.net/problem/2776

 
좋은단어: https://www.acmicpc.net/problem/3986

 
뒤집기: https://www.acmicpc.net/problem/1439

 
단어뒤집기2: https://www.acmicpc.net/problem/17413

기능 개발 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

[ 5. 25 (토) 스터디 문제 공유 ]

제로: https://www.acmicpc.net/problem/10773

도키도키 간식드리미: https://www.acmicpc.net/problem/12789

최소직사각형: https://school.programmers.co.kr/learn/courses/30/lessons/86491

막대기: https://www.acmicpc.net/problem/17608

프린터 큐: https://www.acmicpc.net/problem/1966

더 맵게: https://school.programmers.co.kr/learn/courses/30/lessons/42626

달팽이: https://www.acmicpc.net/problem/1913

level2문제: https://school.programmers.co.kr/learn/courses/30/lessons/147354
level3문제: https://school.programmers.co.kr/learn/courses/30/lessons/42579

폰켓몬(level1): https://school.programmers.co.kr/learn/courses/30/lessons/1845
전화번호 목록(level2): https://school.programmers.co.kr/learn/courses/30/lessons/42577


# [ ] 메뉴 리뉴얼 (level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72411


# [ ] 패션왕 신해빈 (실버 3, 백준)
# https://www.acmicpc.net/problem/9375

# [ ] 미로 탈출 명령어 
# https://school.programmers.co.kr/learn/courses/30/lessons/150365


# [ ] 순위 검색 (Level2, 프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/72412


상근이의 여행: https://www.acmicpc.net/problem/9372 

무한이진트리: https://www.acmicpc.net/problem/2078

Smallest Number in infinite Set: https://leetcode.com/problems/smallest-number-in-infinite-set/description

카펫: https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

# [ ] 백준 2231

def find_smallest_constructor(target):
    # 각 자리수의 합이 최대 9이므로 탐색 시작점을 target - 9 * len(str(target))로 설정
    start = max(1, target - 9 * len(str(target)))
    
    for candidate in range(start, target):
        sum_with_digits = candidate + sum(map(int, str(candidate)))
        if sum_with_digits == target:
            return candidate
    return 0

# 입력 처리
target = int(input())

# 결과 출력
print(find_smallest_constructor(target))