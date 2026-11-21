# AI Text Insight Studio — Project Report

## Overview

AI Text Insight Studio is a lightweight text-analysis app built with Streamlit. It accepts user-provided text and displays an estimated sentiment, frequent keywords, and an extractive summary.

## Tools and methods

- **Streamlit** provides the interactive web interface.
- **TextBlob** calculates sentiment polarity (from -1 to 1) and subjectivity (from 0 to 1).
- **Python regular expressions and `Counter`** identify frequent words and score sentences, excluding a small built-in stopword list.
- **pandas** formats the keyword counts as a table.

The summary selects up to three sentences with the highest frequency-based scores and retains their original order.

## Limitations

The analysis is heuristic. The fixed stopword list is intentionally small, sentiment may not capture sarcasm or context, and the extractive summary does not generate new wording. Results should be interpreted as a quick overview rather than a definitive assessment.

## Run

Create and activate a virtual environment, install dependencies from `requirements.txt`, and run `streamlit run app.py`. See [README.md](README.md) for Windows setup commands.
