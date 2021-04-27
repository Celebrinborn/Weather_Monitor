import os
import logging
import sys
logging.basicConfig(
    level=logging.INFO,
    #format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(os.path.join('logs', 'weather.log')), logging.StreamHandler()])
logging.info('configured logging')

import time
import functions
from playsound import playsound

#get secrets
if os.path.exists('my_secrets.py'):
    import my_secrets
    os.environ['api_key'] = my_secrets.apikey

#get the weather
forcast = functions.GetWeather(logging)
if not isinstance(forcast, str):
    logging.critical('forcast is not a string')
    sys.exit(1)

# convert the forcast to an mp3
functions.CreateMp3(logging, forcast)

# Play the converted file
logging.info('playing mp3')

playsound(os.path.join('output','current_weather.mp3'))