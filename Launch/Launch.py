import os
import time
import io
import random

class Launch():
    def launchLD(a = int):
        os.chdir('C:\LDPlayer\LDPlayer9')
        a = str(a)
        os.system('dnconsole launch --index '+a)
        os.chdir('C:\\fbTool')
        time.sleep(25)
        return

    def quitLD(a = int):
        a = str(a)
        os.chdir('C:\LDPlayer\LDPlayer9')
        os.system('dnconsole quit --index '+a)
        os.chdir('C:\\fbTool')
        time.sleep(5)
        return

    def modifyImei(a = int):
        f = io.open("model.txt", mode="r", encoding="utf-8")
        modelList= f.readlines()
        f.close()
        os.chdir('C:\LDPlayer\LDPlayer9')
        a = str(a)
        head = 'dnconsole modify --index '+a
        os.system(head+' --imei auto --model '+ modelList[random.randint(0,12)])
        os.chdir('C:\\fbTool')
        return