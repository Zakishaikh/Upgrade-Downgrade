import sys
import pytest
import time
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from utilities.customLogger import LogGen
from utilities.ReadTestData import ReadTestData
from utilities.ReadTestData import Excel_Env
from testCases.Test_LoginPage import Test_LoginPage
import traceback
from selenium import common


class Test_TR069_EnableAccesspoint:
    """ baseURL = ReadTestData.getACSURL()
    username = ReadTestData.getUserName()
    password = ReadTestData.getPassword()
    serial_no = ReadTestData.getSerialno()"""
    omitssid = str(ReadTestData.getomitssid())
    '''hgw_URL = ReadTestData.getHGWURL()
    username_HGW = ReadTestData.getUserNameHGW()
    password_HGW = ReadTestData.getPasswordHGW()'''
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    result = 0
    # list_screenshot = ['not changed'] * 6
    testcase_name = "test_TR069_EnableAccesspoint"
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()
    list_accesspointvalue = [1, 1, 1, 1, 1, 1]
    list_advertisementvalue = [1, 1, 1, 1, 1, 1]
    list_maxassodevice = [10, 10, 10, 10, 10, 10]
    output = ''

    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.skip(reason="Executing Twice")
    def test_TR069_EnableAccesspoint(self):
        try:
            self.lp = Test_LoginPage(self.driver)
            self.acs = ACS_MainMenu(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av = ACS_Advanced_View(self.driver)

            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            time.sleep(2)
            self.av.clickTableHeadWifi()
            self.av.clickTableDataAccessPoint()
            time.sleep(2)

            for i in range(1, 7):
                if str(i) not in self.omitssid:
                    self.logger.info(
                        "************** Updating Wifi AccessPoint " + str(i) + " ****************")
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

        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
