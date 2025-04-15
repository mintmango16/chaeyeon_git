#0408 함수_LAB
#----------------------------

#BMI  계산기
x = float(input("키를 m단위로 입력하세요 : "))
y = float(input("몸무게를 kg단위로 입력하세요 : "))

def bmi(height, weight):
    result = weight/((height)**2)
    return result

print(bmi(x, y))

#환전 계산기
x = float(input("환전 금액(원)을 입력하세요요 : "))
y = input("국가를 입력하세요 : ")

def coin(money, country):
    exchange_rate = {"미국":1472.8, "중국" : 200.58, "영국" : 1883.25 , "일본": 10}
    if country in exchange_rate.keys() :
        exchange = money/exchange_rate[country]
    return exchange

print(f"{x}원은은 {coin(x,y)} 단위입니다.")


#N각형 그리는 함수 작성
from turtle import *
t = Turtle()
screen = Screen()
t.shape("turtle")


user_n = int(input("몇각형을 원하시나요? \n 숫자를 입력하세요."))
def n_polygon(n):
    side = 100
    angle = 180*(n-2)/n # 다각형 내각 크기 공식

    for i in range(n) :
        t.forward(side)
        t.left(180-angle)

for i in range(10):
    n_polygon(user_n)
    t.left(20)
screen.mainloop()


#클릭하는 곳에 사각형 그리기
from turtle import *
t = Turtle()
screen = Screen()
t.shape("turtle")

def square():
    t.color("blue")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill

if screen.onscreenclick(t.goto()) :
    square()

#한붓그리기

#이차함수 그래프 그리기

#터틀 미로 탈출 게임

#프랙탈 나무 그리기
