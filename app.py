import streamlit as st
from utils import load_css

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

def home_page():
    load_css()
    
    st.sidebar.markdown("## 💬 Sentiment Lab")
    st.sidebar.caption("Praktikum Natural Language Processing")
    st.sidebar.divider()
    
    st.title("Sentiment Analysis")
    st.markdown(
        "Analisis sentimen sederhana untuk teks **Bahasa Inggris** dan **Bahasa Indonesia**."
    )
    
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-badge">NLP PRAKTIKUM</div>
            <h2>Understand what a text feels like.</h2>
            <p>Masukkan teks, jalankan analisis, lalu lihat hasil sentimen dan skor model.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🇬🇧 English Sentiment")
        st.write("Menggunakan TextBlob untuk polarity & subjectivity serta VADER untuk token sentiment.")
        st.page_link(english_page, label="Open English Analysis →", icon="🇬🇧")
    
    with col2:
        st.markdown("### 🇮🇩 Indonesian Sentiment")
        st.write("Menggunakan Indonesian RoBERTa Sentiment Classifier untuk klasifikasi teks Indonesia.")
        st.page_link(indo_page, label="Open Indonesian Analysis →", icon="🇮🇩")
    
    st.divider()
    
    st.markdown("### Alur Aplikasi")
    step1, step2, step3, step4 = st.columns(4)
    for i, (col, title, desc) in enumerate(
        [
            (step1, "1. Input", "Masukkan teks"),
            (step2, "2. Process", "Model menganalisis teks"),
            (step3, "3. Classify", "Sentimen ditentukan"),
            (step4, "4. Result", "Hasil dan skor ditampilkan"),
        ]
    ):
        with col:
            st.markdown(f"**{title}**")
            st.caption(desc)
    
    st.info("Gunakan menu pada sidebar untuk mencoba kedua analisis.")


home = st.Page(home_page, title="Home", icon="🏠", default=True)
english_page = st.Page("pages/1_English_Sentiment.py", title="English Sentiment", icon="🇬🇧")
indo_page = st.Page("pages/2_Indonesian_Sentiment.py", title="Indonesian Sentiment", icon="🇮🇩")

pg = st.navigation([home, english_page, indo_page])
pg.run()
