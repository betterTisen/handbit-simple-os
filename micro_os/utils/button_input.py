from mpython import *
import time


class BtnInputControllerCls:

    a_state = False
    b_state = False


btnInputController = BtnInputControllerCls()

def on_button_a_down(_):
    global g_my_variable
    time.sleep_ms(10)
    if button_a.value() == 1 or btnInputController.a_state:
        return
    btnInputController.a_state = True
    pass


def on_button_b_down(_):
    global g_my_variable
    time.sleep_ms(10)
    if button_b.value() == 1 or btnInputController.b_state:
        return
    btnInputController.b_state = True
    pass


button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)
button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)
