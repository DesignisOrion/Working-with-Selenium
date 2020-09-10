# Selenium Tutorial #1
# Goals: Connecting chrome driver, print out title.
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://designisorion.com")
print(driver.title)
driver.quit()
