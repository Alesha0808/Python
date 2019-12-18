from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Alesha")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Grishhenko")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Novosibrisk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()