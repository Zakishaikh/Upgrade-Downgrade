import traceback

import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen


class Test_Sanity_GetCurrent:

    omitssid = str(ReadTestData.getomitssid())

    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_value = []
    list_output = []
    list_screenshot = []
    result = 0
    # list_screenshot = ['not changed'] * 6
    testcase_name = "test_Sanity_GetCurrent"
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.skip(reason="Executing Twice")
    def test_Sanity_GetCurrent(self):
        try:
            self.lp = Test_LoginPage(self.driver)
            self.wait = WebDriverWait(self.driver, 10)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.av = ACS_Advanced_View(self.driver)

            self.lp.ACS_LoginPage()

            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTabledataDevice()

            status = self.acs.TR069_Getcurrent()

            if status == 'FAIL':
                self.logger.info('---------GET CURRENT TASK FAILED-----------')
                print('---------GET CURRENT TASK FAILED-----------')
                self.list_output.append('FAIL')
            else:
                self.logger.info('---------GET CURRENT TASK PASSED-----------')
                print('---------GET CURRENT TASK PASSED-----------')
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
