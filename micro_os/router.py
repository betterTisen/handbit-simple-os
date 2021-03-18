from micro_os.globle import globleController
# 展示列表
from micro_os.pages.default import route_idx as def_route_idx, step as def_step, route as def_route
from micro_os.pages.wifi import route_idx as wifi_route_idx, step as wifi_step, route as wifi_route


def set_route(_):
    if globleController.route == def_route_idx:
        def_step(_)
        def_route(_)
    elif globleController.route == wifi_route_idx:
        wifi_step(_)
        wifi_route(_)
    pass
