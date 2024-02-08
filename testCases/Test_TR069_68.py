import pytest
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from utilities.customLogger import LogGen
from utilities.updateExcel import updateExcel
from utilities.ReadTestData import ReadTestData
from utilities.ReadTestData import Excel_Env
from utilities.outputVariables import *
from testCases.Test_LoginPage import Test_LoginPage
from testCases.Test_DeviceInfo import Test_DeviceInfo
import traceback
from selenium import common


class Test_TR069_68:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    no_rows = 1
    result = 0
    list_PeriodicInformInterval = ['60', '65']
    list_url = ['http://iotacs.jioconnect.com:8080/ftacs-digest/ACS']
    testcase_name = "test_TR069_68"
    rownum_Start = 71
    rownum_Finish = 71
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(68)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_68(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.logger.info("***************** " + self.testcase_name + " Started *****************")
            self.acs = ACS_MainMenu(self.driver)
            self.av = ACS_Advanced_View(self.driver)

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
            self.list_url.append("https://" + str_ipv4 + "/ftacs-digest/ACS")
            print(self.list_url)
            self.av.clickTableDataManagementServer()

            str_PeriodicInformInterval = self.av.getPeriodicInformInterval()
            str_URL = self.av.getManagementServerURL()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")

            if str_URL == self.list_url[0]:
                self.av.setManagementServerURL(self.list_url[1])
            else:
                self.av.setManagementServerURL(self.list_url[0])

            if str_PeriodicInformInterval == self.list_PeriodicInformInterval[0]:
                self.av.setPeriodicInformInterval(self.list_PeriodicInformInterval[1])
            else:
                self.av.setPeriodicInformInterval(self.list_PeriodicInformInterval[0])

            status = self.acs.TR069_Sendupdate()

            if status == 'PASS':
                self.list_output.append('PASS')

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

    def test_TR069_68_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
