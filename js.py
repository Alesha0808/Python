from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    x_number = browser.find_element_by_id('input_value').text
    x = x_number
    y = calc(x)
    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    robotCheckbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robotCheckbox.click()

    robots = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots)
    robots.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #time.sleep(1)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()