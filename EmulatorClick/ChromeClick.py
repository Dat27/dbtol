
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import io
import re
import time

verification_code = ''
def getVerificationCode(a,mailPathVar,proxyPathVar) :
    # settup
    f = io.open(proxyPathVar,'r', encoding='utf-8')
    proxyList = f.readlines()
    f.close()
    proxiePro = proxyList[a].split(':')
    options = {
        'proxy': {
            'http': 'http://'+proxiePro[2]+':'+proxiePro[3].strip()+'@'+proxiePro[0]+':'+proxiePro[1], 
            'https': 'http://'+proxiePro[2]+':'+proxiePro[3].strip()+'@'+proxiePro[0]+':'+proxiePro[1],
            'no_proxy': 'localhost,127.0.0.1' # excludes
        }
    }

    driver = webdriver.Chrome(executable_path='C:/fbTool/chromedriver.exe',seleniumwire_options= options)
    driver.set_window_size(1200,800)
    driver.implicitly_wait(15)
    driver.get('https://outlook.live.com/owa/')
    # time.sleep(30)
    # start
    el = driver.find_element(By.CSS_SELECTOR,'a.sign-in-link')
    driver.execute_script("arguments[0].click();",el)
    f = io.open(mailPathVar, mode="r", encoding="utf-8")
    mailList= f.readlines()
    f.close()
    mail = mailList[1]
    x = mail.split("|")
    el = driver.find_element(By.CSS_SELECTOR,'input.form-control')
    el.send_keys(x[0])
    time.sleep(1)
    el = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
    driver.execute_script("arguments[0].click();",el)
    time.sleep(1)
    el = driver.find_element(By.NAME,'passwd')
    el.send_keys(x[1])
    time.sleep(1)
    el = driver.find_element(By.ID,'idSIButton9')
    el.submit()
    time.sleep(1)
    el = driver.find_element(By.ID,'idBtn_Back')
    el.submit()
    time.sleep(5)
    el = driver.find_elements(By.CSS_SELECTOR,'.xfjq3 > span')
    for x in el:
        global verification_code
        verification = re.findall(r'\b\d+\b' , x.text)
        if len(verification):
            verification_code = verification[0]
    # end
    time.sleep(1)
    driver.quit()
    return verification_code
# getVerificationCode(a=0, mailPathVar='C:\\fbTool\hotmai23-9.txt', proxyPathVar="C:\\fbTool\proxy.txt")



