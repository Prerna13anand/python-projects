# Sentiment Analysis Web App

This is a simple web application for performing sentiment analysis on user input using Flask and TextBlob.

## Features
- Enter a sentence and analyze its sentiment (Positive, Negative, Neutral)
- Displays polarity and subjectivity scores
- Clean and responsive **glassmorphism interface** for better user experience.

## 🖥️ Tech Stack

- Python
- Flask
- TextBlob (NLP Library)
- HTML5 + CSS3 (Glass UI)


## Setup Instructions

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Download TextBlob corpora (first time only)**

   ```bash
   python -m textblob.download_corpora
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. **Open your browser and go to** [http://localhost:5000](http://localhost:5000)

## File Structure
- `app.py`: Flask backend
- `templates/index.html`: Frontend HTML
- `requirements.txt`: Python dependencies
- `README.md`: This file