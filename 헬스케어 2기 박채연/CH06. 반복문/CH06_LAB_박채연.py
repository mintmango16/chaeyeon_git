#0404 반복문_LAB
#----------------------------------------
# 1. n각형 그리기
from turtle import *
t = Turtle()
screen = Screen()
t.shape("turtle")

n = int(screen.textinput("n각형 그리기", 
                         "몇각형을 원하시나요? \n 숫자를 입력하세요."))
side = 100
angle = 180*(n-2)/n # 다각형 내각 크기 공식

for i in range(n) :
    t.forward(side)
    t.left(180-angle)

screen.mainloop()

# 2. 랜덤 워크 시뮬레이션
from turtle import *
import random
t = Turtle()
screen = Screen()
t.shape("turtle")
color = ["red", "yellow", "green", "blue","pink"]

i = 1
while i <= 100:
    x = random.randrange(-500, 501 ,10)
    y = random.randrange(-500, 501 ,10)
    pen_color = random.choice(color)
    t.color(pen_color)
    t.goto(x,y)
    i += 1

screen.mainloop()
 

# 3. 범인 찾기 게임
import random

score = 100
thief = random.choice(["1번","2번","3번"])
answer = input("범인이 어떤 방에 숨었는지 맞춰보세요! \n (1번, 2번, 3번 중 선택 입력) : ")
while answer != thief:
    score -= 10
    print(f"틀렸습니다. 점수 :{score}점")
    thief = random.choice(["1번","2번","3번"])
    answer = input("범인이 다시 숨었습니다. 다시 맞춰보세요!")
    if score == 10 :
        print(f"게임 오버. 점수는 {score}점 입니다.")
        break
        
print(f"축하합니다! {thief}방에 숨어있던 범인을 찾았습니다. 점수는 {score}점 입니다.")

# 4. 몬드리안 터틀
import turtle, random
t = turtle.Turtle()

for i in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(10,300)

    r = random.random()
    g = random.random()
    b = random.random()

    t.up()
    t.goto(x,y)
    t.color(r,g,b)
    t.down()
    t.begin_fill()
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.end_fill()
    t.up()


# 5. 모든 약수 구하기
import math
user_str = int(input("자연수 입력 : "))
n=1

divisor= "1"
while n <= user_str:
    number = user_str % n
    if (number == 0) and (n!=1) :
        divisor += str(n) 
    n = int(n)
    n += 1
        
print(f"약수 : {divisor}")
 
# 6. 최대공약수 구하기
    # a, b의 최대공약수는 (a를 b로 나눈 나머지),b의 최대공약수와 같다.
    # 큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체, 이를 반복
    # 나머지가 0이 되면 작은 수(=나누는 수)가 최대공약수
import math
n1 = int(input("정수 1 입력 : "))
n2 = int(input("정수 2 입력 : "))

if n2 > n1 : 
    n1 , n2 = n2, n1
while n2 != 0:
    n1 = n1 % n2
    n1 , n2 = n2, n1

if n1 != 1:
    print(f"최대공약수 : {n1}") 
else :
    print("두 수는 서로소이다.")
    

# 7. 별 그리는 터틀
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.forward(100)
    t.left(144)

# 8. 숫자 맞추기 게임
import random
n = 0
number = random.randint(1, 100)

while True :
    answer = int(input("숫자를 입력하세요 : "))
    n += 1
    if answer == number:
        break
    elif answer > number: 
        print("다운")    
    elif answer < number: 
        print("업")


print(f"축하합니다! 시도횟수 :{n}번")

