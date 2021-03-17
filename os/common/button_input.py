from mpython import *
import time
import threading

class BtnInputController:

    a_state = False
    b_state = False

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(GlobleController, "_instance"):
            with GlobleController._instance_lock:
                if not hasattr(GlobleController, "_instance"):
                    GlobleController._instance = super(
                        GlobleController, cls).__new__(cls, *args, **kwargs)
        return GlobleController._instance

    def _tap_down():
        # 事件回调函数
        def on_button_a_down(_):
            global g_my_variable
            time.sleep_ms(10)
            if button_a.value() == 1:
                return
            pass
        def on_button_b_down(_):
            global g_my_variable
            time.sleep_ms(10)
            if button_b.value() == 1:
                return
            pass
        button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)
        button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)

    def tap_a_button():
        pass

    def run(self):
        self._tap_down()
        pass

