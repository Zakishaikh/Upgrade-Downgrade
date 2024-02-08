from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import time


class ACS_File_Download:

    tabledata_filedownload_xpath = "//span[@id='lmi9']"
    dropdown_filetype_firmwareimage_xpath = "//select[@id='UcFirmware1_ddlFileType']/option[2]"
    radiobutton_fromlist_xpath = "//input[@id='UcFirmware1_rdTarget']"
    dropdown_filename_firstoption_xpath = "//select[@id='UcFirmware1_ddlFileName']/option[2]"
    dropdown_filename_secondoption_xpath = "//select[@id='UcFirmware1_ddlFileName']/option[3]"
    button_cancel_xpath = "//input[@id='btnCancel_btn']"
    button_sendupdate_xpath = "//input[@id='btnSendUpdate_btn']"
    button_add_xpath = "//input[@id='btnAdd_btn']"

    def __init__(self, driver):
        self.temp_xpath = None
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clickTabledataFileDownload(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_filedownload_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_filedownload_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_filedownload_xpath).click()

    def clickDropdownFiletypeFirmwareImage(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "UcFirmware1_ddlFileType")))
        finally:
            element = self.driver.find_element(By.ID, "UcFirmware1_ddlFileType")
            se = Select(element)
            se.select_by_index(1)
        '''try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_filetype_firmwareimage_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.dropdown_filetype_firmwareimage_xpath).click()'''

    def clickRadiobuttonFromList(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.radiobutton_fromlist_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.radiobutton_fromlist_xpath).click()
        # self.driver.find_element(By.XPATH, self.radiobutton_fromlist_xpath).click()

    def getLatestSoftwareVersionName(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "UcFirmware1_ddlFileName")))
        finally:
            element = self.driver.find_element(By.ID, "UcFirmware1_ddlFileName")
            se = Select(element)
            se.select_by_index(1)
            return se.first_selected_option.text

    def clickDropdownFilenameFirstOption(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "UcFirmware1_ddlFileName")))
        finally:
            element = self.driver.find_element(By.ID, "UcFirmware1_ddlFileName")
            se = Select(element)
            se.select_by_index(1)
        '''try:
            self.wait.until(EC.presence_of_element_located((By.ID, "UcFirmware1_ddlFileName")))
        finally:
            self.driver.find_element(By.XPATH, self.dropdown_filename_firstoption_xpath).click()'''
        # self.driver.find_element(By.XPATH, self.dropdown_filename_firstoption_xpath).click()

    def clickDropdownFilenameSecondOption(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "UcFirmware1_ddlFileName")))
        finally:
            element = self.driver.find_element(By.ID, "UcFirmware1_ddlFileName")
            se = Select(element)
            se.select_by_index(2)
        '''try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_filename_secondoption_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.dropdown_filename_secondoption_xpath).click()'''
        # self.driver.find_element(By.XPATH, self.dropdown_filename_secondoption_xpath).click()

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
