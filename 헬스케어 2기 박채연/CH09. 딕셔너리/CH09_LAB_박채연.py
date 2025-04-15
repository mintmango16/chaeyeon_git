#0408 딕셔너리_LAB
#----------------------------

# 1. 가위바위보 게임
import random
game = {"가위":"바위", "바위":"보", "보":"가위"}
com = random.choice(["가위", "바위","보"])
user = input("가위바위보 ! ")

if user in game.keys() :
    if user != com :
        if game[com] == user :
            print(f"com : {com} , 당신이 이겼습니다.")
        elif game[com] != user : 
            print(f"com : {com} , 당신이 졌습니다.")
    else : 
        print(f"com : {com} , 당신이 비겼습니다.")
else : 
    print("가위, 바위, 보 중 하나를 입력하세요.")



# 2. 행성까지의 여행시간
distance_by_planet = {"수성":91.7, "금성" : 41.4, "화성" : 78.4,
                      "목성": 628.7, "토성": 1277.4, "천왕성": 2750.4, 
                      "해왕성":4347.4} # 10^6 km 단위
name = input("행성 이름 : ")
v = int(input("이동 속도(km/h) : "))


if name in distance_by_planet :
    total_hour = int((distance_by_planet[name]*1000000) / v) # 시간 = 거리*속도
    hour = total_hour % 24
    year = total_hour // (31*24*12)
    month = (total_hour - year*365*24) // (31*24)
    day = (total_hour-(year*365*24) - (month*31*24)) // 24
    print(f"이동시간 : {int(total_hour)}시간")
    print(f"이동시간 : 약 {int(year)}년 {int(month)}개월 {int(day)}일 {int(hour)}시간")



# 3. 멘델의 유전법칙



# 4. 튜링상 수상자 데이터분석
awards = {"이름":["팀 버너스리", "리처드 해밍", "에프허르 데이크스트라", "더글러스 엥겔바트", "데니스 리치"],
          "수상년도":[2016, 1968, 1972, 1997, 1983],
          "국적" : ["영국", "미국", "네덜란드", "미국", "미국"],
          "대표업적":["월드 와이드 웹의 하이퍼텍스트 시스템 고안 개발",
                  "오류 검출 부호 및 오류 정정 부호",
                  "프로그래밍 언어 연구, 데이크스트라 알고리즘",
                  "마우스의 발명, 대화형 컴퓨팅","유닉스 운영체제 개발, C언어 개발"]}
for award in awards :
    print(awards["이름"]) #수상자 명단
for award in awards : 
    if awards["수상년도"]<=1990:
        print(award["이름"], award["수상년도"])

# 5. 파이썬으로 이메일 발송
import smtplib

my_email = "cypak0657@gmail.com"
password = "wnze lznz stqo bdbm" #구글 설정-앱 비밀번호

connection = smtplib.SMTP("smtp.gmail.com") #보내는 메일의 SMTP 주소 입력
connection.starttls() #transport layer security : 메세지 암호화
connection.login(user = my_email, password = password)
connection.sendmail(from_addr = my_email, to_addrs = "bluesea0228@hanmail.net", #받는 메일
    msg="Subject:Hello\n\nThis is the body of my email.")
        #Subject:제목\n\n내용 구조로 메시지 입력.
connection.close()
