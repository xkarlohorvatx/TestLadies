from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriver binary must be in PATH
browser = webdriver.Chrome('chromedriver')
browser.get('http://seleniumhq.org/')

try:
    el = browser.find_element_by_class_name('downloadBox')
    el.click()

    re = WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Downloads')
    )

    print("Test OK")

except:
    print("Sorry, it didn't work")

finally:
    browser.quit()
