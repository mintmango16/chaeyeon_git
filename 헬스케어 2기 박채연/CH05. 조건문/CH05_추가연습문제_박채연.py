#0404 조건문_추가연습문제
#----------------------------

# 1. 양수, 0, 음수 출력 프로그램
user_int = int(input("정수를 입력하세요. :"))
if user_int == 0 :
    print("0 입니다.")
elif user_int > 0 :
    print("양수 입니다.")
elif user_int < 0 :
    print("음수 입니다.")

# 2. 배송료 계산 
country = input("국가를 입력하세요. :")

if country == "한국" :
    do = input("도를 입력하세요. : ")
    if do == "제주도":
        delivery = 10000
    else :
        delivery = 5000
else : 
    delivery = 20000
    
print(f"배송료는 {delivery}원 입니다.")

# 3. 2차 방정식의 근 출력
print("이차방정식 ax^2 + bx + c의 근 계산")
a = float(input("a값 입력 : "))
b = float(input("b값 입력 : "))
c = float(input("c값 입력 : "))

root = b**2 - 4*a*c #근의 판별식
if root > 0:
    quadratic_formula1 = (-b + root**0.5)/(2*a)
    quadratic_formula2 = (-b - root**0.5)/(2*a)
    print("2개의 실근이 있습니다. : " + f"{quadratic_formula1}와 {quadratic_formula2}")
elif root == 0:
    quadratic_formula = (-b + root**0.5)/(2*a)
    print("1개의 실근이 있습니다. : " + str(quadratic_formula))
else:
	print("실근이 존재하지 않습니다..")







