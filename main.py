from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
def get_driver():
    """
    Define all the options and the configuration
     of working with scraping and automations with the browser
    :return:
    """
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dec-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["Enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """
        Extract only the temperature from the input text
    :param text:
    :return:
    """
    #The Strategy of using string's approach is less recommended
    # output = text.split(": ")
    # return output[1]
    return re.findall(r'\d+', text)[0]

def main():
    #Loading page .....
    driver = get_driver()
    time.sleep(2)

    #Enter username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+
                            Keys.RETURN)
    time.sleep(2)
    #print(driver.current_url)

    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)


print(main())



