import traceback

import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from testCases.Test_Sanity_GetCurrent import Test_Sanity_GetCurrent
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_83:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    list_StaticRoute = []
    no_rows = 1
    result = 0
    testcase_name = "test_TR069_83"
    rownum_Start = 86
    rownum_Finish = 86
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(83)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_83(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.gc = Test_Sanity_GetCurrent(self.driver)
            self.wait = WebDriverWait(self.driver, 10)
            self.acs = ACS_MainMenu(self.driver)
            self.av = ACS_Advanced_View(self.driver)
            self.logger.info("************** " + self.testcase_name + " Started ****************")

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableheadRouting()
            self.av.clickTableheadRoutingRouter()
            self.av.clickTableheadRoutingRouter1()
            self.av.clickTableheadRoutingRouter1IPv4Forwarding()
            for i in range(1, 5):
                self.av.clickTabledataRoutingRouter1IPv4ForwardingIndex(i)
                status = self.acs.TR069_Getcurrent()
                print('Get Current for IPv4Forwarding ' + str(i) + ' Status on ACS = ' + status)
                self.logger.info('Get Current for IPv4Forwarding ' + str(i) + ' Status on ACS = ' + status)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableheadRouting()
            self.av.clickTableheadRoutingRouter()
            self.av.clickTableheadRoutingRouter1()
            self.av.clickTableheadRoutingRouter1IPv4Forwarding()
            for i in range(1, 5):
                self.av.clickTabledataRoutingRouter1IPv4ForwardingIndex(i)
                self.list_StaticRoute.append(self.av.getRoutingRouter1IPv4ForwardingIndexStaticRoute(i))
            print('IPv4Forwarding StaticRoute = ' + str(self.list_StaticRoute))
            self.logger.info('IPv4Forwarding StaticRoute = ' + str(self.list_StaticRoute))

            if '0' in self.list_StaticRoute or 0 in self.list_StaticRoute:
                list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
                list_output.append(['FAIL'])
            else:
                list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
                list_output.append(['PASS'])
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
                self.logger.info("************** " + self.testcase_name + " Passed ****************")
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

    def test_TR069_83_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
