import traceback

import pytest
from selenium import common

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from testCases.Test_Sanity_GetCurrent import Test_Sanity_GetCurrent
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_95:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_url = []
    list_output = []
    list_screenshot = []
    no_rows = 1
    result = 0
    testcase_name = "test_TR069_95"
    rownum_Start = 98
    rownum_Finish = 98
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(95)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_95(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.av = ACS_Advanced_View(self.driver)
            self.gc = Test_Sanity_GetCurrent(self.driver)

            self.gc.test_Sanity_GetCurrent()

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableheadIP()
            self.av.clickTableheadIPInterface()
            self.av.clickTableheadIPInterface1()
            self.av.clickTableheadIPInterface1IPv4()
            self.av.clickTabledataIPInterface1IPv41()
            str_ipv4 = str(self.av.getTextdataIPInterface1IPv41())
            print(str_ipv4)
            self.av.clickTableheadIPInterface1IPv6()
            self.av.clickTabledataIPInterface1IPv61()
            str_ipv6 = str(self.av.getTextdataIPInterface1IPv61())
            print(str_ipv6)

            self.av.clickTableDataManagementServer()
            str_URL = self.av.getManagementServerURL()
            print(str_URL)

            a, b = 0, 0
            for i in range(len(str_URL)):
                if str_URL[i] == '[':
                    a = i
                if str_URL[i] == ']':
                    b = i
                    break

            if str_URL[a+1:b].count(':') > 1:
                self.list_url.append("https://" + str_ipv4 + "/ftacs-digest/ACS")
                self.list_url.append("https://" + str_ipv6 + "/ftacs-digest/ACS")
            else:
                self.list_url.append("https://" + str_ipv6 + "/ftacs-digest/ACS")
                self.list_url.append("https://" + str_ipv4 + "/ftacs-digest/ACS")

            for i in range(2):
                self.logger.info('*************** Scenario ' + str(i+1) + ' ***************')
                self.lp.ACS_LoginPage()
                self.driver.switch_to.default_content()
                self.av.clickTableDataAdvanced()
                self.av.clickTableDataManagementServer()
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmButtons")
                self.av.clickEditButton()
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmDesktop")
                self.av.setManagementServerURL(self.list_url[i])
                self.logger.info('*************** New URL = ' + self.list_url[i] + ' ***************')
                print('*************** New URL = ' + self.list_url[i] + ' ***************')
                status = self.acs.TR069_Sendupdate()
                if status == 'PASS':
                    self.list_output.append('PASS')
                    self.logger.info('*************** Scenario ' + str(i + 1) + ' PASSED ***************')
                else:
                    self.logger.info('*************** Scenario ' + str(i + 1) + ' FAILED ***************')
                    self.list_output.append('FAIL')

            print(self.list_output)
            if 'FAIL' in self.list_output:
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

    def test_TR069_95_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
