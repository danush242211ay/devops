import streamlit as st

# Page settings
st.set_page_config(page_title="Microdegree Registration", page_icon="🎓", layout="centered")

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #eef2ff, #f8f9ff);
}
.title {
    text-align: center;
    color: #4B0082;
    font-size: 48px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
}
.stButton>button {
    background: linear-gradient(90deg, #4B0082, #6A0DAD);
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='title'>🎓 Microdegree Organization</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Register today and unlock exciting real-world projects 🚀</div>", unsafe_allow_html=True)

st.write("")

# Registration form
with st.form("registration_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    phone = st.text_input("📱 Phone Number")
    college = st.text_input("🏫 College Name")
    course = st.selectbox("📘 Choose Course", ["Python", "Web Development", "Data Science", "AI & ML"])

    submitted = st.form_submit_button("🚀 Register Now")

# After submit
if submitted:
    if name and email and phone and college:
        st.balloons()

        st.success("🎉 Registration Successful!")

        st.markdown(f"""
        # 🎉 Welcome {name}!

        ## 🚀 You have unlocked some exciting projects!

        ### Start learning from these videos 👇
        """)

        # Video links
        st.markdown("### 📺 1. Python Full Course")
        st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")

        st.markdown("### 📺 2. Streamlit Tutorial")
        st.video("https://www.youtube.com/watch?v=example")

        st.markdown("### 📺 3. Build a Streamlit App")
        st.video("https://www.youtube.com/watch?v=example")

        st.info("🎯 Watch these videos and start building amazing real-world projects!")

        st.markdown("---")
        st.markdown("### 💜 Happy Learning!")

    else:
        st.error("⚠️ Please fill all the fields before submitting.")