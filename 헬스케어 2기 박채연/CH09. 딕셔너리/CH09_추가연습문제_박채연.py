#0408 딕셔너리_추가연습문제
#----------------------------

#1. 정수 리스트 받아서 중복요소 제거/정렬하기
myList = []

for i in range(6):
    user_list = int(input("리스트에 넣을 정수를 입력하세요."))
    myList.append(user_list)
mySet=set(myList)
print(sorted(list(mySet)))


#2
dict = {}

for i in range(1,10):
    dict[i] = i**2
    
print(dict)

 
#3
d = {"apple" : 1, "banana" : 2, "grape" : 3}

for k,v in d.items():
    print(k, "->", v)

#4 
first = input("첫 번째 문자열 : ")
second = input("두 번째 문자열 : ")

first_set = set(first)
second_set = set(second)

print(f"모두 포함된 글자 : {first_set & second_set}")

#5

d1 = set({10, 20, 30, 40, 50, 60})
d2 = set({30, 40, 50, 60, 70, 80})
d3 = (d1 | d2) -(d1 & d2) #합집합 - 차집합합
print(f"어느 한 쪽에만 있는 요소들 : {d3}")
