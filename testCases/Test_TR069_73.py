import pytest
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from pageObjects.ACS_FileUpload import ACS_FileUpload
from utilities.customLogger import LogGen
from utilities.updateExcel import updateExcel
from utilities.outputVariables import *
from utilities.ReadTestData import Excel_Env
import traceback
from selenium import common


class Test_TR069_73:
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()
    list_output = []
    rownum_Start = 76
    rownum_Finish = 76
    column_no = 5
    result = 0
    no_rows = 1
    testcase_name = "test_TR069_73"
    logger = LogGen.loggen()
    str_destinationurl = 'ftp://10.64.218.26/'
    str_username = 'ftpuser'
    str_password = 'Jio@1234'
    str_filetype = 'Vendor Log File <i>'
    list_screenshot = []
    list_deviceinfo = []

    @pytest.mark.order(73)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_73(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.fu = ACS_FileUpload(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.logger.info("***************** " + self.testcase_name + " Started *****************")

            self.logger.info("***************** Case 1 *****************")

            self.lp.ACS_LoginPage()

            self.driver.switch_to.default_content()
            self.fu.clickTabledataFileUpload()

            try:
                # time.sleep(4)
                self.driver.switch_to.frame("frmButtons")
                self.fu.clickButtonAdd()
            except common.exceptions.NoSuchElementException:
                pass

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            self.fu.selectFiletypeVendorLogFileInstance()

            self.fu.clickManualURL()
            self.fu.selectInstance1()
            self.fu.setDestinationURL(self.str_destinationurl)
            self.fu.setUsername(self.str_username)
            self.fu.setPassword(self.str_password)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.fu.clickButtonSendUpdate()
            self.fu.clickAlert()

            status = self.acs.TR069_TaskStatus()
            print('***************** Case 1 Status = ' + status + ' *****************')
            self.logger.info('***************** Case 1 Status = ' + status + ' *****************')
            if status == 'PASS':
                self.list_output.append('PASS')
            else:
                self.list_output.append('FAIL')

            ''' self.lp.ACS_LoginPage()
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.driver.switch_to.default_content()
            self.fu = ACS_FileUpload(self.driver)
            self.fu.clickTabledataFileUpload()
            status = self.fu.getFileUploadStatus(self.str_filetype)
            print('***************** Case 1 Status = ' + status + ' *****************')
            self.logger.info('***************** Case 1 Status = ' + status + ' *****************')
            if status == 'PASS':
                self.list_output.append('PASS')
            else:
                self.list_output.append('FAIL')'''

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
                self.logger.info("************** " + self.testcase_name + " Passed ****************")
        finally:
            if self.result == 0:
                self.list_output.clear()
                self.list_screenshot.clear()
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

    def test_TR069_73_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
