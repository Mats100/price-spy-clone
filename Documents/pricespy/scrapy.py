import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"


def chrome_driver():
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--window-size=1920, 1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print('driver created')
    driver.get('https://pricespy.co.uk/')
    return driver


def get_headers(driver):
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 20)

    allow_cookies = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[@class='BaseButton--1lb73g9 gdudid primarybutton']")))
    allow_cookies.click()

    header_div = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[1]")))

    for index in range(1, 11):
        try:
            ActionChains(driver).move_to_element(header_div).perform()
            text = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div/ul/li[{index}]/div/a/div[2]/div/span")))

            image = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div/ul/li[{index}]/div/a/div[1]/img")))

            # price = wait.until(EC.presence_of_element_located(By.XPATH,f"//*[@id="root"]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/ul/li[4]/article/a/div[2]/div/div/span"))
            if index == 3:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div/button")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()
            if index == 6 or index == 9:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/div/button[2]")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()

            print('div_1', text.text, image.get_attribute('src'))
        except StaleElementReferenceException as e:
            print(e)

    extract_body_divs(driver, wait)


def scroll(driver):
    driver.execute_script("window.scrollTo(0, 1080)")


def extract_body_divs(driver, wait):

    # extract second div products
    second_divs = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[2]")))
    for index in range(1, 16):
        try:
            ActionChains(driver).move_to_element(second_divs).perform()
            text = wait.until(EC.presence_of_element_located((By.XPATH,
                                                              f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/ul/li[{index}]/div/a/div/div[1]/span[2]")))
            image = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/ul/li[{index}]/div/a/div/div[1]/img")))

            if index == 4:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/button")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()

            if index == 8:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div/button[2]")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()

            print('div_2', text.text, image.get_attribute('src'))
        except StaleElementReferenceException as e:
            print(e)

    # extract third div products
    third_divs = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]")))
    for index in range(1, 16):
        try:
            ActionChains(driver).move_to_element(third_divs).perform()
            text = wait.until(EC.presence_of_element_located((By.XPATH,
                                                              f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/ul/li[{index}]/article/a/div[2]/span[2]")))
            image = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               f"/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/ul/li[{index}]/article/a/div[1]/img")))
            if index == 4:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/button")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()

            if index == 8:
                next_button = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/div[3]/div[2]/div/div/button[2]")))
                time.sleep(1)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()

            print('div_3', text.text, image.get_attribute('src'))

        except StaleElementReferenceException as e:
            print(e)


if __name__ == "__main__":
    get_headers(chrome_driver())