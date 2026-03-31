# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
title_sbis = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'


try:
    browser.get(sbis_site)
    assert browser.current_url == sbis_site, 'не верно открыли'
    time.sleep(3)

    butt = 'Контакты'
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href=\'/contacts')
    assert start_btn.text == 'Контакты', 'не верно открыли'
    assert start_btn.is_displayed(), 'не нашли элемент'
    start_btn.click()
    time.sleep(3)

    banner = browser.find_element(By.CSS_SELECTOR, '#contacts_clients [href="https://tensor.ru/"]')
    assert banner.is_displayed(), 'не нашли баннер'
    banner.click()
    time.sleep(3)

    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == tensor_site, 'не верно открыли'
    time.sleep(3)

    news_bloc = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    browser.execute_script("return arguments[0].scrollIntoView();", news_bloc)
    assert news_bloc.is_displayed()

    news_bloc_details = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    time.sleep(3)
    assert news_bloc_details.is_displayed(), 'элемент в блоке новостей не отображается'
    news_bloc_details.click()
    time.sleep(3)
    assert browser.current_url == tensor_site + 'about', 'ссылка не правильная'

finally:
    browser.quit()



