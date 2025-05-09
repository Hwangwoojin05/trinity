# # 
# import streamlit as st

# # 🎨 제목 및 소개
# st.title("🎈 황우진의 첫 번째 작품")
# st.info("부천의 물주먹")
# st.write("사랑해요 한국")

# # 🔗 링크 버튼
# st.link_button("쌈뽕한 로블록스 플레이 나우", 'https://www.roblox.com/ko')

# # 📷 이미지 표시
# st.image(
#     "https://media4.giphy.com/media/UaaJjGlexmLyHGkNVy/200.webp",
#     caption="friend"
# )

# # 📦 열 나누기
# col1, col2 = st.columns(2)
# with col1:
#     st.write("왼쪽 열입니다.")
# with col2:
#     st.write("오른쪽 열입니다.")

# # 🗂 탭 나누기
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])
# with tab1:
#     st.write("탭 1에 해당하는 내용입니다.")
# with tab2:
#     st.write("탭 2에 해당하는 내용입니다.")

# # 📖 접이식 설명
# with st.expander("ℹ️ 자세한 설명 보기"):
#     st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

# # 🧭 사이드바
# st.sidebar.title("📌 사이드바 메뉴")
# option = st.sidebar.selectbox("옵션을 선택하세요", ["당신은 이세계의 용사입니다"])
# st.write("선택한 옵션:", option)

# # 🧾 사용자 입력
# name = st.text_area("아버지 성함을 입력해주세요.")

# if name == "이재우":
#     st.success(name + "님이 시군요!")
# else:
#     st.error("안녕히 가십쇼")

# st.error(name + "가 당신의 아버지 이름입니다")

# # 🚻 성별 선택
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "크래파스", "전기톱"])
# st.info("선택한 성별: " + gender)

# # 🤖 GPT 연동 (OpenAI 부분은 그대로 유지)
# import openai

# st.header("gpt 출전")
# user_api_key = st.secrets["openai"]["api_key"]

# if user_api_key:
#     from openai import OpenAI
#     client = OpenAI(api_key=user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)
import streamlit as st
import openai
st.set_page_config(
    page_title="나의 LLM 웹앱",   # 브라우저 탭 제목
    page_icon="📘",              # 브라우저 탭 파비콘
    layout="centered"           # 화면 레이아웃: centered 또는 wide
)

# 🎨 앱 제목
st.title("🎈 황우진의 첫 번째 작품")
st.info("부천의 물주먹")

# 🗂 탭 구성
탭1, 탭2, 탭3, 탭4 = st.tabs(["홈", "입력 폼", "GPT 출전", "기타"])

# 🔹 탭 1: 홈 화면
with 탭1:
    st.write("🇰🇷 사랑해요 한국")
    st.link_button("쌈뽕한 로블록스 플레이 나우", 'https://www.roblox.com/ko')
    st.image(
        "https://media4.giphy.com/media/UaaJjGlexmLyHGkNVy/200.webp",
        caption="friend"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write("왼쪽 열입니다.")
    with col2:
        st.write("오른쪽 열입니다.")

    with st.expander("ℹ️ 자세한 설명 보기"):
        st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

# 🔹 탭 2: 입력 폼
with 탭2:
    st.subheader("🧾 사용자 입력 폼")
    
    # 사이드바
    st.sidebar.title("📌 사이드바 메뉴")
    option = st.sidebar.selectbox("옵션을 선택하세요", ["당신은 이세계의 용사입니다"])
    st.write("선택한 옵션:", option)

    # 이름 입력
    name = st.text_area("아버지 성함을 입력해주세요.")

    if name == "이재우":
        st.success(name + "님이 시군요!")
    else:
        st.error("안녕히 가십쇼")

    st.error(name + "가 당신의 아버지 이름입니다")

    # 성별
    gender = st.radio("성별을 선택하세요", ["남성", "여성", "크래파스", "전기톱"])
    st.info("선택한 성별: " + gender)

# 🔹 탭 3: GPT 기능
with 탭3:
    st.header("🤖 GPT 출전")
    
    # secrets에서 API 키 불러오기
    user_api_key = st.secrets["openai"]["api_key"]

    if user_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=user_api_key)
        prompt = st.text_input("프롬프트를 입력해주세요.")

        if prompt:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)

# 🔹 탭 4: 기타 (여유 공간)
with 탭4:
    st.write("여기에 추가 기능을 넣을 수 있습니다. 예: 파일 업로드, 차트 시각화 등")

with 탭5:
    st.write("누르지마")