from machine import Timer
from mpython import *
import threading


class TouchInputController:
    input_type = 1        # 1:普通模式。2:输入模式
    input_up = False      # 是否大写

    touch_threshold = {'P': 400, 'Y': 400,
                       'T': 400, 'H': 400, 'O': 400, 'N': 400}
    _status_p = _status_y = _status_t = _status_h = _status_o = _status_n = 0

    str_mod = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    num_mod = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    symb_mod = ["_", "+", "-", "*", "/", "=", "?", ",", ".", "'", "\"", ":",
                ";", "!", "@", "#", "$", "%", "^", "&", "(", ")", "[", "]", "{", "}"]

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(GlobleCls, "_instance"):
            with GlobleCls._instance_lock:
                if not hasattr(GlobleCls, "_instance"):
                    GlobleCls._instance = super(
                        GlobleCls, cls).__new__(cls, *args, **kwargs)
        return GlobleCls._instance

    # 普通模式
    def nomal_output:
        pass

    # 输入模式
    def input_output:
        pass

    # 输出
    def outText:
        if input_type == 1:
            pass
        pass

    def run(self, init_x, init_y):
        tim12 = Timer(12)

        def on_touchpad_P_pressed():
            global g_my_variable
            pass

        def on_touchpad_P_unpressed(): pass
        def on_touchpad_Y_pressed(): pass
        def on_touchpad_Y_unpressed(): pass
        def on_touchpad_T_pressed(): pass
        def on_touchpad_T_unpressed(): pass
        def on_touchpad_H_pressed(): pass
        def on_touchpad_H_unpressed(): pass
        def on_touchpad_O_pressed(): pass
        def on_touchpad_O_unpressed(): pass
        def on_touchpad_N_pressed(): pass
        def on_touchpad_N_unpressed(): pass

        def timer12_tick(_):
            try:
                touchPad_P.read()
                pass
            except:
                return
            if touchPad_P.read() < touch_threshold['P']:
                if 1 != self._status_p:
                    self._status_p = 1
                    on_touchpad_P_pressed()
            elif 0 != self._status_p:
                self._status_p = 0
                on_touchpad_P_unpressed()
            if touchPad_Y.read() < touch_threshold['Y']:
                if 1 != self._status_y:
                    self._status_y = 1
                    on_touchpad_Y_pressed()
            elif 0 != self._status_y:
                self._status_y = 0
                on_touchpad_Y_unpressed()
            if touchPad_T.read() < touch_threshold['T']:
                if 1 != self._status_t:
                    self._status_t = 1
                    on_touchpad_T_pressed()
            elif 0 != self._status_t:
                self._status_t = 0
                on_touchpad_T_unpressed()
            if touchPad_H.read() < touch_threshold['H']:
                if 1 != self._status_h:
                    self._status_h = 1
                    on_touchpad_H_pressed()
            elif 0 != self._status_h:
                self._status_h = 0
                on_touchpad_H_unpressed()
            if touchPad_O.read() < touch_threshold['O']:
                if 1 != self._status_o:
                    self._status_o = 1
                    on_touchpad_O_pressed()
            elif 0 != self._status_o:
                self._status_o = 0
                on_touchpad_O_unpressed()
            if touchPad_N.read() < touch_threshold['N']:
                if 1 != self._status_n:
                    self._status_n = 1
                    on_touchpad_N_pressed()
            elif 0 != self._status_n:
                self._status_n = 0
                on_touchpad_N_unpressed()

        tim12.init(period=100, mode=Timer.PERIODIC, callback=timer12_tick)
