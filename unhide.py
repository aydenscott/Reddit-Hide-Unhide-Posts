import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import red_password, red_username

source = r"https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F"
driver = webdriver.Chrome()
driver.get(source)
driver.maximize_window()


# Log in and move to hidden tab
def login():
    driver.find_element_by_class_name("AnimatedForm__textInput").send_keys(red_username)
    driver.find_element_by_xpath(r"//*[@id='loginPassword']").send_keys(red_password, Keys.ENTER)
    time.sleep(7)
    driver.find_element_by_xpath(r"//*[@id='header-bottom-right']/span[1]/a").click()  # Clicks profile
    driver.find_element_by_xpath(r"//*[@id='header-bottom-left']/ul/li[7]/a").click()  # Clicks hidden tab


# Unhide and go to next page
def clickall():
    hiddensum = 0
    while True:
        hidden = driver.find_elements_by_link_text("unhide")
        count = len(hidden)
        hiddensum += count
        if len(hidden) == 0:
            print("Program is done!")
            break
        for hiddenbutton in hidden:
            hiddenbutton.click()
            time.sleep(0.5)
        driver.refresh()
        time.sleep(1.5)
        print(str(hiddensum) + " posts have been unhidden")


login()
clickall()
driver.quit()