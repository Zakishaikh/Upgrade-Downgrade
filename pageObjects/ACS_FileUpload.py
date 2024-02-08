from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import time
from utilities.customLogger import LogGen


class ACS_FileUpload:

    tabledata_fileupload_xpath = "//span[@id='lmi10']"
    button_cancel_xpath = "//input[@id='btnCancel_btn']"
    button_sendupdate_xpath = "//input[@id='btnSendUpdate_btn']"
    button_add_xpath = "//input[@id='btnAdd_btn']"
    radio_defaulturl_xpath = "//input[@id='rdTarget']"
    radio_manualurl_xpath = "//input[@id='rdUrl']"
    textbox_name_xpath = "//input[@id='tbName']"
    textbox_destinationurl_xpath = "//input[@id='tbUrl']"
    textbox_username_xpath = "//input[@id='tbLogin']"
    textbox_password_xpath = "//input[@id='tbPass']"
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.temp_xpath = None
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clickTabledataFileUpload(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_fileupload_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_fileupload_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_filedownload_xpath).click()

    def selectFiletypeVendorConfigurationFile(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlFileType")))
        finally:
            element = self.driver.find_element(By.ID, "ddlFileType")
            se = Select(element)
            se.select_by_visible_text("Vendor Configuration File")

    def selectFiletypeVendorLogFile(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlFileType")))
        finally:
            element = self.driver.find_element(By.ID, "ddlFileType")
            se = Select(element)
            se.select_by_visible_text("Vendor Log File")

    def selectFiletypeVendorLogFileInstance(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlFileType")))
        finally:
            element = self.driver.find_element(By.ID, "ddlFileType")
            se = Select(element)
            se.select_by_visible_text("Vendor Log File <i>")

    def clickDefaultURL(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.radio_defaulturl_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.radio_defaulturl_xpath).click()

    def clickManualURL(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.radio_manualurl_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.radio_manualurl_xpath).click()

    def setName(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_name_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_name_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(value)

    def setUsername(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(value)

    def setDestinationURL(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_destinationurl_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_destinationurl_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_destinationurl_xpath).send_keys(value)

    def setPassword(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(value)

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

    def selectInstance1(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlInstance")))
        finally:
            element = self.driver.find_element(By.ID, "ddlInstance")
            se = Select(element)
            se.select_by_visible_text("1")

    def selectInstance2(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlInstance")))
        finally:
            element = self.driver.find_element(By.ID, "ddlInstance")
            se = Select(element)
            se.select_by_visible_text("2")

    def selectInstance3(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "ddlInstance")))
        finally:
            element = self.driver.find_element(By.ID, "ddlInstance")
            se = Select(element)
            se.select_by_visible_text("3")

    def clickAlert(self):
        time.sleep(4)
        alert = self.driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        time.sleep(3)

    def getFileUploadStatus(self, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//span[@id="rptProfiles_ctl00_Label8"]')))
        finally:
            element = self.driver.find_element(By.XPATH, '//span[@id="rptProfiles_ctl00_Label8"]')
            str_value = element.get_attribute('innerHTML')
            if str_value == value:
                element = self.driver.find_element(By.XPATH, '//table[@id="tblFirmwares"]/tbody/tr[1]')
                str_value = element.get_attribute('isactive')
                if str_value == 'Fail':
                    return 'FAIL'
                elif str_value == 'Ok':
                    return 'PASS'
                elif str_value == 'NoInfo':
                    return 'NoInfo'
            else:
                self.logger.info('************ File Upload - ' + value + ' Not Available in Status Table ************')
                return 'FAIL'
