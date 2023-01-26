
# Q.6007 "C:\Download\'hello'.py" 출력하기
print("\"C:\\Download\\\'hello\'.py\"")
# -> 문자열에 특수 기호가 들어갈 때는 맨 끝이 아니라 중간에도 특수기호 앞에 \를 붙여준다.


# Q.6008 print("Hello\nWorld") 출력하기
print("print(\"Hello\\nWorld\")")

# Q.6009 변수에 문자 1개를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
what = input()
print(what)

# Q.6010 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.
int_var = input()
print(int(int_var))

# Q.6011 변수에 실수 값을 저장한 후 실수로 변환하여 출력해보자.
int_var = input()
print(float(int_var))

# Q.6012 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
one = input()
two = input()
print(int(one))
print(int(two))

# Q.6013 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.
one = input()
two = input()
print(two)
print(one)

# Q.6014 실수 1개 입력받아 3번 출력하기
one = input()
print(float(one))
print(float(one))
print(float(one))

# Q.6015 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
one,two = input().split()
print(one)
print(two)

# Q.6016 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.
one,two = input().split()
print(two,one)

# Q.6017 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.
one = input()
print(one,one,one)

# Q.6018 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
hour,min = input().split(':')
print(hour,min,sep= ":")

# Q.6019 "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y,m,d = input().split('.')
print(d,m,y,sep='-')

# Q.6020 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.
num_front,num_back = input().split('-')
print(num_front+num_back)

# Q.6021 알파벳과 숫자로 이루어진 단어 1개가 입력된다. 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.
voca = input()
for i in range(5):
    print(voca[i])

# Q.6022 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
yymmdd = input()
print(yymmdd[0:2],yymmdd[2:4],yymmdd[4:6])

# Q.6023 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자. 어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.
h,m,s = input().split(':')
print(m)
