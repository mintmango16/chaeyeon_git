#0402 프로그래밍 기초
#------------------------------
print("내가 제일 좋아하는 음식은 피자!")
print("피자"*10)

#------------------------------
import turtle
t= turtle.Turtle()
t.shape("turtle")

 #도형그리기
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100) # 정사각형 만들기

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.circle(100) # 반지름 100인 원

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

##-------------------------------

t.clear()  #모두 지우기

t.width(10) #선의 두께
t.color("blue")
t.forward(100)
t.left(90)
t.forward(100)

t.shape("square")

t.shape("turtle")
t.down()      #펜을 내림
t.goto(100,0) #x, y 좌표값으로 이동
t.up()        #펜을 올림
t.goto(0,200)
t.down()
t.goto(100,200)












