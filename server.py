from flask import Flask, request, jsonify
from emotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    # Get the text to analyze from the URL query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided to analyze"}), 400

    # Call the emotion detector function
    emotion_result = emotion_detector(text_to_analyze)

    # If dominant emotion is None, return the error message
    if emotion_result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    # Format the output as required by the customer
    response = {
        "anger": emotion_result['anger'],
        "disgust": emotion_result['disgust'],
        "fear": emotion_result['fear'],
        "joy": emotion_result['joy'],
        "sadness": emotion_result['sadness'],
        "dominant_emotion": emotion_result['dominant_emotion']
    }
    
    # Return the result as a JSON response
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
