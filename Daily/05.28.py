# TODO : 파이썬 알고리즘 문제풀이 입문

test= "Hi my name is Bada66"

print(test.upper())
print(test.lower())
print(chr(65))
print(ord("A"))
for i in test:
    # if i.isalpha() :
    #     print(i,end="")
    #     # print(i, end=" ")
    if i.isupper():
        print(i, end=" ")