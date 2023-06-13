# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver import Keys

test_site = 'https://fix-online.sbis.ru/'
browser = webdriver.Chrome()

try:
    browser.get(test_site)
    sleep(3)
    u_login, u_password = 'атак2', 'й1ц2у3к4е5н6'
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    assert login.is_displayed(), 'не нашли логин'
    login.send_keys(u_login, Keys.ENTER)
    sleep(1)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    assert password.is_displayed(), 'не нашли пар'
    password.send_keys(u_password, Keys.ENTER)
    sleep(3)

    cont = browser.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]'[0])
    cont.click()
    sleep(5)



finally:
    browser.quit()

