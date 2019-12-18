from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    x_img = browser.find_element_by_id('treasure')
    x_number = x_img.get_attribute('valuex')
    x_element = browser.find_element_by_id('answer')
    x = x_number
    y = calc(x)
    x_element.send_keys(y)
    robots = browser.find_element_by_css_selector("[value='robots']")
    robots.click()
    robotCheckbox = browser.find_element_by_css_selector('input.check-input')
    robotCheckbox.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()