import streamlit as st
import openai

st.set_page_config(page_title="PromptMentor Scanner", layout="centered", initial_sidebar_state="collapsed")
st.title("🧠 PromptMentor – Scanner Builder")
st.write("Let me help you build a trading scanner prompt step-by-step.")

# Load API Key
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# Step 1: User Input
user_goal = st.text_input("What do you want to scan for?", placeholder="e.g., EMA crossover with high volume")

if user_goal:
    with st.spinner("Thinking through your strategy..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're an expert trading bot strategist. Ask follow-up questions to clarify user intent and build a complete Pine Script scanner prompt."},
                {"role": "user", "content": user_goal}
            ]
        )
        answer = response.choices[0].message.content
        st.subheader("🛠 Generated Follow-Up Questions or Prompt:")
        st.write(answer)

