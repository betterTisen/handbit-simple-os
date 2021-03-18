from mpython import *
from machine import Timer
import time

from micro_os.globle import globleController
from micro_os.utils.button_input import btnInputController


class WifiTouchControllerCls:
    is_input_id = True  # 判断第几行数据
    line1_text = ""
    line2_text = ""
    write_idx = 0
    str_high = False  # 大小写
    mod_type = "str"  # str,num,symb

    str_mod = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    num_mod = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    symb_mod = ["_", "+", "-", "*", "/", "=", "?", ",", ".", "'", "\"", ":",
                ";", "!", "@", "#", "$", "%", "^", "&", "(", ")", "[", "]", "{", "}"]

    def __init__(self):
        pass

    def output_text(self):
        if self.mod_type == "str":
            if self.str_high:
                return self.str_mod[self.write_idx].upper()
            else:
                return self.str_mod[self.write_idx]

        elif self.mod_type == "num":
            return self.num_mod[self.write_idx]

        elif self.mod_type == "symb":
            return self.symb_mod[self.write_idx]
        pass


wifiTouchController = WifiTouchControllerCls()

touch_threshold = {'P': 400, 'Y': 400,
                   'T': 400, 'H': 400, 'O': 400, 'N': 400}
_status_p = _status_y = _status_t = _status_h = _status_o = _status_n = 0

tim12 = Timer(12)


def on_touchpad_P_pressed():
    global wifiTouchController
    if wifiTouchController.is_input_id:
        wifiTouchController.line1_text = wifiTouchController.line1_text[:-1]
    else:
        wifiTouchController.line2_text += wifiTouchController.line2_text[:-1]
    pass


def on_touchpad_Y_pressed():
    global wifiTouchController
    if wifiTouchController.mod_type == "str":
        wifiTouchController.write_idx += 1
        return
    wifiTouchController.write_idx = 0
    wifiTouchController.mod_type = "str"
    pass


def on_touchpad_T_pressed():
    global wifiTouchController
    if wifiTouchController.mod_type == "num":
        wifiTouchController.write_idx += 1
        return
    wifiTouchController.write_idx = 0
    wifiTouchController.mod_type = "num"
    pass


def on_touchpad_H_pressed():
    global wifiTouchController
    if wifiTouchController.mod_type == "symb":
        wifiTouchController.write_idx += 1
        return
    wifiTouchController.write_idx = 0
    wifiTouchController.mod_type = "symb"
    pass


def on_touchpad_O_pressed():
    global wifiTouchController
    wifiTouchController.str_high = not wifiTouchController.str_high
    pass


def on_touchpad_N_pressed():
    global wifiTouchController
    if wifiTouchController.is_input_id:
        wifiTouchController.line1_text += wifiTouchController.output_text()
    else:
        wifiTouchController.line2_text += wifiTouchController.output_text()
    wifiTouchController.write_idx = 0
    pass


def timer12_tick(_):
    global _status_p, _status_y, _status_t, _status_h, _status_o, _status_n
    try:
        touchPad_P.read()
        pass
    except:
        return
    if touchPad_P.read() < touch_threshold['P']:
        if 1 != _status_p:
            _status_p = 1
            on_touchpad_P_pressed()
        elif 0 != _status_p:
            _status_p = 0

    if touchPad_Y.read() < touch_threshold['Y']:
        if 1 != _status_y:
            _status_y = 1
            on_touchpad_Y_pressed()
        elif 0 != _status_y:
            _status_y = 0

    if touchPad_T.read() < touch_threshold['T']:
        if 1 != _status_t:
            _status_t = 1
            on_touchpad_T_pressed()
        elif 0 != _status_t:
            _status_t = 0

    if touchPad_H.read() < touch_threshold['H']:
        if 1 != _status_h:
            _status_h = 1
            on_touchpad_H_pressed()
        elif 0 != _status_h:
            _status_h = 0

    if touchPad_O.read() < touch_threshold['O']:
        if 1 != _status_o:
            _status_o = 1
            on_touchpad_O_pressed()
        elif 0 != _status_o:
            _status_o = 0

    if touchPad_N.read() < touch_threshold['N']:
        if 1 != _status_n:
            _status_n = 1
            on_touchpad_N_pressed()
        elif 0 != _status_n:
            _status_n = 0


tim12.init(period=100, mode=Timer.PERIODIC, callback=timer12_tick)

route_idx = "/connect-wifi"


def route(_):
    globleController.route = route_idx    # 当前路由
    globleController.pre_route = "/"    # 上级路由
    # 捕获A、B按钮
    if btnInputController.a_state:
        btnInputController.a_state = False

        if wifiTouchController.is_input_id:
            wifiTouchController.is_input_id = False
            return

        globleController.route = "/connect-wifi"
        return
    if btnInputController.b_state:
        btnInputController.b_state = False
        globleController.route = globleController.pre_route
        return
    pass


def step(_):
    time_str = "id:"
    time2_str = "pwd:"
    oled.fill(0)
    oled.DispChar(time_str, 0, 0, 1)
    oled.DispChar(time2_str, 0, 16, 1)
    oled.DispChar("按A连接", 0*16, 3*16, 1)
    oled.DispChar("按B返回", 5*16, 3*16, 1)

    oled.DispChar(wifiTouchController.line1_text, 24, 0, 1)
    oled.DispChar(wifiTouchController.line2_text, 2*16, 16, 1)
    if wifiTouchController.is_input_id:
        oled.DispChar(wifiTouchController.output_text(), 24 +
                      len(wifiTouchController.line1_text)*8, 0, 2)
    else:
        oled.DispChar(wifiTouchController.output_text(), 32 +
                      len(wifiTouchController.line2_text)*8, 16, 2)
    oled.show()
    pass
