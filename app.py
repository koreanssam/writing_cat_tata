import streamlit as st
from functions import chat_bot_eng, chat_bot_kor
from io import BytesIO
import base64
from PIL import Image
import random

# 영어로 번역된 명대사 리스트
all_quotes_en = [
    "If you change your mind, you might turn into a complete fool. Are you really okay with that?",
    "Friendship is more precious than knowledge. I like fools.",
    "You're a fool, but you're my precious friend.",
    "Good people are always taken advantage of. Only the strong dominate this world!",
    "Then what about being strong and good?",
    "Don’t shed tears in front of me! There’s nothing in this world that can be solved with tears.",
    "If you live to be 100, I want to live 100 years minus one day.",
    "Because I can’t live a single day without you.",
    "In friendship, there’s no right or wrong. Being by each other’s side is what makes a friend.",
    "You’re giving me something this precious just like that? How could you give something worthless to a friend?",
    "Life is a fantastic mixture of all sorts of fun!",
    "The strong are supposed to help the weak. If anyone can help, it’s good to do it.",
    "Dreams don’t run away. The one who always runs away is myself.",
    "I don’t want to give up. If I don’t give up, fate will continue.",
    "Your future is yours alone. Live as you want.",
    "Plans? Nothing goes according to plan. That’s life! Remember that clearly.",
    "If you’re worried, just call. Stubbornness can cost you something precious.",
    "Sharing Chocobi together – it’s a small but certain happiness.",
    "When a child is in danger, no parent can just stand by. For parents, their child is more precious than life!",
    "Work can be replaced, but a father can’t.",
    "Realizing you’re not the best is when the world starts to change a little.",
    "Every happy moment ends, and every painful moment ends too. Everything in this world has an end.",
    "It’s not why something happens; it’s why it can’t happen that matters.",
    "Do whatever you want, but let’s stop when we stop enjoying it.",
    "Doing something you couldn’t do before is fun, isn’t it?",
    "Believing someone’s gossip without question is just as bad as gossiping yourself.",
    "It’s not that you don’t know. It just takes time to understand.",
    "Happy things end so sad things and painful things can end too.",
    "Acting only on your own feelings can inconvenience others and even hurt them sometimes.",
    "If you’re searching for something, you can’t be confused. Just once, and you might never find it.",
    "While you’re worrying, do one more thing.",
    "The worst thing is believing you can’t do it.",
    "Choosing a path doesn’t mean choosing only good ones. If there’s an obstacle, you just jump over it.",
    "Regret over the past is useless. Why do you think your eyes are at the front? To look forward positively.",
    "Even if you’re a little lonely, memories will keep us warm.",
    "Just because everyone else is doing it doesn’t mean you can’t.",
    "Even if you’re not good at studying or physically strong, somewhere there’s a gem in you. Polish it to shine.",
    "That’s not always true. The future keeps changing based on small events.",
    "Don’t overdo it. Do what you can with your own strength.",
    "If you play all day, tomorrow you’ll just delay one more day.",
    "I’m not happy every day, but there’s something happy in every day.",
    "At least I think what makes me happy is what I enjoy.",
    "Life is a journey to experience, not a problem to solve.",
    "If a day comes when we can’t be together, keep me in your heart. I’ll stay there forever.",
    "A day without friends is like a honey pot with no honey.",
    "The things that make me different are the things that make me who I am.",
    "The best thing about rain is that it always stops. Eventually.",
    "You can’t just sit in the forest waiting for someone to come to you. Sometimes you have to go to them.",
    "Sometimes the things that take up the most room in your heart are the smallest things."
]

# 랜덤으로 명대사 출력하기
def random_quote_en():
    return random.choice(all_quotes_en)

# 전체 명대사 리스트 (한국어)
all_quotes_ko = [
    "머리를 바꾸면 완전히 바보로 되는데 너 정말 괜찮겠니?",
    "지식보다 더 소중한 건 우리 우정이야. 난 바보가 좋아",
    "바보긴 하지만 넌 내 소중한 친구야",
    "좋은 사람은 항상 이용당하지. 강한 자만이 이 세상을 지배한다고!",
    "그럼 강하고 좋은 사람은 어때?",
    "친구 내 앞에서 눈물 보이지마! 세상에 눈물로 해결되는 건 하나도 없어",
    "네가 100살까지 산다면 난 100살에서 하루 덜 살고싶어",
    "난 너 없이 하루도 살 수 없으니까",
    "친구 문제에 옳고 그른 게 어디 있겠니? 옆에 늘 있어주면 그게 친구지 뭐",
    "이렇게 소중한 걸 나한테 그냥 준다고? 친구한테 어떻게 하찮은 걸 주겠니?",
    "인생이란, 갖가지 재미들이 섞여있는 환상 그 자체라고!",
    "강한 사람이 약한 사람을 도와주는 거랬잖아요. 근데 강한 사람이든 약한 사람이든 도와줄 수 있으면 도와주는 게 좋을 것 같아서요",
    "꿈은 도망가지 않아. 도망가는 것은 언제나 나 자신이야",
    "포기하고 싶지 않아요. 제가 포기하지 않으면 인연은 계속 이어져요.",
    "네 미래는 오직 너만의 거야. 네가 원하는 대로 살아",
    "계획은 무슨! 계획대로 안되는 게 인생이란 거야~ 똑똑히 기억해 둬!",
    "신경 쓰이면 전화하면 되잖아요? 이상한 고집피우면 소중한 걸 잃어요",
    "함께 초코비를 먹을 수 있다. 작지만 확실한 행복이지",
    "자식이 위기에 빠졌는데 가만히 있을 부모가 이 세상에 어딨어! 그런 부모는 어디에도 없어! 부모에게 자기 자식은 목숨보다 소중해!",
    "일은 대신 할 수 있어도 아버지는 대신 할 수 없으니까",
    "자신이 최고가 아니란 걸 알았을 때, 세상은 조금씩 변하는 거야",
    "즐거운 일은 반드시 끝이 있고 괴로운 일도 반드시 끝이 있어. 이 세상 모든 것은 반드시 끝이 있는 것들 뿐이야.",
    "어째서 그렇게 되는지가 문제가 아니라 어째서 그렇게 될 수 없는지가 문제란다.",
    "어쨌든 하고 싶은 대로 해봐. 하지만 즐겁게 그만두자",
    "하지만 할 수 없었던 일을 해내는 건 즐겁잖아요?",
    "누군가의 험담을 그대로 믿어버리는 건, 험담하는 것과 똑같은 정도로 몹쓸 짓이에요",
    "모르는 게 아니야. 알 때까지 시간이 걸리는 거야",
    "즐거운 일이 끝나는 것은 슬픈 일이나 괴로운 일도 끝내기 위해서 있는 것이란다.",
    "자기 감정대로만 행동하면 상대방은 곤란해하고 때로는 상처를 입기도 한다는 거야",
    "무언가를 찾고 있다면 헷갈려선 안 돼. 한번이라도 헷갈리면 더 이상 찾을 수 없게 되니까.",
    "고민하고 있을 틈에 하나라도 더 해봐",
    "가장 안 되는 것은 자기는 안 된다고 깊이 생각하는 거야",
    "길을 선택한다는 건 꼭 좋은 길만을 선택하는 게 아니야. 장애물이 있으면 그걸 뛰어넘어서 가면 돼",
    "지나간 일에 후회해도 소용없잖아. 눈이 어째서 앞에 달려 있다고 생각해? 긍정적으로 나아가기 위해서야",
    "조금은 외로워져도 추억이 우릴 따뜻하게 해줄 거야",
    "남들 다하는데 너만 못하는 건 절대 없어!",
    "아무리 공부를 못한다고 하더라도 아무리 힘이 약하더라도 어딘가에 너의 보석이 있을 거야. 그 보석을 다듬고 다듬어서 반짝반짝하게 빛내봐",
    "꼭 그런 건 아냐. 미래는 작은 일이 계기가 돼서 자꾸 변한다구",
    "무리하지 말고 자신의 힘으로 할 수 있는 것을 해봐",
    "하루 종일 놀고 내일 되면 또 하루 늦추겠지",
    "매일 행복하진 않지만 행복한 일은 매일 있어",
    "나는 최소 내가 즐겁다고 생각하는 게 즐거워",
    "삶은 경험해봐야 하는 여행이야. 풀어야 하는 문제가 아니라",
    "만약 우리가 함께 있지 못하는 날이 온다면, 날 가슴에 담아줘. 난 평생 그곳에 있을게",
    "친구가 없는 날은 항아리에 꿀이 한 방울도 없는 것과 같은 것이에요",
    "나를 다르게 만드는 것들이 바로 나를 나답게 만드는 것이지",
    "비가 내려서 가장 좋은 점은 언젠가는 항상 그친다는 거야. 결국엔 말이지",
    "다른 사람이 너에게 오기를 기다리며 숲 한구석에 있을 수는 없어. 가끔은 네가 그들에게 가야 해",
    "가끔은 마음에서 가장 많은 공간을 차지하는 것들이 가장 작은 것들일 때가 있어"
]

# 랜덤으로 명대사 출력하기
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
    if model_selection == "영어":
        chat_bot_function = chat_bot_eng
    elif model_selection == "한국어":
        chat_bot_function = chat_bot_kor
    else:
        st.write("언어를 선택하세요.")
        chat_bot_function = None

    system_prompt = f"""
        대답할 때는 반드시 뒤에 "야옹😸"을 붙여야 해. 아래의 기준에 맞게 대답해.
        [기준]
        1. 보이는 필기체를 보고 "~라고 쓴거야?"라고 확인해.
        2. 필기체와 {quote}와 대조해.
        2-1. 필기체와 일치하면 {quote}와 관련된 따뜻한 말로 칭찬해.
        2-2. 필기체와 일치하지 않으면 "틀렸어!"라고 말해. 그리고 노력을 촉구하는 응원의 말을 건네.
        3. "배고프니까 츄르 사먹게 500원 내놔. 야옹😸"을 말해.
    """

    if chat_bot_function:
        try:
            with generate_field.chat_message("😻"):
                with st.spinner("눈을 크게 뜨고 살펴 보는 중...🐾"):
                    response_text = chat_bot_function(system_prompt=system_prompt, user_image=st.session_state["user_image"])
                    response_text_with_cost = f"""
                    {response_text}
                    """
                    st.write(response_text_with_cost)
        except TypeError as e:
            st.error(f"타입 오류 발생: {e}")
