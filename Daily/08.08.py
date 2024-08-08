# [ ] 코테 문제 

from collections import deque


def split_stepwise(message):
    result = []
    next_msg = []
    
    split_msg = deque(message)

    while split_msg:
        # 각 문자를 분리하여 다음 레벨 메시지를 생성
        msg = split_msg.popleft()
        # 다음 레벨 msg 생성
        next_msg.extend([m for m in msg.split(msg[0]) if m != ''])
     
        if not split_msg:
            break
        
    # 현재 단계에서 완전히 사라진 alpha 찾기
    result = set(''.join(message)) - set(''.join(next_msg))
    print(''.join(message),''.join(next_msg))
    print(next_msg,result)   
    return next_msg,sorted(result)


def solution(message):
    result = [ ] # 분해해서 사라진 알파벳 리스트
    next_msg = [message]
 
    while next_msg:
        next_msg, removed_aplpha = split_stepwise(next_msg)
        result.extend(removed_aplpha)
        if not next_msg:  # msg가 비어 있으면 반복 종료
            break
        
    return ''.join(result)
        
print(solution('banbanbact'))