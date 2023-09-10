from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome("C:\\Users\\vinhp\Desktop\\Coding Projects\\Panda\\chromedriver.exe")
driver.get('https://play.typeracer.com')

time.sleep(7)

pyautogui.hotkey('ctrl', 'alt', 'i')

time.sleep(12)

text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
print(text[-3])
time.sleep(5)

pyautogui.typewrite(text[-3], interval=0.046)

time.sleep(20)
driver.quit()