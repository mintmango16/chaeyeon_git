#0411_파일_추가연습문제
#-------------------------------------

# 1. 파일 전부 읽는 프로그램

f = open("D:\\input.txt", "r")
for line in f :
    line = line.rstrip() #오른쪽의 공백 제거
    print(line)
f.close()


# 2. 파일 모든줄 읽어서 리스트에 저장하기

f = open("D:\\input.txt", "r")
data = f.readlines() #여러줄일 경우 리스트로 자동 저장
f.close()
print(data) #리스트 출력


# 3.
#d://words.txt

filename = input("파일 이름을 입력하세요. : ")
infile = open(filename, "r")
char_list=[]
for line in infile : #한 줄씩 가져오기
    line = line.rstrip() #줄마다 맨 뒤 줄바꿈 제거
    for char in line: #한줄에서 한글자씩 반복
        char_list.append(char) 
        #한글자씩 글자 리스트에 넣기 -> 글자를 하나씩 모두 분리
print(len(char_list)) #리스트 안의 요소 개수 출력 = 글자의 개수 

infile.close()


# 4.
#d://words.txt

filename = input("파일 이름을 입력하세요. : ")
infile = open(filename, "r")

char_list=[]
for line in infile : #한 줄씩 가져오기
    line = line.rstrip() #줄마다 맨 뒤 줄바꿈 제거
    for char in line: #한줄에서 한글자씩 반복
        char_list.append(char) 
        #한글자씩 글자 리스트에 넣기 -> 글자를 하나씩 모두 분리

char_dict = {}
for c in char_list :
    if c in char_dict: #문자가 딕셔너리에 있다면
        char_dict[c] +=1 #빈도 증가
    else :
        char_dict[c] = 1 #없으면 등록
print(char_dict)

infile.close()




