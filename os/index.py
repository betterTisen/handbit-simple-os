from mpython import *
import time

from os.globle import GlobleController

def step():
    oled.fill(0)
    oled.DispChar(str(time.localtime()[0]), 0, 0, 1)
    oled.DispChar("wifi断开", 0*16, 3*16, 1)
    oled.DispChar("按A连接wifi", 4*16, 3*16, 1)
    oled.show()
    pass

