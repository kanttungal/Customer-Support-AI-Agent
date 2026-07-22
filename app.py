import uuid
import requests
import streamlit as st

st.set_page_config(
    page_title="Customer Support AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Support AI Agent")
st.caption("Industry Level Multi-Agent Customer Support System")

# ===============================
# Session State Initialization
# ===============================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# ===============================
# Display Previous Messages
# ===============================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===============================
# Chat Input
# ===============================

query = st.chat_input("Ask your question here...")

if query:

    # -----------------------------
    # Display User Message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    # -----------------------------
    # Call FastAPI
    # -----------------------------

    try:

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "query": query,
                "session_id": st.session_state.session_id
            },
            timeout=60
        )

        if response.status_code == 200:

            data = response.json()

            answer = data.get("answer", "No response received.")

            # Update session id if returned
            if data.get("session_id"):
                st.session_state.session_id = data["session_id"]

        else:

            answer = (
                f"❌ API Error\n\n"
                f"Status Code: {response.status_code}\n\n"
                f"{response.text}"
            )

    except requests.exceptions.ConnectionError:

        answer = (
            "❌ Could not connect to FastAPI.\n\n"
            "Start FastAPI first:\n\n"
            "uvicorn api.main:api --reload"
        )

    except Exception as e:

        answer = f"❌ Error:\n\n{str(e)}"

    # -----------------------------
    # Display Assistant Response
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)