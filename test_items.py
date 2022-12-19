from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_productpage_contains_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    result = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(result)>0, "Can't find button"