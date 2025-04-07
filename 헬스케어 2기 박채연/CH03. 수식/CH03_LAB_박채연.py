#0403 수식_LAB
#----------------------------------------
#1 다항식 계산
x , y = -1, 3
print("다항식의 계산 결과 : ", (-y)**3 + 2*(x**2)*y)


#2 화씨온도를 섭씨온도로 변환
F = int(input("화씨온도 : "))

C = (F-32) * (5/9)

print("섭씨온도 :", C)

#3 두점 사이의 거리 구하기
x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
distance = x1**2 

print("두 점 사이의 거리 = ", (((x2-x1)**2)+((y2-y1)**2))**0.5)


#4 그리니치 표준시 - 세계 시간의 기준점
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


#5 계산대 프로그램
money = int(input("투입한 돈 : "))
price = int(input("물건가격 : "))
change = money - price
print("거스름돈 :" , change, "원")
print("500원 동전의 개수 :" , change//500, "개")
print("100원 동전의 개수 :" , change%500//100, "개")
