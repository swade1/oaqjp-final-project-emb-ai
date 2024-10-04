from flask import Flask, request, url_for, redirect, render_template
from EmotionDetection.emotion_detection import emotion_detector 

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route('/emotionDetection')
def detect_emotion(): 
    textToAnalyze = request.args.get('textToAnalyze')
    return emotion_detector(textToAnalyze)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
