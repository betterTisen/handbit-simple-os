import threading


class GlobleController:
    wifi_connect = False   # 是否连接wifi
    scope = 1           # 层级
    route = "/"         # 路由位置

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
