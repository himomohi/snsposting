import streamlit as st
import PIL.Image
import time

# API 키 파일을 불러오는 코드
api_key = st.secrets['GOOGLE_API_KEY']
service = st.secrets['GOOGLE_APPLICATION_CREDENTIALS']
prompt = st.secrets['PROMPT']

####################
# 코드 시작
###################

import google.generativeai as genai
genai.configure(api_key=api_key)  # credentials 인자 제거

st.header("SNS Posting AI")
st.caption('SNS 포스팅 할 이미지를 업로드해주세요. ')


# 세션 상태 초기화
if 'last_request_time' not in st.session_state:
    st.session_state['last_request_time'] = 0

# 이미지 업로드
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    models = genai.GenerativeModel('gemini-pro-vision')

    # 현재 시간 및 마지막 요청 시간 확인
    current_time = time.time()
    last_request_time = st.session_state['last_request_time']

    # 1분 이내에 요청이 있었는지 확인
    if current_time - last_request_time < 60:
        st.warning("1분 안에 다시 요청할 수 없습니다.")
    else:
        with st.spinner("😀SNS 포스팅 내용을 작성중이에요."):
            response = models.generate_content([prompt, img])
            with st.chat_message("ai"):
                st.image(img)
                st.write(response.text)

        # 마지막 요청 시간 업데이트
        st.session_state['last_request_time'] = time.time()
