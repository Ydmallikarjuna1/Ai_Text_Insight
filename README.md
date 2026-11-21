# AI Text Insight Studio

A small Streamlit app for exploring text sentiment, frequent keywords, and an extractive summary.

## Requirements

- Python 3.9 or newer
- pip

## Setup on Windows

Open a terminal in this project folder and run:

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run the app

```powershell
streamlit run app.py
```

Streamlit opens the app in your browser. Paste text into the input area and select **Analyze text**.

## What it does

- Estimates sentiment polarity and subjectivity with TextBlob.
- Lists up to five frequent non-stopword keywords.
- Selects up to three salient sentences as an extractive summary.

The results are heuristic estimates, not a substitute for human interpretation.
