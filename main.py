from machine import Timer  # 导入计时模块
from micro_os.index import step

tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=step)
