from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    resp_anger = response["anger"]
    resp_disgust = response["disgust"]
    resp_fear = response["fear"]
    resp_joy = response["joy"]
    resp_sadness = response["sadness"]
    resp_dominant = response["dominant_emotion"]

    response_str = (
    "For the given statement, the system response is:\n"
    f" - Anger: {resp_anger}\n"
    f" - Disgust: {resp_disgust}\n"
    f" - Fear: {resp_fear}\n"
    f" - Joy: {resp_joy}\n"
    f" - Sadness: {resp_sadness}\n"
    f"The dominant emotion is: {resp_dominant}."
    )

    return response_str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)