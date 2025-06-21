import os
from dotenv import load_dotenv
import streamlit as st
import requests
import urllib.parse

# Config
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
print(f"Using backend URL: {BACKEND_URL}")

# Title
st.title("📊 Scanalytik MVP — LLM Stock Screener")

# --- Section: Google Login ---

if "jwt_token" not in st.session_state:
    st.session_state.jwt_token = None

if st.session_state.jwt_token:
    st.success("✅ Logged in!")
    st.write("You can now run queries below 👇")

else:
    st.info("🔐 Please login with Google first.")
    login_url = f"{BACKEND_URL}/login"
    if st.button("Login with Google"):
        st.write("Click below link if not redirected:")
        st.markdown(f"[Login with Google]({login_url})", unsafe_allow_html=True)

# --- Handle token from URL (when redirected) ---
query_params = st.query_params
if "token" in query_params:
    st.session_state.jwt_token = query_params["token"]
    st.query_params.clear()  # clean URL
    st.rerun()

# --- Section: LLM Query ---
if st.session_state.jwt_token:
    user_query = st.text_input("📥 Enter your query:", "Show top 5 stocks where revenue increased")

    if st.button("Run Query"):
        try:
            response = requests.post(
                f"{BACKEND_URL}/query",
                json={"prompt": user_query},
                headers={"Authorization": f"Bearer {st.session_state.jwt_token}"}
            )

            if response.status_code == 200:
                res = response.json()

                # Show natural language explanation
                st.write("### ℹ️ What this query is doing:")
                st.info(res.get("summary", "No summary provided."))

                # Show result table
                if "result" in res:
                    st.write("### 📊 Result:")
                    st.dataframe(res["result"])
                elif "error" in res:
                    st.error(f"Error running query: {res['error']}")

            else:
                st.error(f"Error: {response.status_code} {response.text}")

        except Exception as e:
            st.error(f"Exception: {e}")
