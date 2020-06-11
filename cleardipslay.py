import sys
sys.path.append(r'lib')

import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    print("Clear...")
    epd.Clear(0xFF)
    
    epd.sleep()
        
except :
    print ('traceback.format_exc():\n%s',traceback.format_exc())
    exit()