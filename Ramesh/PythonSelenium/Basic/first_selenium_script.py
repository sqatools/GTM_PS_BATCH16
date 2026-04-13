# Istall selenium with given command
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/?tag=msndeskabkin-21&ref=pd_sl_5twasf2d2w_e&adgrpid=1318316051640309&hvadid=82395019828275&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=148991&hvtargid=kwd-82395637438085:loc-90&hydadcr=5652_2377259&mcid=b983ec7c37413e6ab8b5124ff4bfc77b")
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Bat")
    time.sleep(2)
    # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Ball")

    # time.sleep(10)
    driver.close()

launch_website_and_verify()