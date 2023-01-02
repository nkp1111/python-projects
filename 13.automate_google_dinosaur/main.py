"""
Automatic Google Dinosaur game
"""
from selenium.webdriver import Chrome

driver = Chrome()
DINO_GAME_URL = "https://elgoog.im/t-rex/?bot"
driver.get(DINO_GAME_URL)

while True:
    pass



