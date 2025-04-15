#0408 함수_추가연습문제
#----------------------------


# 이차함수 그리기
from turtle import *
import random
t = Turtle()
s = Screen()

def f(x):
    y = x**2 + 1
    return y

t.forward(300)
t.home()
t.left(90)
t.forward(300)
t.right(90)

for i in range(0,150):
    t.goto(i, f(i)*0.01)

s.mainloop()

#계산기 함수 정의 

def plus(x,y):
    result = x+y
    return result
def minus(x,y):
    result = x-y
    return result
def multi(x,y):
    result = x*y
    return result
def division(x,y):
    result = x/y
    return result

    
user_x = int(input("x:"))
user_y = int(input("y:"))
print(f"{user_x} + {user_y} = {plus(user_x, user_y)}")
print(f"{user_x} - {user_y} = {minus(user_x, user_y)}")
print(f"{user_x} * {user_y} = {multi(user_x, user_y)}")
print(f"{user_x} / {user_y} = {division(user_x, user_y)}")


#주어진 정수가 소수인지 검사
import math

def testPrime(n):
    for i in range(2, n):
        if (n % i)== 0:
            return False
    return True

for n in range(2, 101):
    if testPrime(n):
        print(n, end = " ")

