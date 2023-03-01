# case_num = input()
# sum_score = 0
# for i in range(int(case_num)):
#     score_list = input().split()
#     sum_score = 0
#     count = 0
#     for j in range(int(score_list[0])):
#         sum_score += int(score_list[j+1])
#     Avg_score = sum_score // int(score_list[0])
#     for j in range(int(score_list[0])):
#         if int(score_list[j+1]) >  Avg_score :
#             count +=1
#     print("{:.3f}%".format((count/int(score_list[0]))*100))

# word = input()
# word = word[:]
# result = 1
# for i in range(len(word)//2):
#     if word[i] != word[-(i+1)]:
#         result = 0
# print(result)