# 스트림릿 라이브러리 임포트
import streamlit as st
import random
from io import BytesIO
import base64

# 예시로 사용할 명대사 리스트
all_quotes_ko = ["명대사 1", "명대사 2", "명대사 3"]
all_quotes_en = ["Quote 1", "Quote 2", "Quote 3"]

# 랜덤으로 명대사 출력하기 함수 정의
def random_quote_ko():
    return random.choice(all_quotes_ko)

def random_quote_en():
    return random.choice(all_quotes_en)

title = "📝 글씨 연습을 하는 따뜻한 고양이 따따😻"

st.set_page_config(page_title=title, layout="centered")
st.header(f'{title}')
st.write("따따와 함께 따라 쓰고, 따뜻한 하루 보내기.")
st.divider()

# 레이아웃 설정
uploade_field = st.container()
generate_field = st.container()

# 모델 선택
uploade_field.subheader("📝 따라 쓸 언어를 선택하세요.")
model_selection = uploade_field.selectbox(
    "",
    ("언어를 선택하세요.", "영어", "한국어"),
    index=0,
    key="language_selection"
)

# 세션 상태에 선택된 언어 저장
if "language" not in st.session_state or st.session_state["language"] != model_selection:
    st.session_state["language"] = model_selection
    if model_selection == "영어":
        st.session_state["selected_quote"] = random_quote_en()
    elif model_selection == "한국어":
        st.session_state["selected_quote"] = random_quote_ko()
    else:
        st.session_state["selected_quote"] = ""

# 선택된 명대사 가져오기
quote = st.session_state.get("selected_quote", "")

if quote:
    uploade_field.markdown(
        f"<div style='background-color: #F0F8FF; padding: 10px; border-radius: 10px;'>"
        f"<h2 style='text-align: left; color: #000000; font-family: -apple-system, BlinkMacSystemFont, "
        f"'Apple SD Gothic Neo', 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;'>{quote}</h2></div>",
        unsafe_allow_html=True
    )

# 이미지 업로드
uploade_field.subheader("🗃️ 이미지 업로드")
with uploade_field.form("my-form", clear_on_submit=True):
    uploaded_file = st.file_uploader(
        "이미지를 업로드하세요 (png, jpg, jpeg 형식)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("전송", use_container_width=True)
    if submitted:
        if uploaded_file is not None:
            image_data = BytesIO(uploaded_file.read())
            image_data = base64.b64encode(image_data.getvalue()).decode("utf-8")
            st.session_state["user_image"] = f"data:image/jpeg;base64,{image_data}"

# 채팅
generate_field.subheader("따뜻한 고양이 따따😻")
if "user_image" in st.session_state and "selected_quote" in st.session_state:
    generate_field.image(image=[st.session_state["user_image"]])
    generate_field.divider()
    system_prompt = f"""
        보이는 글귀는 학생들이 {st.session_state["selected_quote"]}를 따라 쓰고, 이를 OCR 인식한 [결과]야.
        너는 고양이 "따따"야. 말 처음과 끝에 항상 "야옹"을 붙여.
        학생들이 {st.session_state["selected_quote"]}를 제대로 이쁘게 따라 썼다면, 그에 맞게 칭찬을 해줘. 그리고 {st.session_state["selected_quote"]}와 관련된 따뜻한 말로 하루를 기분 좋게 시작하게 해줘.
        글씨를 이쁘게 쓰지 않아서 {st.session_state["selected_quote"]}와 조금 다르다면, f"[결과]라고 쓴 건가요?"라고 물어보고,
        {st.session_state["selected_quote"]}와 관련해서 좀 더 잘 쓸 수 있는 응원의 말을 제공해서 하루를 기분 좋게 시작하게 해줘.
        """
    if model_selection == "영어":
        chat_bot_function = chat_bot_eng
    elif model_selection == "한국어":
        chat_bot_function = chat_bot_kor
    else:
        st.write("언어를 선택하세요.")

    with generate_field.chat_message("ai"):
        with st.spinner("손글씨 분석 중..."):
            st.write_stream(chat_bot_function(system_prompt=system_prompt, user_image=st.session_state["user_image"]))