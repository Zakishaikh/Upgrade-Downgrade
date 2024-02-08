import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.ACS_Device_Info import ACS_Device_Info
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from pageObjects.ACS_FileDownload import ACS_File_Download
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from utilities.customLogger import LogGen
from utilities.updateExcel import updateExcel
from utilities.outputVariables import *
from utilities.ReadTestData import ReadTestData, Excel_Env
from utilities.WriteTestData import SSIDConfigSet
import traceback
from selenium.webdriver.support.ui import Select
from selenium import common


class Test_TR069_57:

    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()
    list_output = []
    rownum_Start = 60
    rownum_Finish = 60
    column_no = 5
    result = 0
    no_rows = 1
    testcase_name = "test_TR069_57"
    logger = LogGen.loggen()

    list_screenshot = []
    list_deviceinfo = []

    @pytest.mark.order(57)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_57(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + " Started ****************")
            self.driver = setup
            self.av = ACS_Advanced_View(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.lp = Test_LoginPage(self.driver)
            self.fd = ACS_File_Download(self.driver)
            self.di = ACS_Device_Info(self.driver)

            self.lp.ACS_LoginPage()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            str_CurrentSoftware = self.di.getTextSoftwareVersion()
            print('Current Software Version = ' + str_CurrentSoftware)
            self.logger.info('************* Current Software Version = ' + str_CurrentSoftware + ' *************')

            self.driver.switch_to.default_content()
            self.fd.clickTabledataFileDownload()

            try:
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmButtons")
                self.fd.clickButtonAdd()
            except common.exceptions.NoSuchElementException:
                pass

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            self.fd.clickDropdownFiletypeFirmwareImage()
            self.fd.clickRadiobuttonFromList()

            str_LatestSoftware = self.fd.getLatestSoftwareVersionName()
            print('Latest Software Version = ' + str_LatestSoftware)
            self.logger.info('************* Latest Software Version = ' + str_LatestSoftware + ' *************')

            if str_LatestSoftware == str_CurrentSoftware:
                print('Selected second option')
                self.fd.clickDropdownFilenameSecondOption()
            else:
                print('Selected first option')
                self.fd.clickDropdownFilenameFirstOption()

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.fd.clickButtonSendUpdate()
            self.av.clickAlert()
            self.driver.switch_to.default_content()
            self.acs.modelpopup()

            status = self.acs.TR069_TaskStatus()
            print(status)
            if status == 'PASS':
                self.logger.info(" ************************* Firmware Update sent waiting 180 seconds *************************")
                print('-----Firmware Update sent waiting 180 seconds-----')
                time.sleep(180)

            self.lp.ACS_LoginPage()
            self.list_devicehistory = self.av.getDeviceHistory()

            # print(self.list_devicehistory)
            if '1 BOOT' in self.list_devicehistory and '4 VALUE CHANGE' in self.list_devicehistory and 'M Download' in self.list_devicehistory and '7 TRANSFER COMPLETE' in self.list_devicehistory:
                self.list_output.append('PASS')
                self.logger.info(" ************************* Firmware Update Passed *************************")
            else:
                self.list_output.append('FAIL')
                self.logger.info(" ************************* Firmware Update Failed *************************")

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

    def test_TR069_57_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
