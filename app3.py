# Selenium Tutorial #3
# Learning: Page navigation. Links, buttons, triggering events.

# Goal: Want to click Python Programming on main page > Beginner Python Tutorials > Get Started button.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
link.click()


try:
    # Allows us to go to Beginner Python Tutorials Page
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    # allows us to clear anyting in the field prior to clicking.
    element.clear()
    element.click()

    # Allows us to click the button to Get Started
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-1931003"))
    )
    element.click()

    # Allows browser to go back 3 pages.
    driver.back()
    driver.back()
    driver.back()
    # Allows browser to go forward 2 pages.
    driver.forward()
    driver.forward()


except:
    driver.quit()
