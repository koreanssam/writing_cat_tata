import streamlit as st
from langchain_core import output_parsers
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def chat_bot_eng(system_prompt, user_image):
    context = HumanMessage(content=[
        {
            "type": "text",
            "text": system_prompt,
        },
        {
            'type': 'image_url',
            'image_url': {"url": user_image}
        }
    ])
    llm = ChatGoogleGenerativeAI(model=st.secrets["gem_model"], api_key=st.secrets["gem_api_key"])
    chain = llm | output_parsers.StrOutputParser()
    return chain.invoke([context])

def chat_bot_kor(system_prompt, user_image):
    context = HumanMessage(content=[
        {
            "type": "text",
            "text": system_prompt,
        },
        {
            'type': 'image_url',
            'image_url': {"url": user_image}
        }
    ])
    llm = ChatOpenAI(model=st.secrets["gpt_model"], api_key=st.secrets["gpt_api_key"])
    chain = llm | output_parsers.StrOutputParser()
    return chain.invoke([context])
