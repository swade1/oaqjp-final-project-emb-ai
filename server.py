from flask import Flask, request, url_for, redirect, render_template
from EmotionDetection.emotion_detection import emotion_detector 

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    max_emotion = max(emotion_result, key=emotion_result.get)
    items = [f"'{k}': {v}" for k, v in emotion_result.items()]
    res = ', '.join(items[:-1]) + f", and {items[-1]}"
    statement = f"For the given statement, the system response is {res}. The dominant emotion is {max_emotion}."
    return statement

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
