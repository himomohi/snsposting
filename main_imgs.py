
import os
from dotenv import load_dotenv
import streamlit as st

import PIL.Image

#API 키 파일을 불러오는 코드
load_dotenv()  # 환경 변수 로드 (괄호 추가)
api_key = os.getenv('GOOGLE_API_KEY')




# 서비스 계정 키 파일의 전체 경로를 구함
# 구글API 서비스 사용시 계정키파일이 필요하다. 하여 해당 부분으로 로드 하였다.
# 현재 파일의 디렉토리 경로를 구함
current_dir = os.path.dirname(os.path.realpath(__file__))
service_account_path = os.path.join(current_dir, 'grand-proton-329404-93f5bf76d4d8.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_path  # 환경 변수 설정

####################
#코드시작 
###################

import google.generativeai as genai
genai.configure(api_key=api_key)  # credentials 인자 제거





st.header("SNS포스팅")


#이미지 업로드
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:       
       img = PIL.Image.open(uploaded_file)
       models= genai.GenerativeModel('gemini-pro-vision')
       with st.spinner("😀SNS 포스팅 내용을 작성중이에요."):
        response=models.generate_content(['항상 한글로 말해주세요. 사진을 읽고 20~30대 의 친근한 남성의 말투로 sns 에 올릴 글을 반말로 친구처럼 작성해주세요. 이것은 주로 인스타에 업로드 할꺼고 SEO에 맞고 트렌디 한 느낌을 주도록 이모지를 포함하여 센스있게 말해주세요.  , #태그 값은 SEO에 검색이 잘되도록 트렌드 를 반영하여 5가지 포함하여 주세요. 태그를 표기할때 상단에 3줄을 띄운후 작성해주세요. 본문과 구별이 잘되도록.',img])
        with st.chat_message("ai"):
            st.image(img)
            st.write(response.text)

