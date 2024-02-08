import time
import traceback
import pytest
from selenium import common
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.LoginPage import ACS_LoginPage, JioCentrum_LoginPage
from utilities.ReadTestData import ReadTestData
from utilities.WriteTestData import SSIDConfigSet
from utilities.customLogger import LogGen


class Test_LoginPage:
    omitssid = str(ReadTestData.getomitssid())
    factory_pass = ReadTestData.getFactoryResetPassword()
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.av = ACS_Advanced_View(self.driver)
        self.lp = ACS_LoginPage(self.driver)
        self.jlp = JioCentrum_LoginPage(self.driver)

    @pytest.mark.skip(reason="Executing Twice")
    def ACS_LoginPage(self):
        try:
            baseURL = ReadTestData.getACSURL()
            username = ReadTestData.getUserName()
            password = ReadTestData.getPassword()
            serial_no = ReadTestData.getSerialno()
            self.logger.info("************** Login to ACS ****************")
            self.driver.get(baseURL)
            # time.sleep(5)
            self.lp.setUsername(username)
            self.lp.setPassword(password)
            # time.sleep(2)
            self.lp.clickLogin()
            time.sleep(5)
            self.driver.switch_to.default_content()
            self.av.clickTableDataSearch()
            self.driver.switch_to.frame("frmDesktop")
            # time.sleep(4)
            self.av.setSearch(serial_no)
            # time.sleep(1)
            self.av.clickSearchButton()
            time.sleep(5)

        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")

    def JioCentrum_LoginPage(self):
        try:
            # time.sleep(2)
            hgw_URL = ReadTestData.getHGWURL()
            username_HGW = ReadTestData.getUserNameHGW()
            password_HGW = ReadTestData.getPasswordHGW()
            self.logger.info("************** Login to GUI Portal ****************")
            self.driver.get(hgw_URL)
            # time.sleep(5)
            self.jlp.setUsername(username_HGW)
            self.jlp.setPassword(password_HGW)
            # time.sleep(2)
            self.jlp.clickLogin()
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='card_lan_ipaddr']")))
            except TimeoutException:
                self.logger.info("************** Login to GUI Portal ****************")
                self.driver.get(hgw_URL)
                self.jlp.setUsername(username_HGW)
                self.jlp.setPassword(password_HGW)
                self.jlp.clickLogin()
                time.sleep(3)

            time.sleep(3)
            # self.jlp.managerforcedlogin()
            # time.sleep(5)

        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")

    def JioCentrum_FactoryResetLogin(self):
        try:
            hgw_URL = ReadTestData.getHGWURL()
            username_HGW = ReadTestData.getUserNameHGW()
            password = 'Jiocentrum'
            password_HGW = ReadTestData.getPasswordHGW()
            lp = JioCentrum_LoginPage(self.driver)
            self.logger.info("************** Login to JioCentrum Portal after Factory Reset ****************")
            self.driver.get(hgw_URL)
            time.sleep(5)
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="tf1_userName"]')))
            finally:
                self.driver.find_element(By.XPATH, '//*[@id="tf1_userName"]').clear()
                self.driver.find_element(By.XPATH, '//*[@id="tf1_userName"]').send_keys(username_HGW)

            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="tf1_password"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@id="tf1_password"]').clear()
                self.driver.find_element(By.XPATH, '//input[@id="tf1_password"]').send_keys(password)

            time.sleep(2)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="loginBtn"]')))
            finally:
                self.driver.find_element(By.XPATH, '//*[@class="loginBtn"]').click()

            self.logger.info(" ************************* Logged In to Jio Centrum *************************")
            time.sleep(5)
            lp.managerforcedlogin()
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="tf1_adminPassword"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@id="tf1_adminPassword"]').clear()
                self.driver.find_element(By.XPATH, '//input[@id="tf1_adminPassword"]').send_keys(password_HGW)

            self.logger.info(" ************************* Admin Password Changed *************************")
            time.sleep(2)
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="tf1_cnfAdminPassword"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@id="tf1_cnfAdminPassword"]').clear()
                self.driver.find_element(By.XPATH, '//input[@id="tf1_cnfAdminPassword"]').send_keys(password_HGW)

            self.logger.info(" ************************* Admin Password Confirmed *************************")
            time.sleep(2)
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="tf1_guestPassword"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@id="tf1_guestPassword"]').clear()
                self.driver.find_element(By.XPATH, '//input[@id="tf1_guestPassword"]').send_keys(password_HGW)

            self.logger.info(" ************************* Guest Password Changed *************************")
            time.sleep(2)
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="tf1_cnfGuestPassword"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@id="tf1_cnfGuestPassword"]').clear()
                self.driver.find_element(By.XPATH, '//input[@id="tf1_cnfGuestPassword"]').send_keys(password_HGW)

            self.logger.info(" ************************* Guest Password Confirmed *************************")
            time.sleep(2)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="button.changePassword.changePassword"]')))
            finally:
                self.driver.find_element(By.XPATH, '//input[@name="button.changePassword.changePassword"]').click()

            self.logger.info(" ************************* Submit Button Clicked *************************")
            time.sleep(5)
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='msgError']/p[1]")))
            text = element.get_attribute('innerHTML')
            if 'User credentials are updated successfully.' in text:
                print('Password Changed Successfully.')
                self.logger.info(" ************************* Password Changed Successfully. *************************")
            else:
                print('Password Changed Unsuccessful.')
                self.logger.info(" ************************* Password Changed Unsuccessful. *************************")

            for i in range(6):
                SSIDConfigSet.setSSIDPASSWORD(i + 1, self.factory_pass)

        except common.exceptions.NoSuchElementException:
            print("No such element")
        except common.exceptions.WebDriverException:
            print("Web driver error")
        except AttributeError:
            print("Driver error")
