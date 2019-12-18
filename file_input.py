from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Alesha")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Grishhenko")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Alesha0808@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    element = browser.find_element_by_name('file')
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #time.sleep(1)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()