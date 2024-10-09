import requests

def emotion_detector(text_to_analyze):
    print("text to analyze is: {text_to_analyze}")
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    response_json_subset = formatted_response['emotionPredictions'][0]['emotion']
  
    dominant_emotion = max(response_json_subset, key=response_json_subset.get)
    response_json_subset['dominant_emotion'] = dominant_emotion
    
    print("{")
    json_items = list(response_json_subset.items())
    for i, (key, value) in enumerate(json_items):
    if i == len(json_items) - 1:
        print(f"'{key}': {value}")
    else:
        print(f"'{key}': {value},")
    print("}")

    #return response_json_subset
