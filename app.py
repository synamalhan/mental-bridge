import streamlit as st
import requests

# -------------------------
# Config + Sidebar
# -------------------------
st.set_page_config(page_title="Mental Health Bridge", layout="centered")

with st.sidebar:
    st.title("🧬 Profile")
    st.session_state['sensitivity'] = st.slider(
        "Sensitivity to emotional topics", 1, 10, st.session_state.get('sensitivity', 5)
    )
    st.session_state['reactions'] = st.text_area(
        "Common reactions",
        st.session_state.get('reactions', ''),
        help="e.g. shuts down, dismisses, gets anxious"
    )
    st.session_state['tone'] = st.selectbox(
        "Preferred tone",
        ["Calm", "Direct", "Empathetic", "Logical", "Emotional"],
        index=["Calm", "Direct", "Empathetic", "Logical", "Emotional"].index(
            st.session_state.get('tone', 'Calm')
        )
    )

# -------------------------
# Model Utility
# -------------------------
def call_mistral(prompt: str, model: str = "mistral") -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=15
        )
        if response.ok:
            return response.json().get("response", "").strip()
        else:
            return "⚠️ Error: Model response failed."
    except Exception as e:
        return f"⚠️ Error connecting to Ollama: {e}"

# -------------------------
# Main UI
# -------------------------
st.title("🧠 Mental Health Bridge")
st.markdown("Support tool to help improve conversations about mental health with parents.")

tab1, tab2, tab3 = st.tabs([
    "👶 Simulation (for Child)",
    "👵 Simulation (for Parent)",
    "💡 Understand What's Happening"
])

# -------------------------
# Tab 1 - Child Sim
# -------------------------
with tab1:
    st.subheader("👶 Talk as the Child (Simulates Your Parent)")

    if "child_chat" not in st.session_state:
        st.session_state.child_chat = []

    for msg in st.session_state.child_chat:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Say something to your parent...")
    if user_input:
        st.session_state.child_chat.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        parent_prompt = f"""
You are roleplaying as a parent responding to their child. Use the following profile to guide your response. A knee jerk reaction is helpful here. Do not be overly logical or analytical, do not overthink it. Just respond as a parent would in the moment.
No being overly nice or sweet or kind. Just be a parent.

Sensitivity: {st.session_state['sensitivity']}/10  
Reactions: {st.session_state['reactions']}  
Tone: {st.session_state['tone']}  

Child says:
\"{user_input}\"

Respond as the parent would:
"""
        parent_response = call_mistral(parent_prompt)
        st.session_state.child_chat.append({"role": "assistant", "content": f"**Parent Response:** {parent_response}"})
        st.chat_message("assistant").write(f"**Parent Response:** {parent_response}")

        reframe_prompt = f"""
Take the following message from a child and rephrase it so it's easier for a sensitive parent to hear and understand. Not in a formal way but in words that might be easier to understand. Make it very casual and just be a child.

Sensitivity: {st.session_state['sensitivity']}/10  
Reactions: {st.session_state['reactions']}  
Tone: {st.session_state['tone']}  

Original message:
\"{user_input}\"

Rephrased for better reception:
"""
        reframed = call_mistral(reframe_prompt)
        st.session_state.child_chat.append({"role": "assistant", "content": f"**Reframed:** {reframed}"})
        st.chat_message("assistant").write(f"**Reframed:** {reframed}")

# -------------------------
# Tab 2 - Parent Sim
# -------------------------
with tab2:
    st.subheader("👵 Talk as the Parent (Simulates the Child)")

    if "parent_chat" not in st.session_state:
        st.session_state.parent_chat = []

    for msg in st.session_state.parent_chat:
        st.chat_message(msg["role"]).write(msg["content"])

    parent_input = st.chat_input("Say something as the parent...")
    if parent_input:
        st.session_state.parent_chat.append({"role": "user", "content": parent_input})
        st.chat_message("user").write(parent_input)

        child_prompt = f"""
You are roleplaying as a child responding to their parent. Here is the child's profile to guide your response. A knee jerk reaction is helpful here. Do not be overly logical or analytical, do not overthink it. Just respond as a child would in the moment.

Sensitivity: {st.session_state['sensitivity']}/10  
Reactions: {st.session_state['reactions']}  
Tone: {st.session_state['tone']}  

Parent says:
\"{parent_input}\"

Respond as the child would:
"""
        child_response = call_mistral(child_prompt)
        st.session_state.parent_chat.append({"role": "assistant", "content": f"**Child Response:** {child_response}"})
        st.chat_message("assistant").write(f"**Child Response:** {child_response}")

        reframe_prompt = f"""
Take the following message from a parent and rephrase it so it's easier for a child to understand and feel emotionally safe hearing.

Sensitivity: {st.session_state['sensitivity']}/10  
Reactions: {st.session_state['reactions']}  
Tone: {st.session_state['tone']}  

Original message:
\"{parent_input}\"

Rephrased version:
"""
        reframed = call_mistral(reframe_prompt)
        st.session_state.parent_chat.append({"role": "assistant", "content": f"**Reframed:** {reframed}"})
        st.chat_message("assistant").write(f"**Reframed:** {reframed}")

# -------------------------
# Tab 3 - Understand Mental Health
# -------------------------
with tab3:
    st.subheader("💡 Ask Anything About Mental Health")

    if "insight_chat" not in st.session_state:
        st.session_state.insight_chat = []

    for msg in st.session_state.insight_chat:
        st.chat_message(msg["role"]).write(msg["content"])

    insight_input = st.chat_input("Ask about communication, mental health, parenting...")
    if insight_input:
        st.session_state.insight_chat.append({"role": "user", "content": insight_input})
        st.chat_message("user").write(insight_input)

        insight_prompt = f"""
You are a mental health expert helping someone understand sensitive emotional topics.

Be logical, compassionate, clear, and avoid jargon.

Question or concern:
\"{insight_input}\"

Respond in a way that feels safe and educational:
"""
        insight_response = call_mistral(insight_prompt)
        st.session_state.insight_chat.append({"role": "assistant", "content": insight_response})
        st.chat_message("assistant").write(insight_response)
