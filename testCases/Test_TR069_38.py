import traceback

import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_38:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    str_value = '8.8.8.8'
    list_output = []
    list_screenshot = []
    no_rows = 1
    result = 0
    testcase_name = "test_TR069_38"
    rownum_Start = 41
    rownum_Finish = 41
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(38)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_38(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.logger.info("***************** " + self.testcase_name + " Started *****************")
            self.wait = WebDriverWait(self.driver, 10)
            self.lp.ACS_LoginPage()

            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()

            self.av = ACS_Advanced_View(self.driver)
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableheadDNS()

            self.av.clickTableheadDNSClient()
            self.av.clickTableheadDNSClientServer()
            self.av.clickTabledataDNSClientServerServer1()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            self.logger.info("************** Updating DNS SERVER value from DNS SERVER 1 ****************")
            print("************** Updating DNS SERVER value from DNS SERVER 1 ****************")

            self.av.setDNSServer1DNSSERVER(self.str_value)

            status = self.acs.TR069_Sendupdate()
            if status == 'PASS':
                self.list_output.append('PASS')
            else:
                self.list_output.append('FAIL')

            list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
            list_output.append(self.list_output)
        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
        else:
            self.result = 1
            if 'FAIL' in self.list_output:
                self.logger.error("************** " + self.testcase_name + " Failed ****************")
                self.driver.save_screenshot(".\\Screenshots\\" + self.testcase_name + ".png")
                self.driver.close()
                assert False
            else:
                assert True
                self.driver.close()
                self.logger.error("************** " + self.testcase_name + " Passed ****************")
        finally:
            if self.result == 0:
                for i in range(self.no_rows-len(self.list_output)):
                    self.list_output.append('FAIL')
                    self.list_screenshot.append("FAIL")
                list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
                list_output.append(self.list_output)
                self.logger.error("************** " + self.testcase_name + " Failed ****************")
                try:
                    self.driver.close()
                except AttributeError:
                    print(traceback.format_exc())
                    print("Driver error")
                except common.exceptions.WebDriverException:
                    print(traceback.format_exc())
                    print("Web driver error")
                finally:
                    assert False

    def test_TR069_38_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
