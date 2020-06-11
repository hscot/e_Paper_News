#!/usr/bin/python
import sys
sys.path.append(r'lib')
import signal
import epd2in13_V2
import epdconfig
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from newsapi import NewsApiClient
import json
import requests



#Initializes API
api = NewsApiClient(api_key='Your-API-Key-Here')

top_headlines = api.get_top_headlines(sources='die-zeit', language='de')

#Checks if Python3+ is being used.
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3.0 or greater!")

#Main function

def main():
    y = json.dumps(top_headlines)
    x = json.loads(y)
    source_name = x['articles'][0]['source']['name']
    source_string = "Source: " + source_name
    epd = epd2in13_V2.EPD()
    while True:
        try:
            print("Clearing EPD")
            epd.init(epd.FULL_UPDATE)
            epd.Clear(0xFF)
            HBlackimage = Image.new('1', (epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), 255)

            print("Drawing information to EPD")
            drawblack = ImageDraw.Draw(HBlackimage)
            font20 = ImageFont.truetype('fonts/arial.ttf', 20)
            font10 = ImageFont.truetype('fonts/arial.ttf', 10)

            n_image = Image.new('1', (epd.height, epd.width), 255)
            n_image_draw = ImageDraw.Draw(image)

            epd.init(epd.FULL_UPDATE)
            epd.displayPartBaseImage(epd.getbuffer(n_image))
            epd.init(epd.PART_UPDATE)

            n_image_draw.text((0, 10), source_string, font = font10, fill = 0)
            
            #Begin displaying top 5 headlines

            articles = top_headlines['articles']
            results = []
            for ar in articles:
                results.append(ar['title'])
            for i in range(0, 5):
                n_image_draw.text((0, (35 + (i * 15))), (str(i + 1) + "." + results[i]), font = font10, fill = 0)
            #Displays current time
            while(True):
                n_image_draw.rectangle((180, 0, 250, 30), fill = 255)
                n_image_draw.text((180, 0), time.strftime('%H:%M'), font = font20, fill = 0)
                epd.displayPartial(epd.getbuffer(n_image))

        except IOError as e:
            print('traceback.format_exec():\n%s', traceback.format_exc())
            epdconfig.module_init()
            epdconfig.module_exit()
            exit()
        time.sleep(60)

def ctrl_c_handler(signal, frame):
    print("Crtl-C Pressed. Exiting!")
    epdconfig.module_init()
    epdconfig.module_exit()
    exit(0)

    signal.signal(signal.SIGINT, ctrl_c_handler)

if __name__ == '__main__':
    main()

