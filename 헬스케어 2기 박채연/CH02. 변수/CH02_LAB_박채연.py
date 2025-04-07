#CH02 변수 LAB
#---------------------

#1. 반지름이 r인 원 넓이 구하기
r= 10
print("반지름이 ", r, "인 원의 넓이 : ", r, "*", r, "*", 3.14)

#2. 내가 원하는 원 그리기
import turtle
t= turtle.Turtle()
t.shape("turtle")

radius = int(input("원의 반지름을 입력하시오. : "))
color =  input("원의 색깔을 입력하시오. : ")

t.color(color)
t.fillcolor(color)
t.begin_fill()
t.circle(radius)
t.end_fill()

#3. 천둥번개
time= int(input("측정 시간(초) 입력 : "))
c = 300000000   #30만km/s
sound = 340     # 340m/s
distance = time * sound
print("자신의 위치에서 번개가 친 장소까지의 거리 = ", distance, "m")


