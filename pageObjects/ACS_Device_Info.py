# import time
# from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import common
from utilities.customLogger import LogGen


class ACS_Device_Info:

    button_starttrace_xpath = "//input[@id='btnSetTrace_btn']"
    button_stoptrace_xpath = "//input[@id='btnStopTrace_btn']"
    button_showtrace_xpath = "//input[@id='btnShowTrace_btn']"
    tabledata_deviceinfo_xpath = "//span[@id='lmi3']"
    text_description_xpath = "//table[@id='tblDeviceInfo']/tbody[1]/tr[1]/td[2]"
    text_hardwareversion_xpath = "//table[@id='tblDeviceInfo']/tbody[1]/tr[2]/td[2]"
    text_firmwareversion_xpath = "//table[@id='tblDeviceInfo']/tbody[1]/tr[3]/td[2]"
    text_manufacturer_xpath = "//table[@id='tblDeviceInfo']/tbody[1]/tr[5]/td[2]"
    text_modelname_xpath = "//table[@id='tblDeviceInfo']/tbody[1]/tr[7]/td[2]"
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.temp_xpath = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_TableDataDeviceInfo(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_deviceinfo_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_deviceinfo_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_deviceinfo_xpath).click()

    def clickStartTrace(self):
        try:
            #time.sleep(4)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            print("Start trace")
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_starttrace_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.button_starttrace_xpath).click()
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info(" ************************* Start Trace Clicked *************************")
        except (common.exceptions.NoAlertPresentException, common.exceptions.NoSuchElementException):
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            time.sleep(3)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_starttrace_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.button_starttrace_xpath).click()
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info(" ************************* Start Trace Clicked *************************")
        # self.driver.find_element(By.XPATH, self.button_starttrace_xpath).click()

    def clickStopTrace(self):
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_stoptrace_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.button_stoptrace_xpath).click()
            print("Stop trace")
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(10)
            self.logger.info(" ************************* Stop Trace Clicked *************************")
            self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH, "//span[@id='lmi3']").click()
        except (common.exceptions.NoSuchElementException, common.exceptions.StaleElementReferenceException):
            pass
        except common.exceptions.NoAlertPresentException:
            self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH, "//span[@id='lmi3']").click()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            time.sleep(3)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_stoptrace_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.button_stoptrace_xpath).click()
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(10)
            self.logger.info(" ************************* Stop Trace Clicked *************************")
            self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH, "//span[@id='lmi3']").click()
        # self.driver.find_element(By.XPATH, self.button_stoptrace_xpath).click()

    def clickShowTrace(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_showtrace_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_showtrace_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_showtrace_xpath).click()

    def getTextDescription(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_description_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.text_description_xpath).text
        # return self.driver.find_element(By.XPATH, self.text_description_xpath).text

    def getTextHardwareVersion(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_hardwareversion_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.text_hardwareversion_xpath).text
        # return self.driver.find_element(By.XPATH, self.text_hardwareversion_xpath).text

    def getTextSoftwareVersion(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_firmwareversion_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.text_firmwareversion_xpath).text
        # return self.driver.find_element(By.XPATH, self.text_firmwareversion_xpath).text

    def getTextManufacturer(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_manufacturer_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.text_manufacturer_xpath).text
        # return self.driver.find_element(By.XPATH, self.text_manufacturer_xpath).text

    def getTextModelName(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_modelname_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.text_modelname_xpath).text
        # return self.driver.find_element(By.XPATH, self.text_modelname_xpath).text

    def clickFactoryReset(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frmButtons")
        print("Start Factory Reset")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='btnReset_btn']")))
        finally:
            self.driver.find_element(By.XPATH, "//input[@id='btnReset_btn']").click()
        # self.driver.find_element(By.XPATH, "//input[@id='btnReset_btn']").click()
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info("************************* Factory Reset Clicked *************************")
        except common.exceptions.NoAlertPresentException:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            time.sleep(3)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='btnReset_btn']")))
            finally:
                self.driver.find_element(By.XPATH, "//input[@id='btnReset_btn']").click()
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info("************************* Factory Reset Clicked *************************")
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.modelpopup()
        # time.sleep(2)

    def clickReboot(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frmButtons")
        print("Start Reboot")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='btnReboot_btn']")))
        finally:
            self.driver.find_element(By.XPATH, "//input[@id='btnReboot_btn']").click()
        # self.driver.find_element(By.XPATH, "//input[@id='btnReboot_btn']").click()
        # time.sleep(3)
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info(" ************************* Reboot Clicked *************************")
        except common.exceptions.NoAlertPresentException:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            time.sleep(3)
            try:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='btnReboot_btn']")))
            finally:
                self.driver.find_element(By.XPATH, "//input[@id='btnReboot_btn']").click()
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(2)
            alert.accept()
            time.sleep(5)
            self.logger.info(" ************************* Reboot Clicked *************************")
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.modelpopup()
        # time.sleep(2)

    def modelpopup(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnAlertOk_btn"]')))
        finally:
            self.driver.find_element(By.XPATH, '//*[@id="btnAlertOk_btn"]').click()

