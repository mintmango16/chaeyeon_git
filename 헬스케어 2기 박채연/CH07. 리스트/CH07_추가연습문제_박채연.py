#0408 리스트_추가연습문제
#----------------------------
#1. 1부터 100 중 난수 10개를 생성해서 리스트 value 채우기
import random
list = []
for i in range(10):
    list.append(random.randint(0,100))
print(list)

#2. 리스트에 저장된 값만큼 별표 출력
list = [20, 1, 12, 9, 18]
for n in range(0,5) :
    print(f"{list[n]}       {"*"*list[n]}")

#3. 색상 꺼내서 사각형 그리기
from turtle import *
import random
t=Turtle()
t.shape("turtle")

t.up()
def draw_square(x,y,c):
    t.color(c)
    t.begin_fill()
    t.goto(x, y)
    t.down()
    for i in range(4):
        t.forward(100)    
        t.right(90)
    t.up()
    t.end_fill()

for c in ["yellow", "red", "purple", "blue"] :
    x = random.randrange(-100,100)
    y = random.randrange(-100,100)
    draw_square(x,y,c)

     
#4. 랜덤 색상으로 별 그리기
from turtle import *
import random
t=Turtle()
s=Screen()

t.shape("turtle")
s.bgcolor("black")
t.up()

def draw_star(x,y,c,length):
    t.color(c)
    t.begin_fill()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.forward(100)
        t.left(144)
    t.up()
    t.end_fill()

for i in range(10):
    c = random.choice(["yellow", "red", "purple", "blue", "green", "skyblue", "white"])
    x = random.randrange(-300,300)
    y = random.randrange(-300,300)
    length = random.randrange(-100,100)    
    draw_star(x,y,c,length)

