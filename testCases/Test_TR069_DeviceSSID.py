import sys
import time
import traceback

import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.WriteTestData import SSIDConfigSet
from utilities.customLogger import LogGen


class Test_TR069_DeviceSSID:
    omitssid = str(ReadTestData.getomitssid())

    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    result = 0
    # list_screenshot = ['not changed'] * 6
    testcase_name = "test_TR069_DeviceSSID"
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()
    list_value = ['TestJio 1 ab', 'TestJio 2 ab', 'TestJio 3 ab', 'TestJio 4 ab', 'TestJio 5 ab', 'TestJio 6 ab']
    list_accesspointvalue = [1, 1, 1, 1, 1, 1]
    list_advertisementvalue = [1, 1, 1, 1, 1, 1]
    list_maxassodevice = [10, 10, 10, 10, 10, 10]
    output = ''

    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.skip(reason="Executing Twice")
    def test_TR069_DeviceSSID(self):
        try:
            self.lp = Test_LoginPage(self.driver)

            # time.sleep(2)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.wait = WebDriverWait(self.driver, 10)
            # time.sleep(2)
            # time.sleep(4)
            self.av = ACS_Advanced_View(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            # time.sleep(2)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            # time.sleep(2)
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadSSID()
            # time.sleep(3)
            for i in range(1, 7):
                self.logger.info(
                    "************** Updating Wifi SSID " + str(i) + " Name ****************")
                self.av.clickTableDataSSID_index(i)
                time.sleep(2)
                self.av.setSSIDName(i, self.list_value[i - 1])
                self.driver.save_screenshot(".\\Screenshots\\" + self.testcase_name + str(i) + ".png")
                time.sleep(2)
            # time.sleep(2)

            self.output = self.acs.TR069_Sendupdate()

            if self.output == 'FAIL':
                self.logger.info('---------SSID NAME UPDATE TASK FAILED-----------')
                print('---------SSID NAME UPDATE TASK FAILED-----------')
                self.list_output.append('FAIL')
            else:
                self.logger.info('---------SSID NAME UPDATE TASK PASSED-----------')
                print('---------SSID NAME UPDATE TASK PASSED-----------')
                self.list_output.append('PASS')

            self.output = ''

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            # time.sleep(2)
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            # time.sleep(2)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            # time.sleep(2)
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableDataAccessPoint()
            for i in range(1, 7):
                self.logger.info(
                    "************** Updating Wifi AccessPoint " + str(i) + " ****************")
                # self.av.ClickTableHeadAccespoint(i)
                self.av.ClickTableDataAccespoint_index(i)
                time.sleep(2)
                self.av.setAccessPointEnable(i, self.list_accesspointvalue[i - 1])
                self.av.setAccessPointSSIDAdvertisementEnabled(i, self.list_advertisementvalue[i - 1])
                time.sleep(2)

            self.output = self.acs.TR069_Sendupdate()

            if self.output == 'FAIL':
                self.logger.info('---------ACCESSPOINT UPDATE TASK FAILED-----------')
                print('---------ACCESSPOINT UPDATE TASK FAILED-----------')
                self.list_output.append('FAIL')
                sys.exit()
            else:
                self.logger.info('---------ACCESSPOINT UPDATE TASK PASSED-----------')
                print('---------ACCESSPOINT UPDATE TASK PASSED-----------')
                self.list_output.append('PASS')

            self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            # time.sleep(2)
            self.jc.clicknetworkMenu()
            # time.sleep(3)
            self.jc.clickwireless()
            # time.sleep(3)
            # time.sleep(3)
            self.jc.profilebtn()
            l = self.jc.getSSIDNames()
            for i in range(0, 6):
                SSIDConfigSet.setSSIDNAME(i + 1, l[i])

        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
