import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        # Return a dictionary with None values for all emotions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # URL of the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Create the input payload (JSON format)
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to the API
    response = requests.post(url, headers=headers, json=input_data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract emotions from the response
        emotions = response.json()
        # Return the emotions dictionary with dominant emotion included
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        # If the API request fails, return None for all emotions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
