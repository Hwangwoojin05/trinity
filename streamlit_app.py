import streamlit as st

st.title("🎈 황우진의 첫 번째 작품")
st.info(
    "부천의 물주먹"
)
st.write(
    "사랑해요 한국"
)
st.link_button("쌈뽕한 로블록스 플레이 나우", 'https://www.roblox.com/ko')
st.image("https://media4.giphy.com/media/UaaJjGlexmLyHGkNVy/200.webp?cid=82a1493bynsupb8nuczr9ex10bmgrf4fwys8hxdv1bxxtl3h&ep=v1_gifs_trending&rid=200.webp&ct=g", caption="friend")
# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")
    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["당신은 이세계의 용사입니다"])
st.write("선택한 옵션:", option)
name=st.text_area("아버지 성함을 입력해주세요.")

if name== "이재우":
    st.success(name+"님이 시군요!")
else:
    st.error("안녕히 가십쇼")
st.error(name+"가 당신의 아버지 이름입니다")
gender=st.radio("성별을 선택하세요",["남성","여성","크래파스","전기톱"])
st.info("선택한 성별:"+gender)