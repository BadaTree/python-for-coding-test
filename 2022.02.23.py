# score = input()
# if 90<= int(score)<= 100:
#     print("A")
# elif 80<= int(score)<= 89:
#     print("B")
# elif 70<= int(score)<= 79:
#     print("C")
# elif 60<= int(score)<= 69:
#     print("D")
# else :
#     print("F")

start_h, start_m = input().split()
start_h =int(start_h)
start_m = int(start_m)
time = int(input())

end_time = (start_h*60) + start_m + time
print()

# end_h = (time/60) + int(start_h)
# end_m = time % 60 + int(start_m)
#
# if end_m >= 60 :
#     end_h = end_h + (end_m/60)
#     if int(end_h) >= 24:
#         end_h = end_h - 24
#     end_m = end_m% 60
#
# print(int(end_h),end_m)

