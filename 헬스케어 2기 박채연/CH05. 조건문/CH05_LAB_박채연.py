#0404 조건문_LAB
#----------------------------------------

# 1. 직각삼각형 판별
side_a = int(input("변 a의 길이 : "))
side_b = int(input("변 b의 길이 : "))
side_c = int(input("변 c의 길이 : "))

if side_c**2 == side_a**2 + side_b**2 :
	print("직각삼각형 입니다.")
else :
	print("직각삼각형이 아닙니다.")

# 2. 정수의 종류 판별
from turtle import *
t = turtle.Turtle()
screen = Screen()
t.shape("turtle")
user_int = int(screen.textinput("정수", "숫자를 입력하세요."))

if user_int == 0:
	t.goto(100,0)
	t.write("입력된 정수는 0입니다.")
elif user_int > 0:
	t.goto(100,100)
	t.write("입력된 정수는 양의 정수입니다.")
else :
	t.goto(100,-100)
	t.write("입력된 정수는 음의 정수입니다.")

# 3. 주민등록번호 뒷자리 의미 확인
print("주민등록번호의 성별 정보 번호를 생성합니다.")
number = int(input("생성번호 : "))
if number == 1 or 3:
	print("남성입니다.")
elif number == 2 or 4:
	print("여성입니다.")
else:
	print("형식이 올바르지 않습니다.")

# 4. 동전 던지기 게임
from turtle import *
import random
t = Turtle()
screen = Screen()

coin_thorw = random.choice([0,1])
if coin_thorw == 0:
    coin_front = screen.bgpic("D:/헬스케어 2기 박채연/CH05. 조건문/front.gif")
elif coin_thorw == 1:
    coin_back = screen.bgpic("D:/헬스케어 2기 박채연/CH05. 조건문/back.gif")

screen.mainloop()

# 5. 전기회로
battery_1 = input("1번 전지가 있습니까? (Y/N)")
battery_2 = input("2번 전지가 있습니까? (Y/N)")

if (battery_1 == "Y" and battery_2== "Y"):
	print("직렬연결 : 전구에 불이 켜집니다.")
	print("병렬연결 : 전구에 불이 켜집니다.")
elif (battery_1 == "Y" or battery_2== "Y"):
	print("직렬연결 : 전구에 불이 꺼집니다.")
	print("병렬연결 : 전구에 불이 켜집니다.")
elif (battery_1 == "N" and battery_2== "N"):
	print("직렬연결 : 전구에 불이 꺼집니다.")
	print("병렬연결 : 전구에 불이 꺼집니다.")
else : 
	print("답변이 Y/N 형식이 아닙니다.")

# 6. 윤년 판단
user_year = int(input("연도를 입력하세요. : "))

	# 윤년은 4년주기이면서 100년주기 제외(단, 400년 주기는 윤년)
if ((user_year % 4 == 0) and (user_year%100 != 0)) or (user_year%400 == 0) :
	print(f"{user_year}년은 윤년입니다.")
else:
	print(f"{user_year}년은 윤년이 아닙니다.")
 
# 7. 이차방정식 판별식
print("이차방정식 y= ax^2 + bx +c 의 판별식 계산")
a = float(input("a값 입력 : "))
b = float(input("b값 입력 : "))
c = float(input("c값 입력 : "))
logic = b**2 - 4*a*c

if logic > 0:
	print("방정식은 서로 다른 두 실근 입니다.")
elif logic == 0:
	print("방정식은 서로 같은 두 실근 입니다.")
else:
	print("방정식은 서로 다른 두 허근 입니다.")

# 8. 사용자가 원하는 도형 그리기
from turtle import *
t = turtle.Turtle()
screen = Screen()
t.shape("turtle")

diagram = screen.textinput("도형 그리기", 
                           "도형을 입력하세요.\n(직사각형, 정삼각형, 원 중 선택 입력)")
if diagram == "직사각형":
    width = int(screen.textinput("사각형", "가로 길이를 입력하세요."))
    length = int(screen.textinput("사각형", "세로 길이를 입력하세요."))
    t.forward(width)
    t.setheading(90)
    t.forward(length)
    t.setheading(180)
    t.forward(width)
    t.setheading(270)
    t.forward(length)
elif diagram == "정삼각형":
    side = int(screen.textinput("정삼각형", "한 변의 길이를 입력하세요."))
    t.forward(side)
    t.setheading(120)
    t.forward(side)
    t.setheading(240)
    t.forward(side)
elif diagram == "원":
    radius = int(screen.textinput("원", "반지름의 길이를 입력하세요."))
    t.circle(radius)
else:
    print("도형을 정확히 입력해주세요.")

# 9. 두 원의 위치 관계 시뮬레이션
big_x = int(input("큰 원의 중심좌표 x : "))
big_y = int(input("큰 원의 중심좌표 y : "))
big_radius = int(input("큰 원의 반지름 : "))
small_x = int(input("작은 원의 중심좌표 x : "))
small_y = int(input("작은 원의 중심좌표 y : "))
small_radius = int(input("작은 원의 반지름 : "))

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()	
t.goto(big_x, big_y)
t.down()
t.circle(big_radius)
t.up()
t.goto(small_x, small_y)
t.down()
t.circle(small_radius)
t.home()

dist = ((big_x-small_x)**2 + (big_y-small_y)**2)**0.5

if dist == 0 :
    t.write("원의 중심이 같은 중심원", align= "center")
elif dist == big_radius - small_radius :
    t.write("내접", align= "center")
elif (big_radius - small_radius) < dist < (big_radius + small_radius) :
    t.write("두 점에서 만납니다.", align= "center")
elif dist > (big_radius + small_radius) :
    t.write("만나지 않고 외부에 있습니다.", align= "center")
elif dist == (big_radius + small_radius) :
    t.write("외접", align= "center")
elif dist < (big_radius - small_radius) :
    t.write("만나지 않고 내부에 있습니다.", align= "center")    
   