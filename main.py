from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import undetected_chromedriver as uc

url = "https://autoteka.ru/report_by_identifier/YNUMBERMK71"

browser = uc.Chrome()

for i in range(72, 1000, 1):
    eurl = ""
    if i < 10:
        eurl = url.replace("NUMBER", "00" + str(i))
    elif i < 100:
        eurl = url.replace("NUMBER", "0" + str(i))
    else:
        eurl = url.replace("NUMBER", str(i))

    print(i)
    browser.get(eurl)

    carFound = True
    while len(browser.find_elements(By.CLASS_NAME, "moQlJ")) == 0:
        time.sleep(1)



        if len(browser.find_elements(By.CLASS_NAME, "Tl8gM")) > 0:
            if browser.find_elements(By.CLASS_NAME, "Tl8gM")[0].text == "Данных для формирования отчёта по указанному госномеру недостаточно":
                carFound = False
                break
            else:
                print(browser.find_elements(By.CLASS_NAME, "Tl8gM")[0].text)

        if len(browser.find_elements(By.CLASS_NAME, "peKFe")) > 0:
            break

    if carFound:
        el = ""
        if len(browser.find_elements(By.CLASS_NAME, "moQlJ")) > 0:
            el = browser.find_elements(By.CLASS_NAME, "moQlJ")[0]
        elif len(browser.find_elements(By.CLASS_NAME, "peKFe")) > 0:
            el = browser.find_elements(By.CLASS_NAME, "peKFe")[0]
        with open("cars", "a+", encoding="utf-8") as f:
            f.write(str(i) + ", " + el.text + "\n")
            f.close()
        print(el.text)

browser.quit()

# import undetected_chromedriver as uc
# import time
# driver = uc.Chrome()
# url = "https://autoteka.ru/report_by_identifier/Y013MK71"
# driver.get(url)

# time.sleep(100)
