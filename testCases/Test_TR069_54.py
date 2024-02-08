import traceback

import pytest
from selenium import common

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_54:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    no_rows = 1
    result = 0
    testcase_name = "test_TR069_54"
    rownum_Start = 57
    rownum_Finish = 57
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(54)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_54(self, setup):
        try:
            self.driver = setup
            self.logger.info("***************** " + self.testcase_name + " Started *****************")
            self.lp = Test_LoginPage(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.av = ACS_Advanced_View(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableDataManagementServer()
            str_URL = self.av.getConnectionRequestURL()
            print(str_URL)
            a, b = 0, 0
            for i in range(len(str_URL)):
                if str_URL[i] == '[':
                    a = i
                if str_URL[i] == ']':
                    b = i
                    break

            if str_URL[a+1:b].count(':') > 1:
                self.list_output.append('PASS')
            else:
                self.list_output.append('FAIL')
                print('Address not in IPv6 Format')

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
                for i in range(self.no_rows - len(self.list_output)):
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

    def test_TR069_54_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
