"""
Server.py controls routes and starts the Flask server. Additionally
it provides the business logic for the emotion detector.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Returns the index.html
    """
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
    """
    This function calls emotion_detector to detect emotions in text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.pop('dominant_emotion')
    if dominant_emotion is None:
        return "<h3>Invalid Text! Please try again!<h3>"

    response_str = str(response).replace('{','').replace('}','')
    items = response_str.split(", ")
    new_string = ", ".join(items[:-1]) + " and " + items[-1]
    formatted_string = f"For the given statement, the system response is {new_string}. \
The dominant emotion is <b>{dominant_emotion}</b>."
    return formatted_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
