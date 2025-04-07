###0403 수식_추가연습문제
###----------------------------

#1
chicken = int(input("닭의 수 : "))
pig = int(input("돼지의 수 : "))
cow = int(input("소의 수 : "))
total_lag = chicken*2 + pig*4 + cow*4
print("전체 다리의 수 : " + str(total_lag))

#2
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print("두점 사이의 거리 = ", distance)

#3
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.setheading(45)
t.forward(141)
t.home()
t.setheading(0)
t.forward(100)
t.left(90)
t.forward(100)
turtle.bye()

#4
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

t.up()
t.goto(x1, y1)
t.down()
t.goto(x2,y2)
t.write("직선의 길이 : "+ str(((x1-x2)**2+(y1-y2)**2)**0.5))

#5
import time
fsecond = int(time.time())
    # 1970/01/01 이후 현재까지의 시간을 초단위의 실수값으로 반환
    
total_min = fsecond // 60       # 전체 시간 분단위
minute = total_min % 60         # 현재 시간 분단위
total_hour = total_min // 60    # 전체 시간 시단위
korea_time_hour = (total_hour + 9) % 24         # 한국 현재시간 시단위
        # 한국은 그리니치 표준시보다 +9시간이므로
        # 전체시간에 9시간을 더한후 24시간을 나눈 나머지가 한국 현재시간 시단위

print("현재 한국 시간 : ", korea_time_hour, "시", minute, "분")






