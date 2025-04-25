import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # 이미지 처리 라이브러리

# 환율 정보 
exchange_rates = {
    # 미국 
    ("대한민국 원", "미국 달러"): 0.0007,
    ("미국 달러", "대한민국 원"): 1441.50,
    
    # 중국
    ("대한민국 원", "중국 위안"): 0.0048,  
    ("중국 위안", "대한민국 원"): 197.47,   
    
    # 일본
    ("대한민국 원", "일본 엔"): 0.085,     
    ("일본 엔", "대한민국 원"): 1003.97,      
    
    # 영국
    ("대한민국 원", "영국 파운드"): 0.00058, 
    ("영국 파운드", "대한민국 원"): 1870.00,
    }

currencies = ["대한민국 원", "미국 달러", "중국 위안", "일본 엔", "영국 파운드"]

def convert_currency():
    
    global from_cur, to_cur
    try:
        amount = float(entry_amount.get())
        from_cur = combo_from.get() # 현재 선택된 값을 가져옴 
        to_cur = combo_to.get()
        rate = exchange_rates.get((from_cur, to_cur), 
                                  # 해당하는 환율 검색, 딕셔너리 형태이므로 키 검색시 value 반환
                                  None)  # 없을 시 반환값 
        
        if rate is None:
            messagebox.showerror("오류", "해당 환율 정보가 없습니다.")
            return
        
        result = amount * rate
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{result:.2f}")
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력해주세요.")

def update_label(event):
    # 드롭박스에서 선택된 값 가져오기
    from_cur = combo_from.get()
    to_cur = combo_to.get()
    
    # 선택된 통화에 해당하는 환율 가져오기
    rate = exchange_rates.get((from_cur, to_cur), None)
    
    if rate is not None:
        # 라벨 텍스트 변경
        sub_title2.config(text=f"= {rate} {to_cur}")
    else:
        sub_title2.config(text="통화를 선택하세요.")   
    #1 {from_cur} 
    
# 메인 창
window = tk.Tk()
window.title("환율 계산기")
window.geometry("900x500") # 창 크기 설정 
window.configure(bg="white") # 전체 배경 색상 설정 

# 제목 설정 
title = tk.Label(window, text= "환율 정보",
                 font=("맑은 고딕", 18), bg = "white", fg = "black")
title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# 기준 설명  
sub_title = tk.Label(window, text= f"1 대한민국 원 ",
                 font=("맑은 고딕", 10), bg = "white", fg = "black")
sub_title.grid(row=1, column=0, padx=10, pady=5, sticky="w")

sub_title2 = tk.Label(window, text= "",
                 font=("맑은 고딕", 13), bg = "white", fg = "black")
sub_title2.grid(row=2, column=0, padx=10, pady=5, sticky="w")


# 기준 설명  
title = tk.Label(window, text= "2025년 4월 25일 기준",
                 font=("맑은 고딕", 10), bg = "white", fg = "black")
title.grid(row=3, column=0, padx=10, pady=5, sticky="w")


# 금액 입력
entry_amount = tk.Entry(window, font=("맑은 고딕", 15))
entry_amount.insert(0, "1000") # 인덱스 0 위치에 문자열 삽입 (초기값 설정)
entry_amount.grid(row=4, column=0, padx=10, pady=10)

combo_from = ttk.Combobox(window, values=currencies, font=("맑은 고딕", 15), 
                          state="readonly") # 드롭박스 목록에서만 선택 가능(직접 입력 불가) 
combo_from.set("대한민국 원") # 초기값 설정 
combo_from.grid(row=4, column=1, padx=10, pady=10)

# 결과 출력
entry_result = tk.Entry(window, font=("맑은 고딕", 15))
entry_result.grid(row=5, column=0, padx=10, pady=10)

combo_to = ttk.Combobox(window, values=currencies, font=("맑은 고딕", 15),
                        state="readonly")
combo_to.set("국가 통화를 선택하세요.") # 초기값 설정 
combo_to.grid(row=5, column=1, padx=10, pady=10)


# 드롭다운 선택 시 자동 환산
combo_from.bind("<<ComboboxSelected>>", lambda e : (convert_currency(), update_label(e)))
combo_to.bind("<<ComboboxSelected>>", lambda e : (convert_currency(), update_label(e)))


# 초기값을 기준으로 라벨 업데이트
update_label(None)

# 변환 버튼
#btn_convert = tk.Button(window, text="변환", command=convert_currency)
#btn_convert.grid(row=3, column=0, padx=5, pady=10)

# 이미지 삽입
image = Image.open(r"C:\\Users\\CY\\바탕 화면\\아시아 경제 헬스케어반\\image.png")  # 이미지 파일 경로 지정
photo = ImageTk.PhotoImage(image)  # Tkinter에서 사용할 수 있는 형식으로 변환

# 이미지 삽입 위치: grid에서 오른쪽 정렬 
image_label = tk.Label(window, image=photo, bg="white")
image_label.photo = photo  # 사진 객체를 메모리에 유지하기 위해 저장
image_label.place(x=525, y=150) 

window.mainloop()
