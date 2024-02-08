# from utilities.updateExcel import updateExcel
# from utilities.readProperties import ReadConfig
# from utilities.outputVariables import *
# from selenium.webdriver.common.by import By
import traceback

import pytest
from selenium import common

# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from pageObjects.ASCSearch import ASC_Search
# from pageObjects.ASCAdvancedView import ASC_Advanced_View
from pageObjects.ACS_Device_Info import ACS_Device_Info
from testCases.Test_LoginPage import Test_LoginPage
from utilities.customLogger import LogGen

list_deviceinfo = []


class Test_DeviceInfo:

    def __init__(self, driver):
        self.driver = driver
        self.li = Test_LoginPage(self.driver)
        self.di = ACS_Device_Info(self.driver)

    @pytest.mark.skip(reason="Executing Twice")
    def DeviceInfo(self):
        try:
            '''LogGen.loggen().info("************** Test TR069 ACS DeviceInfo ****************")
            self.li.ACS_LoginPage()
            self.driver.switch_to.default_content()
            # self.di.click_TableDataDeviceInfo()
            self.driver.switch_to.frame("frmDesktop")
            # self.description = self.di.text_description_xpath
            list_deviceinfo.append(self.di.getTextHardwareVersion())
            list_deviceinfo.append(self.di.getTextSoftwareVersion())
            list_deviceinfo.append(self.di.getTextManufacturer())
            list_deviceinfo.append(self.di.getTextModelName())'''
            self.driver.close()
        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
        finally:
            list_deviceinfo = ['NONE', 'NONE', 'NONE', 'NONE']
            for i in range(4 - len(list_deviceinfo)):
                list_deviceinfo.append(0)
            return list_deviceinfo
