import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="For You 💙", layout="centered")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------------- BACKGROUND & STYLE ----------------
st.markdown(
    """
    <style>
    html, body {
        background: transparent;
    }

    .stApp {
        background: transparent;
    }

    [data-testid="stAppViewContainer"] {
        background-image:
        linear-gradient(
            rgba(255, 250, 205, 0.88),
            rgba(255, 250, 205, 0.88)
        ),
        url("https://images.unsplash.com/photo-1470509037663-253afd7f0f51");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    h1, h2, p {
        text-align: center;
        color: #4a3b1f;
        font-family: "Segoe UI", sans-serif;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- CARD HELPER ----------------
def card(content):
    st.markdown(
        f"""
        <div style="
            background-color: rgba(255,255,255,0.9);
            padding: 30px;
            border-radius: 20px;
            margin: 30px auto;
            max-width: 620px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.1);
        ">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- PROGRESS BAR ----------------
progress_map = {
    0: 5, 1: 15, 2: 30, 3: 45,
    4: 60, 5: 75, 6: 90, 7: 100
}
st.progress(progress_map.get(st.session_state.step, 0))

# ---------------- STEP 0 ----------------
if st.session_state.step == 0:
    card("""
    <h1>Good morning, my chick 🐣</h1>
    <p>
    I made this little space just for you.<br>
    Take your time — I’m right here 💙
    </p>
    """)
    if st.button("Start", use_container_width=True):
        st.session_state.step = 1

# ---------------- STEP 1 ----------------
elif st.session_state.step == 1:
    card("<h2>How are you feeling today?</h2>")
    if st.button("Better 🙂", use_container_width=True):
        st.session_state.step = 2
    if st.button("A little tired 😌", use_container_width=True):
        st.session_state.step = 2
    if st.button("Missing you 💙", use_container_width=True):
        st.session_state.step = 2

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    card("<h2>What helps you feel better?</h2>")
    if st.button("Rest 🛌", use_container_width=True):
        st.session_state.step = 3
    if st.button("Medicine 💊", use_container_width=True):
        st.session_state.step = 3
    if st.button("Thinking of you 💕", use_container_width=True):
        st.session_state.step = 3

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    card("<h2>Do you miss me?</h2>")
    col1, col2 = st.columns(2)
    if col1.button("Yes 💙"):
        st.session_state.step = 4
    if col2.button("No"):
        st.session_state.step = 99

# ---------------- GAME OVER ----------------
elif st.session_state.step == 99:
    card("<h2>Wrong answer 😌</h2><p>Try again.</p>")
    if st.button("Restart", use_container_width=True):
        st.session_state.step = 0

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    card("<h2>What do you want most from me right now?</h2>")
    if st.button("A kiss 😘", use_container_width=True):
        st.session_state.step = 5
    if st.button("A cuddle 🤍", use_container_width=True):
        st.session_state.step = 5
    if st.button("Just you here 💙", use_container_width=True):
        st.session_state.step = 5

# ---------------- STEP 5 ----------------
elif st.session_state.step == 5:
    card("<h2>Do I make your days better?</h2>")
    if st.button("Always 💕", use_container_width=True):
        st.session_state.step = 6
    if st.button("Yes 😊", use_container_width=True):
        st.session_state.step = 6
    if st.button("More than you know 💙", use_container_width=True):
        st.session_state.step = 6

# ---------------- STEP 6 ----------------
elif st.session_state.step == 6:
    card("<h2>How many kisses do I get?</h2>")
    if st.button("1 💋", use_container_width=True):
        st.session_state.step = 7
    if st.button("5 💋💋💋💋💋", use_container_width=True):
        st.session_state.step = 7
    if st.button("10 😍", use_container_width=True):
        st.session_state.step = 7
    if st.button("Unlimited ❤️", use_container_width=True):
        st.session_state.step = 7

# ---------------- STEP 7 ----------------
elif st.session_state.step == 7:
    card("<h2>🎅 Your Santa wish this year</h2><p>Write it from your heart ✍️</p>")
    wish = st.text_input("Your wish")
    if st.button("Save my wish", use_container_width=True):
        st.session_state.answers["Santa"] = wish
        st.session_state.step = 8

# ---------------- FINAL ----------------
elif st.session_state.step == 8:
    st.balloons()
    card(f"""
    <h1>My favourite person</h1>

    <p>
    I know you haven’t been feeling well,<br>
    yet you still came to see me.
    </p>

    <p>
    That meant more to me than I can say.
    </p>

    <p>
    Please rest, take care of yourself,<br>
    and remember you are deeply appreciated.
    </p>

    <p>
    <b>Get well soon.</b><br>
    I’m always here for you 💙
    </p>

    <p>
    🎅 Your wish:<br>
    <b>{st.session_state.answers.get("Santa", "")}</b>
    </p>
    """)
