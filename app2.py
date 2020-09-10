# Selenium Tutorial #2
# Goals: Access Search bar, Search for something and then extract all search results
from selenium import webdriver
# give us access to the enter key and the space key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
# access the search field
search = driver.find_element_by_name('s')
# Searching for the word "test" in the search results.
search.send_keys('test')
# Allows us to press enter key when searching for word
search.send_keys(Keys.RETURN)

# Explict wait allows the page to scaper to pause prior to scraping the first results (https://selenium-python.readthedocs.io/waits.html)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # prints all the text of the search results which is in the dev tools inspect as ID = Main for all results.
    # print(main.text)

    # Allows to print all header tags of the search results
    articles = main.find_elements_by_tag_name('article')
    # loop through articles to find headers then print it out.
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)
finally:
    driver.quit()


# prints the entire source code of a page
# print(driver.page_source)


# Allows the website to appear results for 5 seconds then closes window.
# time.sleep(5)

driver.quit()
