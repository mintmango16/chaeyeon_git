#0411_모듈과 라이브러리_tkinker 제작 
#-------------------------------------

import math
result = math.gcd(255,300) #최대공약수 출력
print(result)

from math import *  # math 모든 모듈 불러오기
result1 = gcd(255,300)
print(result1)

#----------------------------------------------
from tkinter import *
window = Tk() #윈도우 창 띄우기

# button = Button(window, text = "클릭하세요 !")
# button.pack()

w = Label(window, text= "박스 1", bg = "red", fg = "white")
w.place(x=0, y=0) #위치 지정, 절대 배치 관리자자
w = Label(window, text= "박스 2", bg = "green", fg = "black")
w.place(x=20, y=20) 
w = Label(window, text= "박스 3", bg = "blue", fg = "white")
w.place(x=40, y=40) 

window.mainloop()


 
#버튼 이벤트 처리 : 섭씨 화씨 변환
 
from tkinter import *
window = Tk() #윈도우 창 띄우기

def c():
    f = float(e1.get())
    C = (f-32) * (5/9)
    e2.insert(0, str(C))

def f():
    c = float(e2.get())
    F = (c* 1.8) + 32
    e1.insert(0, str(F))


l1 = Label(window, text = "화씨", font = "helvetica 16 italic") #표시시
l2 = Label(window, text = "섭씨", font = "helvetica 16 italic")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window, bg = "skyblue", fg = "blue") #입력받기기
e2 = Entry(window, bg = "skyblue", fg = "blue")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text = "화씨 -> 섭씨", command = c,
            font = "helvetica 16")
b2 = Button(window, text = "섭씨 -> 화씨", command = f,
            font = "helvetica 16")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()

 
#윈도우 창 메뉴 만들기
import tkinter as tk
def open():
    pass

def quit():
    window.quit()
    
window = tk.Tk()
menubar = tk.Menu(window) #window에 메뉴바 생성
filemenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command = open)
filemenu.add_command(label="종료", command = open)

menubar.add_cascade(label="파일", menu=filemenu)

window.config(menu=menubar)
window.mainloop()

 
# 마우스로 그림그리기
from tkinter import *

def paint(event): #점을 생성
    x1, y1 = (event.x-1), (event.y+1) #event.x :마우스 좌표 정보
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2) #지정한 위치에 타원 그리기

window = Tk()
canvas = Canvas(window) #그림그리는 도화지를 window에 생성
canvas.pack() #생성한 캔버스를 창에 표시
canvas.bind("<B1-Motion>", paint) #bund는 event 정보를 paint 에 넘겨줌
    # 마우스 왼쪽버튼 = B1, B1을 누르거나 드래그하면 paint 함수 실행
window.mainloop() #윈도우 창 계속 유지