from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    user_text = ''
    if request.method == 'POST':
        user_text = request.form['text']
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity, user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)