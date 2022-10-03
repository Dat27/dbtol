import os
from time import sleep
import io
import random
from appium.webdriver.common.appiumby import AppiumBy
from appium import *
from Connect.ConnectAppium import ConnectAppium
from Launch.Launch import Launch
from EmulatorClick.ChromeClick import getVerificationCode






class EmulatorClick():
    def __init__(self,by,path):
        self.by = by
        self.path = path
    def regFb(a,mailPathVar,proxyPathVar):
        Launch.modifyImei(a)
        print('modify thanh cong')
        Launch.launchLD(a)
        driver = ConnectAppium.conn(a,str(4723+a), proxyPathVar)
        ConnectAppium.install(a)
        driver.implicitly_wait(20)
        driver.press_keycode(3)
        el = driver.find_element(AppiumBy.ID,'com.ldmnq.launcher3:id/preview_background')
        el.click()
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lite')
        el.click()
        try:
            el = driver.find_element(AppiumBy.ID,'com.android.packageinstaller:id/permission_deny_button')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup[3]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup')
            el.click()

            f = io.open("ten.txt", mode="r", encoding="utf-8")
            first= f.readlines()
            f.close()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView[1]')
            el.click()
            el.send_keys(first[random.randint(0,49)].strip())
            sleep(2)
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView[2]')
            el.click()
            el.send_keys(first[random.randint(49,99)].strip())
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup')
            el.click()
            el = driver.find_element(AppiumBy.ID,'com.android.packageinstaller:id/permission_deny_button')
            el.click()
            el = driver.find_element(AppiumBy.ID,'com.android.packageinstaller:id/permission_deny_button')
            el.click()
            sleep(2)
            el = driver.find_element(AppiumBy.ID,'com.android.packageinstaller:id/permission_deny_button')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.View')
            el.click()


            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.widget.MultiAutoCompleteTextView')
            el.click()
            f = io.open(mailPathVar, mode="r", encoding="utf-8")
            mailList= f.readlines()
            f.close()
            mail = mailList[a]
            x = mail.split("|")
            el.send_keys(x[0])
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[1]')
            el.click()

            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View[1]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup['+str(random.choice([1,2,11]))+']/android.view.View')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup['+str(random.randint(1,9))+']/android.view.View')
            el.click()

            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View[3]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup['+str(random.randint(1,9))+']/android.view.View')
            el.click()

            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View[5]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.View')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup[9]/android.view.View')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup[9]/android.view.View')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup['+str(random.randint(6,9))+']/android.view.View')
            el.click()

            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup['+str(random.randint(1,2))+']/android.view.View[1]')
            el.click()
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[4]/android.widget.MultiAutoCompleteTextView')
            el.click()
            el.send_keys(x[1])
            el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[4]/android.view.ViewGroup')
            # el.click()
            driver.implicitly_wait(5)
            verification_code = getVerificationCode(a=a, mailPathVar=mailPathVar, proxyPathVar=proxyPathVar)
            print(verification_code)
            
            # after get code

            # delete mail
            # f = io.open(mailPathVar,'r', encoding='utf-8')
            # lines = f.readlines()
            # f.close()
            # deleteLine = lines[a]

            # f = io.open(mailPathVar,'w',encoding='utf-8')
            # for line in lines:
            #     if line.strip() == deleteLine.strip():
            #         pass
            #     else:
            #         f.write(line)
            #         # print('viet dong: '+line)
            # f.close()

            # change proxy
            # f = io.open(proxyPathVar,'r', encoding='utf-8')
            # lines = f.readlines()
            # f.close()
            # deleteLine = lines[0]

            # f = io.open(proxyPathVar,'w',encoding='utf-8')
            # for line in lines:
            #     if line.strip() == deleteLine.strip():
            #         pass
            #     else:
            #         f.write(line)
            # f.close()

            # f = io.open(proxyPathVar,'a',encoding='utf-8')
            # f.write(deleteLine)
            # f.close()

            ConnectAppium.uninstall(a)

            driver.quit()

        except:
            # delete mail
            # f = io.open(mailPathVar,'r', encoding='utf-8')
            # lines = f.readlines()
            # f.close()
            # deleteLine = lines[a]

            # f = io.open(mailPathVar,'w',encoding='utf-8')
            # for line in lines:
            #     if line.strip() == deleteLine.strip():
            #         pass
            #     else:
            #         f.write(line)
            #         # print('viet dong: '+line)
            # f.close()

            # change proxy
            # f = io.open(proxyPathVar,'r', encoding='utf-8')
            # lines = f.readlines()
            # f.close()
            # deleteLine = lines[0]

            # f = io.open(proxyPathVar,'w',encoding='utf-8')
            # for line in lines:
            #     if line.strip() == deleteLine.strip():
            #         pass
            #     else:
            #         f.write(line)
            # f.close()

            # f = io.open(proxyPathVar,'a',encoding='utf-8')
            # f.write(deleteLine)
            # f.close()
            pass
        else:
            driver.quit()
            pass