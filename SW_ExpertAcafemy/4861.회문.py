# TODO: 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

# T = int(input())


# for i in range(1,T+1):
#     N,M = list(map(int, input().split(' ')))
#     Area = [[0]*M for _ in range(N)]
#     result = ""
#     found = False

#     # 문자열 입력 받기 
#     for j in range(N):
#         Area[j][:] = list(input())
    
#     # 가로 먼저 검사 
#     if N %2 == 0:
#         for r in range(N):
#             mid = M//2 
#             count = 0
#             for m in range(mid):
#                 if Area[r][mid-1-i] != Area[r][mid+i]:
#                     break
#                 else : 
#                     count += 1
#             if mid == count : 
#                 result = Area[r][:]
#                 found = True

#     # 세로 먼저 검사 
#     if  not found:
#         for r in range(M):
#             mid = N//2 
#             count = 0
#             for m in range(mid):
#                 if Area[mid-1-i][r] != Area[mid+i][r]:
#                     break
#                 else : 
#                     count += 1
#             if mid == count : 
#                 result = Area[:][r]
#                 found = True
                
#     print(f"#{i} {''.join(result)}")

print(not False)