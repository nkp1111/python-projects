"""
Automatic Google Dinosaur game
"""
from selenium.webdriver import Chrome
import pyautogui
from time import sleep
from PIL import Image, ImageGrab

driver = Chrome()
DINO_GAME_URL = "https://elgoog.im/t-rex/?bot"
driver.get(DINO_GAME_URL)
sleep(1)
pyautogui.PAUSE = 1

pyautogui.keyDown("up")
sleep(1)

while True:
    pyautogui.keyUp("up")
    img = ImageGrab.grab().convert("L")
    image_data = img.load()

    for i in range(440, 500):
        for j in range(530, 580):
            print(image_data[i, j])
            if image_data[i, j] < 160:
                pyautogui.keyDown("up")
                break
