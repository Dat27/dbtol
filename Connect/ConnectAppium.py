from appium import webdriver
import subprocess
import os
import io
import time

device_name= []
class ConnectAppium():
    def __init__(self, uuid, platformName, appPackage, appActivity):
        self.u_uid = uuid
        self.platform_name = platformName
        self.app_package = appPackage
        self.app_activity = appActivity
    
    def connectAppium(self,port = str):
        
        derised_cap = {
            "udid": self.u_uid,
            "platformName": self.platform_name,
            "appPackage": self.app_package,
            "appActivity": self.app_activity
        }
        
        driver = webdriver.Remote("http://localhost:"+port+"/wd/hub",derised_cap)
        print("connect emulator success "+self.u_uid)
        return driver

    def getProperty(a,proxyPathVar):
        os.system("adb devices")
        time.sleep(3)
        # os.system("adb devices")
        #get devices name
        get_devices_name = subprocess.check_output('adb devices', shell=True, universal_newlines=True)
        get_devices_name = get_devices_name.split()
        global device_name
        for x in get_devices_name:
            i= x.find("emulator")
            if i >= 0:
                device_name.append(x)
        f = io.open(proxyPathVar, mode="r", encoding="utf-8")
        first= f.readlines()
        f.close()
        os.system('adb -s '+device_name[a]+' shell settings put global http_proxy '+first[a])
        print("addproxy for"+device_name[a]+'success')
        time.sleep(3)
        connect_para_full = subprocess.check_output('adb -s '+device_name[a]+' shell dumpsys window | find "mCurrentFocus"', shell=True, universal_newlines=True)
        connect_para = connect_para_full.split()[2].rstrip("}")
        connect_para = connect_para.split("/")
        print("get property success")
        return connect_para
    def conn(a = str, p = str, proxyPath = str):
        connect_para = ConnectAppium.getProperty(int(a), proxyPath)
        driver = ConnectAppium.connectAppium(ConnectAppium(device_name[a],"Android",connect_para[0],connect_para[1]),p)
        return driver
    def uninstall(a = str):
        os.system('adb -s '+device_name[int(a)]+' uninstall com.facebook.lite')
        pass
    def install(a = str):
        os.system('adb -s '+device_name[int(a)]+' install fblite.apk')
        pass

# ConnectAppium.conn(0,'4723','C:\\fbTool\\proxy.txt')
# os.system('dir')
