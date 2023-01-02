"""
Automatic Google Dinosaur game
"""
from selenium.webdriver import Chrome
import pyautogui

driver = Chrome()
DINO_GAME_URL = "https://elgoog.im/t-rex/?bot"
driver.get(DINO_GAME_URL)
pyautogui.PAUSE = 1
pyautogui.keyDown("space ")
while True:
    print(pyautogui.position())
    print(pyautogui.size())
    pyautogui.PAUSE = 1
    pyautogui.keyDown("up")
    pass



