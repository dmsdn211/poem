import streamlit as st
import random

st.set_page_config(page_title="오늘의 시 한 편 ✨", page_icon="📜")

# 🎨 헤더
st.markdown("<h1 style='text-align: center; color: #a0522d;'>📖 오늘의 시 한 편 🌿</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>당신의 하루에 감성을 더해줄 시를 선물합니다 🎁</p>", unsafe_allow_html=True)
st.markdown("---")

# 🌸 시 리스트
poems = [
    {
        "title": "풀꽃 🌱",
        "author": "나태주 ✍️",
        "content": "자세히 보아야\n예쁘다\n오래 보아야\n사랑스럽다\n너도 그렇다",
        "mood": "잔잔한 위로 💕"
    },
    {
        "title": "서시 🌅",
        "author": "윤동주 🌙",
        "content": "죽는 날까지 하늘을 우러러\n한 점 부끄럼이 없기를\n잎새에 이는 바람에도\n나는 괴로워했다",
        "mood": "자기성찰과 결의 🕊️"
    },
    {
        "title": "너에게 묻는다 ❓",
        "author": "정호승 🪶",
        "content": "연탄재 함부로 차지 마라\n너는\n누구에게 한 번이라도 뜨거운 사람이었느냐",
        "mood": "강렬한 울림 🔥"
    },
    {
        "title": "행복 😊",
        "author": "유하 🌈",
        "content": "사랑하는 사람이\n있다는 것은\n참으로 행복한 일이다",
        "mood": "따뜻한 감성 ☀️"
    },
    {
        "title": "길 🛤️",
        "author": "김춘수 🍁",
        "content": "길은 내가 걷기 전에는\n길이 아니었네\n내가 걸으면서\n길이 되었네",
        "mood": "인생의 여정 🚶"
    }
]

# 🎲 세션 상태 초기화
if "poem" not in st.session_state:
    st.session_state.poem = random.choice(poems)

# 🔁 버튼 클릭 시 새로운 시 선택
if st.button("🔄 다른 시도 추천해줘!"):
    st.session_state.poem = random.choice(poems)

poem = st.session_state.poem

# 📜 시 출력
st.markdown(f"<h2 style='color: #d2691e;'>📝 {poem['title']}</h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color: #555;'>by {poem['author']}</h4>", unsafe_allow_html=True)
st.markdown(f"<pre style='background-color:#fff8dc; padding: 20px; border-radius: 10px; font-size: 16px;'>{poem['content']}</pre>", unsafe_allow_html=True)

# 🌈 해석 or 느낌
st.markdown(f"<p style='font-size: 18px; color: #6a5acd;'>✨ {poem['mood']}</p>", unsafe_allow_html=True)

# 🎁 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>🌷 하루 한 편의 시가 당신에게 위로가 되길 바라며 🌷</p>", unsafe_allow_html=True)
