import altair as alt
import pandas as pd
import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from utils import load_css, sentiment_badge

load_css()
st.title("🇬🇧 English Sentiment Analysis")
st.caption("TextBlob + VADER | mengikuti pendekatan pada modul praktikum")


def convert_to_df(sentiment):
    sentiment_dict = {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
    }
    return pd.DataFrame(sentiment_dict.items(), columns=["metric", "value"])


def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []

    for token in docx.split():
        score = analyzer.polarity_scores(token)["compound"]

        if score > 0.1:
            pos_list.append({"token": token, "score": score, "sentiment": "Positive"})
        elif score <= -0.1:
            neg_list.append({"token": token, "score": score, "sentiment": "Negative"})
        else:
            neu_list.append({"token": token, "score": score, "sentiment": "Neutral"})

    return pos_list, neg_list, neu_list

example = "I really love this movie. The story is amazing and the actors are great."
text = st.text_area(
    "Enter English text",
    value=example,
    height=150,
    placeholder="Type an English sentence here...",
)

if st.button("Analyze Sentiment", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Menganalisis sentimen..."):
            sentiment = TextBlob(text).sentiment
            polarity = sentiment.polarity
            subjectivity = sentiment.subjectivity

            if polarity > 0:
                label, emoji = "Positive", "😊"
            elif polarity < 0:
                label, emoji = "Negative", "😠"
            else:
                label, emoji = "Neutral", "😐"

            left, right = st.columns([0.9, 1.1])

            with left:
                sentiment_badge(label, emoji)
                st.write("")
                metric1, metric2 = st.columns(2)
                with metric1:
                    st.metric("Polarity", f"{polarity:.3f}")
                with metric2:
                    st.metric("Subjectivity", f"{subjectivity:.3f}")

            with right:
                st.markdown("### Polarity & Subjectivity")
                result_df = convert_to_df(sentiment)
                chart = (
                    alt.Chart(result_df)
                    .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
                    .encode(
                        x=alt.X("metric:N", title=None),
                        y=alt.Y("value:Q", title="Score", scale=alt.Scale(domain=[-1, 1])),
                        tooltip=["metric", alt.Tooltip("value:Q", format=".3f")],
                    )
                    .properties(height=280)
                )
                st.altair_chart(chart, use_container_width=True)

            st.divider()
            st.markdown("### Token Sentiment (VADER)")
            pos_list, neg_list, neu_list = analyze_token_sentiment(text)

            token_col1, token_col2, token_col3 = st.columns(3)
            with token_col1:
                st.metric("Positive tokens", len(pos_list))
                if pos_list:
                    st.dataframe(pd.DataFrame(pos_list), use_container_width=True, hide_index=True)
                else:
                    st.caption("No positive token detected.")

            with token_col2:
                st.metric("Negative tokens", len(neg_list))
                if neg_list:
                    st.dataframe(pd.DataFrame(neg_list), use_container_width=True, hide_index=True)
                else:
                    st.caption("No negative token detected.")

            with token_col3:
                st.metric("Neutral tokens", len(neu_list))
                if neu_list:
                    st.dataframe(pd.DataFrame(neu_list), use_container_width=True, hide_index=True)
                else:
                    st.caption("No neutral token detected.")

with st.expander("About this page"):
    st.write(
        "TextBlob digunakan untuk mendapatkan polarity dan subjectivity. "
        "VADER digunakan untuk membaca compound score pada token. "
        "Pada pendekatan modul, polarity > 0 dikategorikan Positive, polarity < 0 Negative, "
        "dan polarity = 0 Neutral."
    )
