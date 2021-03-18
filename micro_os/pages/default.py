from mpython import *
import time

from micro_os.globle import globleController
from micro_os.utils.button_input import btnInputController

route_idx = "/"

def route(_):
    globleController.route = route_idx    # 当前路由
    globleController.pre_route = route_idx    # 上级路由
    # 捕获A、B按钮
    if btnInputController.a_state :
        btnInputController.a_state = False
        globleController.route = "/connect-wifi"
        pass
    if btnInputController.b_state :
        btnInputController.b_state = False
        globleController.route = globleController.pre_route
        pass
    pass

def step(_):
    week = ["一", "二", "三", "四", "五", "六", "日"]
    time_str = "%s年%s月%s日 星期%s" % (str(time.localtime()[0]), str(
        time.localtime()[1]), str(time.localtime()[2]), week[time.localtime()[6]])
    time2_str = "%s时%s分" % (str(time.localtime()[3]), str(time.localtime()[4]))
    oled.fill(0)
    oled.DispChar(time_str, 0, 0, 1)
    oled.DispChar(time2_str, 0, 16, 1)
    oled.DispChar("按A连接wifi", 0*16, 3*16, 1)
    oled.DispChar("wifi断开", 5*16, 3*16, 1)
    oled.show()
    pass

