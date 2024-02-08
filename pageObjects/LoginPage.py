import time

from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ACS_LoginPage:

    textbox_name_id = "txtName"
    textbox_password_id = "txtPassword"
    button_login_xpath = "//input[@id='btnLogin_btn']"
    link_logout_xpath = "//img[@id='imgBtnLogout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def setUsername(self, username):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_name_id)))
            # print('Located Username')
        finally:
            self.driver.find_element(By.ID, self.textbox_name_id).clear()
            self.driver.find_element(By.ID, self.textbox_name_id).send_keys(username)
            # print('Clicked Username')

    def setPassword(self, password):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
            # print('Located Password')
        finally:
            self.driver.find_element(By.ID, self.textbox_password_id).clear()
            self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
            # print('Clicked Password')

    def clickLogin(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
            # print('Located Login Button')
        finally:
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()
            # print('Clicked Login Button')

    def clicklogout(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
        # self.driver.find_element(By.XPATH, self.link_logout_xpath).click()


class JioCentrum_LoginPage:

    textbox_name_xpath = '//input[@id="username"]'
    textbox_password_xpath = '//input[@id="userpassword"]'
    button_login_xpath = "//button[@id='loginBtn']"
    link_logout_xpath = "//div[@id='navbar_logout']"
    menulist_xpath = "//div[@id='h_menu_list']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setUsername(self, username):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_name_xpath)))
            # print('Located Login')
        finally:
            self.driver.find_element(By.XPATH, self.textbox_name_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(username)
            # print('Clicked Login')

    def setPassword(self, password):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
            # print('Located Password')
        finally:
            self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
            # print('Clicked Password')

    def clickLogin(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
            # print('Located Login Button')
        finally:
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()
            # print('Clicked Login Button')

    def clickMenuList(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menulist_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.menulist_xpath).click()

    def clicklogout(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
        # self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def managerforcedlogin(self):
        for i in range(0, 2):
            try:
                element = self.driver.find_element(By.XPATH, '//*[@id="tf1_forcedLoginDialog"]')
                element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tf1_forcedLoginContent"]/div/a')))
                time.sleep(5)
                element.click()
                print("Session Active")
                break
            except (common.exceptions.ElementNotInteractableException, TypeError):
                pass