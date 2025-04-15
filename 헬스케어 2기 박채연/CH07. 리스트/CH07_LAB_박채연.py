""" #0408 리스트_LAB
#----------------------------
# .append  .insert  .remove   del  .pop():맨뒤 항목 삭제  .index

# heroes = ["아이언맨", "토르","헐크", "스칼렛 위치"]
# heroes.sort(reverse=True) # 내림차순 정렬
# new_heroes = sorted(heroes) # 새로운 리스트로 저장

#1. 주기율표
table = ["수헬리베붕", "탄질산플네나", "마알규", "인활염아칼칼"]
user_table = []

for i in [0,1,2,3] :
    user_answer = input("주기율표 구절을 입력하세요 :")
    user_table.append(user_answer)

print(user_table)

#1-1 다른 방법
user_table = [0, 0, 0, 0]

for i in [0,1,2,3] :
    user_answer = input("주기율표 구절을 입력하세요 :")
    user_table[i] = user_answer
print(user_table)



#2. 오늘의 명언
import random

text = ["고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.",
        "사람은 사랑할 때 누구나 시인이 된다.",
        "꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다."]
today_text = random.choice(text)
print("########오늘의 명언########")
print(today_text)

 
#3. 스파이럴 spial  그리기
import turtle 

color = ["red", "yellow", "green", "blue"]
 """

#4. 오륜기 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
r =50
colors = ["blue", "black","red", "yellow", "green"]
postions = [
    (-2*r, 0), (0,0), (2*r, 0),
    (-r, -r), (r, -r)]

for i in range(5):
    t.up()
    t.goto(postions[i])
    t.down()
    t.color(colors[i])
    t.circle(r)


""" 
#5. 습도 구하기
user_temp = int(input("현재 온도 : "))
user_water = float(input("현재 수증기량 : "))
temp_by_water = [
    [0, 10, 20, 30],            #온도 리스트
    [4.8, 9.4, 17.3, 30.4]]     #포화 수증기량 리스트

if user_temp in temp_by_water[0] : #입력받은 온도가 행렬에 있는지 확인
    index = temp_by_water[0].index(user_temp) #사용자 온도에 해당하는 인덱스 저장
    max_water = temp_by_water[1][index]       #사용자 온도에 해당하는 포화 수증기량 저장
    humidity = (user_water/max_water) * 100
    print(f"{user_temp}도의 현재 습도는 약 {humidity}% 입니다.")
else :
    print("입력한 온도가 10, 20, 30, 40도중 하나가 아닙니다.")
 """