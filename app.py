import streamlit as st
from PIL import Image, ImageOps
import io

# Streamlit 앱 설정
st.set_page_config(page_title="이미지 변환 웹 앱", layout="wide")

# 사이드바 메뉴
st.sidebar.title("메뉴")
app_mode = st.sidebar.selectbox("선택하세요", ["흑백 변환", "채색 변환"])

if app_mode == "흑백 변환":
    st.title("그림 파일을 흑백으로 변환하는 웹 앱")
    st.write("그림 파일을 업로드하면 흑백으로 변환해드립니다.")

    # 사용자로부터 이미지 파일 업로드 받기
    uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"])

    # 이미지 업로드 시 처리
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # 원본 이미지 표시
        st.image(image, caption="원본 이미지", use_column_width=True)

        # 이미지 흑백 변환 함수
        def convert_to_black_and_white(image):
            # 이미지를 흑백으로 변환
            grayscale_image = ImageOps.grayscale(image)
            return grayscale_image

        # 흑백 이미지 변환
        bw_image = convert_to_black_and_white(image)

        # 흑백 이미지 표시
        st.image(bw_image, caption="흑백 이미지", use_column_width=True)

        # 흑백 이미지 다운로드 버튼
        buf = io.BytesIO()
        bw_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(label="흑백 이미지 다운로드", data=byte_im, file_name="bw_image.png", mime="image/png")
elif app_mode == "채색 변환":
    import colorize
    colorize.colorize_image()
