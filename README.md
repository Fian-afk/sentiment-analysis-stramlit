# Sentiment Analysis Streamlit

NLP website for:
- English Sentiment Analysis with TextBlob + VADER
- Indonesian Sentiment Analysis with Indonesian RoBERTa Sentiment Classifier

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

For Windows PowerShell, if the execution policy prevents venv from being activated, use the Command Prompt or run `\.venv\Scripts\python.exe -m pip install -r requirements.txt` and then `\.venv\Scripts\python.exe -m streamlit run app.py`.

## Structure

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
