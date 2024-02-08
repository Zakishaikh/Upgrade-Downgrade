from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import common
import time
from selenium.webdriver.support.ui import Select


class ACS_CustomRPC:

    button_customrpc_xpath = "//span[@nameinner='Custom RPC']"
    select_methodname_xpath = "//select[@id='ddlMethods']"
    button_customrpcSetParameterValues_xpath = "//select[@id='ddlMethods']/option[@value='SetParameterValues']"
    textarea_customrpctextrequest_xpath = "//textarea[@id='txtRequest']"
    button_cancel_xpath = "//input[@id='btnCancel_btn']"
    button_sendupdate_xpath = "//input[@id='btnSendUpdate_btn']"
    button_add_xpath = "//input[@id='btnAdd_btn']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clickCustomRPC(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_customrpc_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_customrpc_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_customrpc_xpath).click()

    def clickCustomRPCSelectSetParameterValues(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_methodname_xpath)))
        finally:
            element = self.driver.find_element(By.ID, "ddlMethods")
            se = Select(element)
            se.select_by_visible_text("SetParameterValues")
        # self.driver.find_element(By.XPATH, self.button_customrpcSetParameterValues_xpath).click()

    def clickCustomRPCSelectUpload(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_methodname_xpath)))
        finally:
            element = self.driver.find_element(By.ID, "ddlMethods")
            se = Select(element)
            se.select_by_visible_text("Upload")

    def setCustomRPCTextrequest(self, text):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textarea_customrpctextrequest_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textarea_customrpctextrequest_xpath).clear()
            try:
                self.driver.find_element(By.XPATH, self.textarea_customrpctextrequest_xpath).send_keys(text)
            except common.exceptions.ElementNotInteractableException:
                pass
        # self.driver.find_element(By.XPATH, self.textarea_customrpctextrequest_xpath).clear()
        # self.driver.find_element(By.XPATH, self.textarea_customrpctextrequest_xpath).send_keys(text)

    def clickButtonCancel(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_cancel_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_cancel_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_cancel_xpath).click()

    def clickButtonSendUpdate(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_sendupdate_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_sendupdate_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_sendupdate_xpath).click()

    def clickButtonAdd(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_add_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_add_xpath).click()

    def clickAlert(self):
        time.sleep(4)
        alert = self.driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        time.sleep(3)
