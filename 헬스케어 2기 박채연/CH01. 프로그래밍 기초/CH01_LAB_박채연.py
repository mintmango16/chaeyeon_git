#CH01. 프로그래밍 기초 LAB
#---------------------------------

#1
print("시간순삭 파이썬")

#2
print("9*8은 72입니다.")

#3
print("너무 ", "반짝"*2, " 눈이 부셔", " No"*5)
print("너무 ", "깜짝"*2, " 놀란 나는", " Oh"*5)
print("너무 ", "짜릿"*2, " 몸이 떨려", " Gee"*5)


#--------------------------

import turtle
t= turtle.Turtle()
t.shape("turtle")

#1
t.circle(100) # 반지름 100인 원

#2
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100) # 정육각형

#--------------------------
#1
import turtle
t= turtle.Turtle()
t.shape("turtle")
t.width(10)
t.forward(100)
t.left(90)
t.forward(100)

#2
t.color("blue")
t.forward(100)
t.left(90)
t.forward(100)

#3
t.shape("square")
t.forward(100)
t.left(90)
t.forward(100)

#4
t.shape("turtle")
t.down()      #펜을 내림
t.goto(100,0) #x, y 좌표값으로 이동
t.up()        #펜을 올림
t.goto(0,200)
t.down()
t.goto(100,200)






