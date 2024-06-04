import streamlit as st
from PIL import Image
import requests
import io

# 채색 이미지 변환 함수
def colorize_image():
    st.title("흑백 사진을 채색하는 웹 앱")
    st.write("흑백 사진을 업로드하면 AI가 채색해드립니다.")

    # 사용자로부터 흑백 이미지 파일 업로드 받기
    uploaded_file = st.file_uploader("흑백 이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"])

    # 이미지 업로드 시 처리
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # 원본 흑백 이미지 표시
        st.image(image, caption="원본 흑백 이미지", use_column_width=True)

        # 흑백 이미지 채색 함수
        def colorize_via_api(image):
            # 이미지를 바이트 스트림으로 변환
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = buffered.getvalue()

            # API 요청 (여기서는 예시로 DeepAI의 colorizer API 사용)
            response = requests.post(
                "https://api.deepai.org/api/colorizer",
                files={"image": img_str},
                headers={"api-key": "YOUR_DEEPAI_API_KEY"}
            )
            return response.json()

        # AI API를 사용하여 이미지 채색
        result = colorize_via_api(image)
        if "output_url" in result:
            colorized_image_url = result["output_url"]
            colorized_image = Image.open(requests.get(colorized_image_url, stream=True).raw)

            # 채색된 이미지 표시
            st.image(colorized_image, caption="채색된 이미지", use_column_width=True)

            # 채색된 이미지 다운로드 버튼
            buf = io.BytesIO()
            colorized_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(label="채색된 이미지 다운로드", data=byte_im, file_name="colorized_image.png", mime="image/png")
        else:
            st.error("이미지 채색에 실패했습니다. 다시 시도해주세요.")

