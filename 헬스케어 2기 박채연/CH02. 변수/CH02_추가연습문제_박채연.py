#0402 변수_추가연습문제
#----------------------------

#1
name = input("이름을 입력하세요.")
age = int(input("나이를 입력하세요."))
print(name, "씨는 ", 2120 - age,"년에 100살이시네요!")

#2
r = int(input("반지름을 입력하세요:"))
print("반지름이 ", r, "인 원의 넓이 =", r*r*3.14)

#3
import turtle
t= turtle.Turtle()
t.shape("turtle")

side = 100

t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)

#4
side = 200
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)

#5
import turtle
t= turtle.Turtle()
t.shape("turtle")

side = 100
angle = 90

t.forward(side*2)
t.left(angle)
t.forward(side*2)
t.left(angle)
t.forward(side*2)
t.left(angle)
t.forward(side*2)

t.up()
t.goto(0, side)
t.left(angle)
t.down()
t.forward(side*2)

t.up()
t.goto(side, 0)
t.left(angle)
t.down()
t.forward(side*2)




