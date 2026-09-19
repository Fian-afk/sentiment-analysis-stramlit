import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero-card {
            padding: 2rem;
            border: 1px solid rgba(128, 128, 128, 0.20);
            border-radius: 24px;
            margin: 1.2rem 0 2rem 0;
            background: linear-gradient(135deg, rgba(91, 33, 182, 0.10), rgba(59, 130, 246, 0.07));
        }

        .hero-badge {
            display: inline-block;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            border: 1px solid rgba(128, 128, 128, 0.25);
        }

        .hero-card h2 {
            margin-top: 0.9rem;
            margin-bottom: 0.5rem;
            font-size: 2.1rem;
        }

        .hero-card p {
            font-size: 1.05rem;
            opacity: 0.8;
            margin-bottom: 0;
        }

        .result-card {
            padding: 1.25rem;
            border: 1px solid rgba(128, 128, 128, 0.18);
            border-radius: 18px;
            background: rgba(128, 128, 128, 0.04);
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(128, 128, 128, 0.18);
            padding: 1rem;
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def sentiment_badge(label: str, emoji: str):
    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size: 0.82rem; opacity: 0.7;">SENTIMENT</div>
            <div style="font-size: 2rem; font-weight: 750; margin-top: 0.3rem;">{emoji} {label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
