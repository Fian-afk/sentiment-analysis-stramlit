import pandas as pd
import streamlit as st
from transformers import pipeline

from utils import load_css, sentiment_badge

load_css()
st.title("🇮🇩 Indonesian Sentiment Analysis")
st.caption("Indonesian RoBERTa Sentiment Classifier")

MODEL_NAME = "w11wo/indonesian-roberta-base-sentiment-classifier"


@st.cache_resource(show_spinner="Loading Indonesian sentiment model...")
def load_model():
    return pipeline(
        "sentiment-analysis",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
    )


label_map = {
    "positive": ("Positive", "😊"),
    "negative": ("Negative", "😠"),
    "neutral": ("Neutral", "😐"),
}

example = "Pelayanannya sangat bagus dan makanannya enak."
text = st.text_area(
    "Masukkan teks Bahasa Indonesia",
    value=example,
    height=150,
    placeholder="Tulis kalimat Bahasa Indonesia di sini...",
)

st.info("Model pertama kali dijalankan akan membutuhkan waktu karena bobot model perlu diunduh.")

if st.button("Analisis Sentimen", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        try:
            with st.spinner("Menganalisis sentimen..."):
                classifier = load_model()
                result = classifier(text, truncation=True)[0]

                raw_label = result["label"].lower()
                score = float(result["score"])
                label, emoji = label_map.get(raw_label, (result["label"], "🔎"))

                left, right = st.columns([0.9, 1.1])

                with left:
                    sentiment_badge(label, emoji)
                    st.write("")
                    st.metric("Confidence", f"{score:.2%}")

                with right:
                    st.markdown("### Prediction")
                    st.progress(score)
                    st.write(f"**Label model:** `{result['label']}`")
                    st.write(f"**Confidence:** `{score:.4f}`")

                st.divider()
                st.markdown("### Input")
                st.code(text, language="text")

                result_df = pd.DataFrame(
                    [{
                        "text": text,
                        "label": label,
                        "confidence": score,
                    }]
                )
                st.markdown("### Result Table")
                st.dataframe(result_df, use_container_width=True, hide_index=True)

        except Exception as exc:
            st.error("Model gagal dijalankan.")
            st.exception(exc)

with st.expander("About this model"):
    st.write(
        "Model ini adalah Indonesian RoBERTa Base Sentiment Classifier yang di-fine-tune "
        "pada dataset SmSA untuk komentar dan ulasan Bahasa Indonesia. "
        "Hasil prediksi model sebaiknya tetap dipahami sebagai klasifikasi berbasis data pelatihan model."
    )
