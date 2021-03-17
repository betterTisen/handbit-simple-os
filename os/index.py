from mpython import *
import time

from globle import GlobleController
from common.touch_input import TouchInputController

oled.DispChar(time.localtime()[0], 0, 0, 1)

oled.DispChar("wifi未连接", 2*16, 3*16, 1)
oled.show()


