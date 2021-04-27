import os
import sys
import requests
from gtts import gTTS
if __name__ == "__main__":
    import os
    print("don't be a dumbass")
    sys.exit(1)


def GetWeather(logging):
    query = f"https://api.openweathermap.org/data/2.5/weather?q=Quincy,WA,USA&appid={os.environ['api_key']}&units=imperial"
    response = requests.get(query)
    logging.info(response.status_code)
    if response.status_code != 200:
        logging.error('status code was NOT 200')
        logging.error(query.replace(os.environ['api_key'], '{secret}')) #remove secret before logging
        return 1

    data = response.json()
    logging.info(str(data))

    weather = f"Good morning Cameron. The weather is currently {data['weather'][0]['description']} and it feels like {data['main']['feels_like']} degrees"
    logging.info(weather)
    return weather



def CreateMp3(logging, script):
    # Language in which you want to convert
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=script, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    path = os.path.join('output', "current_weather.mp3")
    logging.info(f'saving mp3 at {path}')
    myobj.save(path)