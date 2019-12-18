from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"




try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_number = browser.find_element_by_id('input_value')
    x = x_number.text
    y = calc(x)
    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)


    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()