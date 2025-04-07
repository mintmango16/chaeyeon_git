#0403 자료의 종류_추가연습문제
#----------------------------

#1
user_str = input("문자열을 입력하세요 : ")
print(user_str + "하는 중")


#2
sign = input("기호를 입력하세요 : ") #기호는 문자 2개로 가정 
insert_str = input("중간에 삽입할 문자열을 입력하세요 : ")
print(sign[0]+insert_str+sign[1])


#3
drive= input("드라이브 이름 : ")
directory = input("디렉토리 이름 : ")
file = input("파일 이름 : ")
extension = input("확장자 이름 : ")

print(f"완전한 파일 이름은 {drive}:{directory}{file}.{extension}")








