# Sentiment Analysis Streamlit

Website praktikum NLP untuk:
- English Sentiment Analysis dengan TextBlob + VADER
- Indonesian Sentiment Analysis dengan Indonesian RoBERTa Sentiment Classifier

## Jalankan

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Untuk Windows PowerShell jika execution policy menghalangi aktivasi venv, gunakan terminal Command Prompt atau jalankan `\.venv\Scripts\python.exe -m pip install -r requirements.txt` lalu `\.venv\Scripts\python.exe -m streamlit run app.py`.

## Struktur

```text
sentiment_analysis_streamlit/
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── pages/
    ├── 1_English_Sentiment.py
    └── 2_Indonesian_Sentiment.py
```
