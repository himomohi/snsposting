

import streamlit as st

import PIL.Image

#API 키 파일을 불러오는 코드
api_key = st.secrets['GOOGLE_API_KEY']
service= st.secrets['GOOGLE_APPLICATION_CREDENTIALS']
prompt=st.secrets['PROMPT']


####################
#코드시작 
###################

import google.generativeai as genai
genai.configure(api_key=api_key)  # credentials 인자 제거



st.header("SNS Posting AI")


#이미지 업로드
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:       
       img = PIL.Image.open(uploaded_file)
       models= genai.GenerativeModel('gemini-pro-vision')
       with st.spinner("😀SNS 포스팅 내용을 작성중이에요."):
        response=models.generate_content([prompt,img])
        with st.chat_message("ai"):
            st.image(img)
            st.write(response.text)

