#streamlit run train1.py

import streamlit as st
import time

st.set_page_config(layout="wide") # 기본값 : centered

st.title('이것은 제목입니다')
st.header('이것은 헤더입니다')
st.subheader('이것은 서브헤더입니다')

#st.markdown : caption, latex, code block 활용 가능
st.markdown("---") # 영역 구분을 위한 수평선 
st.divider() # 수평선 그리는 다른 방법

col1, col2 = st.columns([2,3])

with col1:
    st.subheader('column1 영역입니다')
with col2:
    st.subheader('column2 영역입니다')
    st.checkbox('column2의 checkbox')

col1.subheader('다른 방법으로 작성한 col1 서브 헤더')
col2.checkbox('다른 방법으로 생성한 checkbox')

st.markdown("---")

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
    st.write('tab1 test')
with tab2:
    st.write('tab2 test')
    
st.markdown("---")

#사이드바 생성성
st.sidebar.title('이곳은 사이드바입니다')
st.sidebar.checkbox('사이드바의 체크박스')

#접었다 펼수 있는 영역 생성
with st.sidebar.expander("필터 옵션"): # 제목
    option1 = st.checkbox("옵션 1") # 내부 콘텐츠 
    option2 = st.slider("값 선택", 0, 100, 50)

with st.sidebar.expander("추가 정보"):
    st.write("여기에 추가적인 설명을 넣을 수 있습니다.")

# 시각적으로 그룹화하거나 레이아웃을 관리하기 위한 컨테이너
container1 = st.sidebar.container()
container1.markdown("---")
container1.subheader("설정 그룹 1")
value1 = container1.number_input("값 1", 0, 100)
value2 = container1.number_input("값 2", 0, 100)

container2 = st.sidebar.container()
container2.subheader("설정 그룹 2")
checkbox1 = container2.checkbox("활성화")
radio_option = container2.radio("선택", ["A", "B"])

st.write(f"값 1: {value1}, 값 2: {value2}")
st.write(f"활성화: {checkbox1}, 선택: {radio_option}")
container1.markdown("---")

# 비어있는 공간을 위한 placeholder -> 나중에 동적으로 삽입하거나 업데이트 가능 
    # 특정 조건이 충족되었을 때 동적으로 표시(메시지, 이미지, 로딩 애니메이션)
status_area = st.sidebar.empty()

if st.button("작업 시작"):
    status_area.info("작업 중...")
    time.sleep(3)
    status_area.success("작업 완료!")
else:
    status_area.info("대기 중...")

st.write("메인 콘텐츠")

st.markdown("---")

# 이미지 불러오기
from PIL import Image

hangang = Image.open('hangang.png')

col3, col4 = st.columns([2,3])

with col3 :
    st.title('col3')
with col4 :
    st.title('col4')
    st.checkbox('col4의 checkbox')
col4.image(hangang)

