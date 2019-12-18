from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    x = browser.find_element_by_id('input_value').text
    x = calc(int(x))


    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()