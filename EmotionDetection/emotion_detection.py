import requests
import json

NULL_RESULT = {
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion': None
}

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze or ""}}

    try:
        response = requests.post(url, json=payload, headers=header)

        # Requirement: use status_code to handle blank entries
        if response.status_code == 400:
            return NULL_RESULT

        # Any other unexpected non-200 → treat as error/None
        if response.status_code != 200:
            return NULL_RESULT

        formatted = json.loads(response.text)
        emotions = formatted['emotionPredictions'][0]['emotion']

        dominant = max(emotions, key=emotions.get)

        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant
        }

    except Exception:
        # Network/JSON/Key errors → return None payload as per spec
        return NULL_RESULT
