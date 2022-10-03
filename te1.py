from Connect.ConnectAppium import ConnectAppium
from EmulatorClick.LdClick import EmulatorClick
from Launch.Launch import Launch
# from appium.webdriver.common.appiumby import AppiumBy
from appium import *
import _thread

def ld(a=int):
    EmulatorClick.regFb(a=a, mailPathVar='C:\\fbTool\hotmai23-9.txt', proxyPathVar='C:\\fbTool\proxy.txt')
    pass
num = 1
try:
    for i in range(num):
        _thread.start_new_thread(ld, (i,))
except:
    print('error')
while 1:
    pass