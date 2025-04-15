#0411_파일_LAB
#-------------------------------------

#r : 처음부터 읽기
#w : 처음부터 쓰기, 기존거 제거
#a : append, 파일 끝에서 이어쓰기
#r+ : 파일 읽고 쓰기 모드

#rstrip() :오른쪽의 공백 제거
#split(a) :a를 기준으로 텍스트 분리

#CSV 읽기 : import csv
import csv
f = open("d:\\input.csv", 'r')
data = csv.reader(f)

for line in data :
    print(line)
    
f.close() 

# 1. 파일 복사
with open('d:\\test.txt', 'r',encoding='utf-8') as f:
    data = f.readlines()
f.close()
result = open("d:\\result.txt", 'w')
result.writelines(data)
result.close()


# 2. 연설문 데이터 분석
infile = open('d:\\introduction.txt', 'r') 

word_dic = {}
total_count =0

for line in infile :
    line = line.rstrip() #맨 오른쪽 줄바꿈 기호 삭제해서 교체
    word_list = line.split() #공백 기준으로 단어 분리하여 저장
    for word in word_list:
        word = word.lower() #모두 소문자로 변경
        word = word.strip(",") #콤마 삭제
        word = word.strip(".") #온점 삭제
        if word in word_dic : # 단어가 딕셔너리에 있으면
            word_dic[word] += 1 #횟수 추가
            total_count += 1 #전체 횟수 추가
        else :
            word_dic[word] = 1 #단어가 없으면 딕셔너리에 등록
            total_count += 1
            

outfile = open('d:\\outfile.txt', 'w') 
result = ""
for key in sorted(word_dic.keys()) :
    result = key +" " + str(word_dic[key]) + "\n" # 한 단어 한 줄에 출력
    outfile.write(result)  #한 줄씩 쓰기 -> 반복
print("총 단어 수 : " + str(total_count))
outfile.close()
infile.close()




# 3. 평균 강수량 통계
import csv 
f = open("d:\\강수량 분석.csv", 'r')
data = csv.reader(f)

n, sum = 0, 0

for line in data:
    n += 1 #월당 측정을 1로 측정
    sum += float(line[2]) #강수량 합산
    
print(f"대관령 2009년 01월 부터 2019년 12월까지의 총 강수량 : {sum}")
print(f"대관령 2009년 01월 부터 2019년 12월까지의 평균 강수량 : {sum/n}")



# 4. 행맨
import random

with open('d:\\hangman.txt', 'r', encoding='utf-8') as f :
    data = f.readlines() #데이터 불러오기
       
word = random.choice(data).rstrip() #답안 랜덤 선택
answer = list(word) #문자열을 리스트로 변환
quiz = list(len(answer)*"_") #문제 출제

chance = 10 #기회는 10번
while chance > 0 :
    user = input("단어를 추측하세요 : ")
    chance -= 1 #기회 감소
    i = 0
    for c in word :  #정답의 문자 검색
        if c == user : #정답에 유저가 입력한 문자가 있다면
            quiz[i] = c
            #word의 동일 인덱스 내용을 quiz의 같은 인덱스 자리에 넣기
        i += 1 #word의 인덱스
    print(quiz)
    
    if quiz == answer  : #정답 리스트와 문제 리스트가 같다면
        print("성공입니다.")
        break
    if chance == 0 :
        print("실패입니다.")
        break
f.close()
    






