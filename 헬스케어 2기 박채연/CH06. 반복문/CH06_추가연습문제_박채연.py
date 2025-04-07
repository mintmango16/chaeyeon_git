#0404 반복문_추가연습문제
#----------------------------

# 1. 사용자에게 곱셈 퀴즈 내고 사용자가 답 맞추기
n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))  
answer = 0

while answer != n1 * n2 :
    answer = int(input(f"{n1}*{n2}는 ? :"))
print("정답입니다!")

# 2. 난수 생성 -> 2개의 주사위 던지기
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print(f"첫번째 주사위 : {dice1}, 두번째 주사위 : {dice2}")

# 3. 터틀 모듈로 눈 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
for i in range(6):
    t.forward(100)
    t.forward(-30); t.left(60); t.forward(30)
    t.forward(-30); t.right(120); t.forward(30)
    t.up()
    t.goto(0,0)
    t.down()
    t.setheading(60 + i * 60)

# 4. 터틀 모듈로 sin 함수 그래프 그리기
import turtle
import math
t = turtle.Turtle()
t.shape("turtle")

for degree in range(360):
    radian = 3.14 * degree / 180.0 # 각도->라디안으로 변환
    s = math.sin(radian) # parameter=라디안 
    t.goto(degree, s*100)
    
