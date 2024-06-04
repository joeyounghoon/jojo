import streamlit as st
import openai

# Streamlit 페이지 설정
st.set_page_config(page_title="OpenAI Chatbot", page_icon=":robot_face:")

# API Key 입력 받기
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# 챗봇 상호작용 기록 초기화
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# OpenAI API 호출 함수
def get_openai_response(api_key, user_input):
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# 사용자 입력 처리
if api_key:
    user_input = st.text_input("You:", key="user_input")
    if user_input:
        response = get_openai_response(api_key, user_input)
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Assistant: {response}")
        st.experimental_rerun()

# 챗봇 대화 기록 표시
st.subheader("Chatbot Conversation")
for message in st.session_state.chat_history:
    st.write(message)
