from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, ('price')), '$100')
    )
    button = browser.find_element_by_tag_name("button")
    button.click()

    x = browser.find_element_by_id('input_value').text
    x = calc(int(x))


    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_id("solve").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()