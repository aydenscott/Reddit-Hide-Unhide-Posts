import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import red_username, red_password

source = r"https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F"
driver = webdriver.Chrome()
driver.get(source)
driver.maximize_window()


# Log in
def login():
    driver.find_element_by_class_name("AnimatedForm__textInput").send_keys(red_username)
    driver.find_element_by_xpath(r"//*[@id='loginPassword']").send_keys(red_password, Keys.ENTER)
    time.sleep(5)


def hide():
    hidesum = 0
    while True:
        hidelist = driver.find_elements_by_link_text("hide")
        count = len(hidelist)
        hidesum += count
        for hide1 in hidelist:
            hide1.click()
            time.sleep(0.7)
        driver.find_element_by_class_name("next-button").click()
        time.sleep(2.5)
        print("%d posts have been hidden" % hidesum)


login()
hide()
