from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
consent = driver.find_element(by=By.CLASS_NAME, value='fc-button-label')
consent.click()
time.sleep(2)
language = driver.find_element(by=By.ID, value='langSelect-EN')
language.click()
time.sleep(2)
cookie = driver.find_element(by=By.ID, value='bigCookie')
product_list = ['0']

def get_cookies():
    for i in range(200):
        cookie.click()


def get_money():
    cookies = driver.find_element(by=By.XPATH, value="//div[@id='cookies' and @class='title']")
    cookies = cookies.text.split('\n')[0].strip(' cookies''')
    return int(cookies)


def search_upgrades():
    upgrades = driver.find_element(By.ID, 'upgrades')
    list_upgrades = upgrades.find_elements(By.TAG_NAME, 'div')
    for upgrade in reversed(list_upgrades):
        try:
            upgrade.click()
        except Exception as e:
            print(e)

def search_products(list):
    product = driver.find_element(By.ID, 'products')
    products = product.find_elements(By.TAG_NAME, 'div')
    last_item = list[-1]
    try:
        product_number = product.find_element(By.ID, f'product{int(last_item)+1}')
        global product_list
        item = int(last_item)+1
        product_list.append(str(item))
    except Exception as e:
        print(e)
    for item in list:
        try:
            print(item)
            product_number = product.find_element(By.ID, f'product{item}')
            product_number.click()
        except Exception as e:
            print(e)


while True:
    get_cookies()
    search_upgrades()
    get_cookies()
    search_products(product_list)






