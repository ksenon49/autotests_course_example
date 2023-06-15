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
contacts = 'https://fix-online.sbis.ru/page/dialogs'
empioyee = 'Удачная Мария'
message = 'Кар'

try:
    browser.get(test_site)
    sleep(3)
    u_login, u_password = 'удачная', 'й1ц2у3к4е5н6'
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    assert login.is_displayed(), 'не нашли логин'
    login.send_keys(u_login, Keys.ENTER)
    sleep(1)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    assert password.is_displayed(), 'не нашли пар'
    password.send_keys(u_password, Keys.ENTER)
    sleep(5)

    browser.get(contacts)
    sleep(2)
    btn_pls = browser.find_element(By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[3]/div/div/div[5]/div[2]/div[1]/span/span')
    assert btn_pls.is_displayed(), 'не нашли кнопку сообщения'
    btn_pls.click()
    sleep(15)

    fio_search = browser.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_hideCustomPlaceholder')
    fio_search.send_keys(empioyee, Keys.ENTER)
    sleep(5)

    mes_autor = browser.find_element(By.CSS_SELECTOR, '.person-Info__withActivity')
    mes_autor.click()
    sleep(5)
    mes_text = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    mes_text.click()
    mes_text.send_keys(message)
    browser.maximize_window()
    sleep(6)

    mes_btn = browser.find_element(By.CSS_SELECTOR, '.controls-icon_style-contrast')
    mes_btn.click()
    sleep(3)

    check_mes = browser.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    sleep(2)
    assert check_mes.text == message, 'нет сообщ'

    action_chain = ActionChains(browser)
    action_chain.move_to_element(check_mes)
    action_chain.perform()
    sleep(2)
    delete_mes = browser.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_mes.click()
    sleep(3)
    check_mes = browser.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert check_mes != message, 'сообщ не удалено'

finally:
    browser.quit()

