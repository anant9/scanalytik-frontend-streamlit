import streamlit as st

# Page config
st.set_page_config(page_title="Scanalytik", page_icon="📊", layout="wide")

# Load CSS from external file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Top Nav Bar ---
st.markdown("""
    <div class="navbar">
        <div class="navbar-left">🤖 Scanalytik</div>
        <div class="navbar-right">
            <a href="#">How It Works</a>
            <a href="#">Features</a>
            <a href="#">Pricing</a>
            <button class="google-btn">Login with Google</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero-section">
        <h2>🚀 Get Started - Login with Google</h2>
        <p class="subtitle">Free forever • No credit card required</p>
    </div>
""", unsafe_allow_html=True)

# --- Popular Queries ---
st.markdown("### Try these popular searches:")

col1, col2 = st.columns(2)

with col1:
    st.button("Show me Nifty 50 stocks up 2% today")
    st.button("Banking stocks hitting 52-week high")

with col2:
    st.button("Find IT stocks with high volume")
    st.button("Stocks down more than 3% this week")

# --- User Input ---
st.markdown("""
<div class="input-section">
    <p>💬 Or type your own query: <i>'Show me stocks up 2% in last 10 minutes'</i></p>
</div>
""", unsafe_allow_html=True)

user_query = st.text_input(
    label="Type your query",
    label_visibility="collapsed",
    placeholder="Show me stocks up 2% in last 10 minutes"
)
# --- Scan Button ---
st.markdown("<br>", unsafe_allow_html=True)

if st.button("▶️  Scan for Free", key="scan_btn"):
    st.success(f"Running query: {user_query}")
