from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Firefox(executable_path='C:/TEMP/geckodriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name('input.first')
    input1.send_keys("Alesha")
    input2 = browser.find_element_by_tag_name('input.second')
    input2.send_keys("Grishhenko")
    input3 = browser.find_element_by_tag_name('input.third')
    input3.send_keys("Alesha0808@yandex.ru")
    input4 = browser.find_element_by_xpath('//div/form/div[2]/div/input')
    input4.send_keys("01")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()