import time
import traceback

import pytest
from selenium import common

from pageObjects.ACS_CustomRPC import ACS_CustomRPC
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_70:

    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()
    list_output = []
    rownum_Start = 73
    rownum_Finish = 73
    column_no = 5
    result = 0
    no_rows = 1
    testcase_name = "test_TR069_70"
    logger = LogGen.loggen()

    list_screenshot = []
    list_deviceinfo = []

    @pytest.mark.order(70)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_70(self, setup):
        try:
            self.driver = setup
            self.logger.info("***************** " + self.testcase_name + " Started *****************")
            self.lp = Test_LoginPage(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.fd = ACS_CustomRPC(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.fd.clickCustomRPC()

            try:
                self.driver.switch_to.frame("frmButtons")
                self.fd.clickButtonAdd()
            except common.exceptions.NoSuchElementException:
                pass

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            self.fd.clickCustomRPCSelectUpload()

            text = '''<cwmp:Upload xmlns:cwmp="urn:dslforum-org:cwmp-1-0">
                        <CommandKey></CommandKey>
                        <FileType>3 Vendor Configuration File 1</FileType>
                        <URL>ftp://10.64.218.26/test70</URL>
                        <Username>FTPuser</Username>
                        <Password>FTPpass12</Password>
                        <DelaySeconds>0</DelaySeconds>
                      </cwmp:Upload>'''

            self.fd.setCustomRPCTextrequest(text)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.fd.clickButtonSendUpdate()
            self.fd.clickAlert()

            status = self.acs.TR069_TaskStatus()
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
                self.list_output.clear()
                self.list_screenshot.clear()
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

    def test_TR069_70_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
