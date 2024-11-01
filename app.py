import streamlit as st
from functions import chat_bot_eng, chat_bot_kor
from io import BytesIO
import base64
from PIL import Image
import random

# 영어 명대사
all_quotes_en = [
    "If we can’t accept limitations, then we’re no better than the bad guys.",
    "With great power comes great responsibility.",
    "I want to choose my own path. Live in the moment.",
    "Cowards never start. The weak never finish and the winners never quit.",
    "Arrogance and fear keep you from learning the simplest and most significant lesson of all.",
    "I can do this all day.",
    "Human development may feel slow, but something great may emerge in the process.",
    "I was suffused by the injunctions. Never repeat.",
    "It’s still you inside of it.",
    "You are the light of my life, my precious son, my little Star-Lord.",
    "You’re her hero, Scott. Just be the person that she already thinks you are.",
    "It’s hard for a good man to be a king.",
    "Please don’t say that. It was real. It was real to me. You are my mother. You were my real mother.",
    "We can’t do this alone. We need you.",
    "The entire time I knew him, he only ever had one goal to wipe out half the universe.",
    "Hope is the greatest of the gifts we receive.",
    "Today’s special moments are tomorrow’s memories.",
    "I have just met you and I love you.",
    "I’d rather die tomorrow than live a hundred years without knowing you.",
    "Because when I look at you, I can feel it. And I look at you and I’m home.",
    "My dream wouldn’t be complete without you in it.",
    "Love is putting someone else’s needs before yours.",
    "You are my greatest adventure.",
    "Whatever gift awaits will be just as special as you.",
    "You must not let anyone define your limits because of where you come from. Your only limit is your soul.",
    "Sometimes the smallest things take up the most room in your heart.",
    "Venture outside your comfort zone. The rewards are worth it.",
    "Our fate lives within us, you only have to be brave enough to see it.",
    "You control your destiny. You don’t need magic to do it.",
    "Never say goodbye because goodbye means going away and going away means forgetting.",
    "The very things that hold you down are going to lift you up.",
    "Don’t spend your time lookin’ around for something you want that can’t be found.",
    "If watching is all you’re gonna do, then you’re gonna watch your life go by without ya.",
    "A true hero isn’t measured by the size of his strength but by the strength of his heart.",
    "It’s up to you how far you’ll go. If you don’t try, you’ll never know.",
    "If you keep on believing the dream that you wish will come true.",
    "A woman doesn’t know how powerful her voice is until she has been silenced.",
    "There comes a day when you’re gonna look around and realize happiness is where you are.",
    "If your mind doesn’t grow old, People never grow old.",
    "A conscience is that still, small voice that people won’t listen to.",
    "There is no one who can’t fall. However, only those who get up again will learn how to move forward."
]

# 한글 명대사
all_quotes_ko = [
    "만약 우리가 한계를 인정하지 못한다면, 우리 또한 나쁜 놈들과 다름없어.",
    "큰 힘에는 큰 책임이 따른다.",
    "이젠 나의 길을 가겠어. 매 순간을 누리며.",
    "겁쟁이들은 시작도 하지 않지, 약한 자들은 끝까지 해내는 법이 없으며, 승자는 절대로 포기하지 않아.",
    "거만함과 두려움이 너를 가장 간단하고 의미 있는 것들을 배우는 것으로부터 막는단다.",
    "하루종일도 할 수 있어.",
    "인류의 발전이 더디게 느껴질지도 모르겠지만, 그 과정에서 위대한 것이 나타날 수도 있어.",
    "난 명령에 따를 뿐인 자들에게 휘둘려 살았어. 다신 반복하지 않아.",
    "그 안에 있는 건 당신이야.",
    "넌 내 삶의 빛이고, 가장 소중한 보물이란다, 나의 작은 스타.",
    "당신은 캐시의 영웅이야, 스콧. 캐시가 생각하는 그런 사람이 되려고 해봐.",
    "착한 사람은 왕이 되기 어려운 법이다.",
    "제발 그렇게 말하지 마. 내게는 진짜였어. 당신은 우리 엄마이고, 나의 진짜 엄마였어.",
    "우리는 혼자서 이걸 감당할 수 없어. 당신이 필요해.",
    "내가 그를 알고 나서부터 보면 그는 오로지 단 하나의 목표밖엔 없었어. 우주의 절반을 쓸어버리는 것.",
    "희망은 우리가 받은 가장 위대한 선물이에요.",
    "오늘의 특별한 순간들은 내일의 기억들이다.",
    "너를 방금 만났고 사랑해.",
    "너를 알지 못하는 백년을 살 바에 죽는 게 나아.",
    "왜냐하면 내가 너를 볼 때, 나는 느껴져. 그리고 너를 보면 나는 집이야.",
    "나의 꿈은 너 없이는 완전하지 않아.",
    "사랑은 너보다 다른 사람의 필요함을 우선시하는 것이야.",
    "너는 나의 가장 위대한 모험이야.",
    "어떤 선물이 기다리고 있든, 당신만큼 특별할 거에요.",
    "남이 당신의 한계를 정하게 하지 마세요. 당신의 한계는 당신의 영혼밖에 없답니다.",
    "한 사람의 마음을 채우는 것이 가끔은 아주 작은 것들이야.",
    "안전지대 밖에서 모험을 해보세요. 보상은 그만한 가치가 있을 거예요.",
    "운명은 항상 우리 곁에 있죠, 당신은 운명을 볼 수 있을 만큼 용감해지기만 하세요.",
    "당신의 운명은 당신이 통제해요. 마법은 필요 없어요.",
    "작별 인사는 절대 하지 마요. 작별 인사는 멀리 간다는 것이고 멀리 간다는 것은 잊는다는 거니까요.",
    "당신을 억누르고 있는 그것들이 당신을 끌어올릴 수 있을 거예요.",
    "찾을 수 없는 것을 찾느라 시간을 낭비하지 마세요.",
    "당신이 하는 일이 구경하는 것이라면 당신은 당신 없이 당신의 삶이 지나가는 것을 보게 될 거예요.",
    "진정한 영웅은 그의 힘의 크기가 아닌 그의 마음의 크기를 측정해요.",
    "얼마나 멀리 갈 수 있는지는 당신에게 달려있죠. 해보지 않으면 절대 알 수 없을 거예요.",
    "계속 믿는다면 당신이 소망하는 꿈이 현실이 될 거예요.",
    "여자는 침묵할 때까지 자신의 목소리가 얼마나 강한지 모릅니다.",
    "주위를 둘러보고 행복이 자신이 있는 그곳이라는 것을 깨달은 날이 올 거야.",
    "마음이 늙지 않으면, 사람은 영원히 늙지 않아.",
    "양심은 사람들에게 들리지 않는 작은 목소리야.",
    "넘어지지 않는 사람은 없어. 단, 다시 일어나는 사람만이 앞으로 나아가는 법을 배우는 거야."
]

# 명대사 출력
def random_quote_en():
    return random.choice(all_quotes_en)
def random_quote_ko():
    return random.choice(all_quotes_ko)

title = "📝 글씨 연습을 하는 따뜻한 고양이 따따😻"

st.set_page_config(page_title=title, layout="centered")
st.header(f'{title}')
st.write("<h3>따따와 함께 따라 쓰는 따뜻한 말</h3>", unsafe_allow_html=True)
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
    submitted = st.form_submit_button("타타에게 물어보기", use_container_width=True)
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

    if model_selection == "영어" 
        chat_bot_function = chat_bot_kor
    elif model_selection == "한국어":
        chat_bot_function = chat_bot_eng
    else:
        st.write("언어를 선택하세요.")
        chat_bot_function = None

    system_prompt = f"""
        너는 사람들의 마음을 치유하는 치유사야.
        대답할 때는 반드시 뒤에 "야옹😸"을 붙여야 해.
        보이는 필기체를 보고 "~라고 쓴거야?"라고 확인해.
        필기체를 {quote}와 대조해.
        일치하면 {quote}와 관련된 따뜻한 말로 하루를 기분 좋게 시작하게 건네.
        일치하지 않으면 노력을 촉구하는 응원의 말을 건네.
    """

    if chat_bot_function:
        try:
            with generate_field.chat_message("😻"):
                with st.spinner("눈을 크게 뜨고 살펴 보는 중...🐾"):
                    response_text = chat_bot_function(system_prompt=system_prompt, user_image=st.session_state["user_image"])
                    response_text_with_cost = f"{response_text}\n\n 배고파! 츄르 사먹게 500원 내놔. 야옹😸"
                    st.write(response_text_with_cost)
        except TypeError as e:
            st.error(f"타입 오류 발생: {e}")
