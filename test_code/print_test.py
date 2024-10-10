import re
def detect_emotion():

    response = {"anger":0.06, "disgust":0.002,"fear":0.24,"joy":0.46,"dominant_emotion":"joy"}
    
    dominant_emotion = response.pop('dominant_emotion')  
    response_str = str(response).replace('{','').replace('}','')
    items = response_str.split(", ")
    new_string = ", ".join(items[:-1]) + " and " + items[-1]
    print(f"For the given statement, the system response is {new_string}. The dominant emotion is {dominant_emotion}.") 

if __name__ == "__main__":
    detect_emotion()
