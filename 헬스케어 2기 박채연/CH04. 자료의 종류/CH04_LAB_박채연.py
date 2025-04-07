#0403 자료의 종류_LAB
#----------------------------------------
#type() # 자료형 확인 함수

#1 소금물의 농도
print("소금물의 농도를 구하는 프로그램입니다.")
salt = int(input("소금의 양은 몇 g입니까?"))
water = int(input("물의 양은 몇 g입니까?"))
density = (salt/(salt+water))*100
print("소금물의 농도 : ", density, "%")


#2 간단한 챗봇 프로그램
print("안녕하세요.")
name = input("이름이 무엇인가요? ")
print("만나서 반갑습니다.", name," 님\n"
    , name, "님, 이름의 길이는 다음과 같습니다. :" , len(name))
age = int(input("나이가 어떻게 돼요? "))
print("내년이면 ", age + 1, "세가 되시는군요!")

#3 거북이와 인사
from turtle import *
t=Turtle()
screen = Screen()
t.shape("turtle")
user_name = screen.textinput("거북이와 인사하기!", "이름을 입력하세요.")
t.write("안녕하세요! "+ user_name + "님, 저는 거북이랍니다.")

t.color("pink", "pink")
t.begin_fill()
t.circle(20)
t.left(60)
t.circle(20)
t.left(60)
t.circle(20)
t.left(60)
t.circle(20)
t.left(60)
t.circle(20)
t.left(60)
t.circle(20)
t.end_fill()    # 핑크색 꽃 그리기
t.color("green")

t.up()
t.goto(70,70)
t.write(user_name + "님, 만난 기념으로 꽃을 그려드렸는데 어떠신가요?")

#4 암호프로그램 만들기
normal = input("평문 : ")
password = normal[-1::-1]
print("암호문 : %s" % password)

#5 2050년 나이 계산
import time
now = time.time()
thisYear = int(1970 + now //(365*24*3600))
print("올해는 " + str(thisYear) + "년입니다.")
user_age = int(input("당신의 나이를 입력하세요 : "))
print("2050년에는 "+ str(2050-thisYear+user_age)+"세이시군요.")
