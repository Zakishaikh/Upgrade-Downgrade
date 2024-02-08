
import time
import traceback
import pytest
from selenium import common
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_Device_Info import ACS_Device_Info
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_07:
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()
    factory_pass = ReadTestData.getFactoryResetPassword()

    rownum_Start = 8
    rownum_Finish = 8
    column_no = 5
    testcase_name = "test_TR069_ACS_07"
    no_rows = 1
    result = 0
    logger = LogGen.loggen()
    i = 1
    list_devicehistory = []
    list_output = []
    list_screenshot = []
    list_deviceinfo = []
    list_row = []

    @pytest.mark.order(7)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_07(self, setup):
        try:
            self.logger.info(" *************************" + self.testcase_name + " *************************")
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.av = ACS_Advanced_View(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.di = ACS_Device_Info(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")

            self.di.clickStopTrace()
            self.di.clickStartTrace()

            for i in range(10):
                self.logger.info("************** " + str(i + 1) + " Started ****************")
                self.di.clickFactoryReset()

                status = self.acs.TR069_TaskStatus()
                print(status)
                if status == 'PASS':
                    print('-----Factory Reset sent waiting 300 seconds-----')
                    self.logger.info(" ************************* Factory Reset sent waiting 300 seconds  *************************")
                    time.sleep(300)

                self.lp.ACS_LoginPage()

                self.list_devicehistory = self.av.getDeviceHistory()

                print(self.list_devicehistory)
                if '1 BOOT' in self.list_devicehistory and '0 BOOTSTRAP' in self.list_devicehistory:
                    self.logger.info(
                        " ************************* Factory Reset Passed  *************************")
                    self.list_output.append('PASS')
                    self.lp.JioCentrum_FactoryResetLogin()
                    self.lp.ACS_LoginPage()
                    try:
                        self.driver.switch_to.default_content()
                        self.av.clickTableDataAdvanced()
                        self.driver.switch_to.frame("frmButtons")
                        self.av.clickSaveParameterButton()
                        self.logger.info(
                            " ************************* Save Parameter Clicked  *************************")
                    except (common.exceptions.NoSuchElementException, common.exceptions.TimeoutException):
                        self.logger.info(
                            " ************************* Save Parameter Clicked Failed  *************************")
                    time.sleep(3)
                else:
                    self.logger.info(
                        " ************************* Factory Reset Failed  *************************")
                    self.list_output.append('FAIL')

                self.driver.switch_to.default_content()
                self.di.click_TableDataDeviceInfo()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.di.clickStopTrace()

            self.lp.JioCentrum_FactoryResetLogin()

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
                print(self.list_output)
                self.list_output.clear()
                for i in range(self.no_rows):
                    self.list_output.append('FAIL')
                    self.list_screenshot.append("FAIL")
                list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
                list_output.append(self.list_output)
                for i in range(4 - len(self.list_deviceinfo)):
                    self.list_deviceinfo.append(0)
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

    def test_TR069_07_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
