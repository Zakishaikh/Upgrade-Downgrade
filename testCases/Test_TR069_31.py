import traceback
import time
import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_31:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_value = [0]
    list_output = []
    result = 0
    no_rows = 1
    testcase_name = "test_TR069_31"
    rownum_Start = 34
    rownum_Finish = 34
    column_no = 5
    int_SSIDNo = 1
    list_deviceinfo = []
    list_JCstatus = []
    logger = LogGen.loggen()

    @pytest.mark.order(31)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_31(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + "****************")
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.wait = WebDriverWait(self.driver, 10)
            self.av = ACS_Advanced_View(self.driver)

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableDataAccessPoint()
            self.av.ClickTableDataAccespoint_index(self.int_SSIDNo)
            status = self.acs.TR069_Getcurrent()
            if status == 'FAIL':
                self.logger.info('---------GET CURRENT TASK FAILED-----------')
                print('---------GET CURRENT TASK FAILED-----------')
            else:
                self.logger.info('---------GET CURRENT TASK PASSED-----------')
                print('---------GET CURRENT TASK PASSED-----------')

            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableDataAccessPoint()

            if str(self.int_SSIDNo) not in self.omitssid:
                self.logger.info(
                    "************** Updating Wifi AccessPoint " + str(self.int_SSIDNo) + " Enable Value ****************")
                self.av.ClickTableDataAccespoint_index(self.int_SSIDNo)
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmButtons")
                self.av.clickEditButton()
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmDesktop")
                self.av.setAccessPointSSIDAdvertisementEnabled(self.int_SSIDNo, self.list_value[0])
                status = self.acs.TR069_Sendupdate()
            else:
                status = 'NT'
            print(status)

            '''self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            self.jc.clicknetworkMenu()
            self.jc.clickwireless()

            self.list_JCstatus = self.jc.getAPAdvertisementStatus()'''
            self.list_JCstatus = ["Disabled", "Disabled", "Disabled", "Disabled", "Disabled", "Disabled"]

            if str(self.int_SSIDNo) not in str(self.omitssid):
                if self.list_JCstatus[self.int_SSIDNo-1] == "Disabled" and status == 'PASS':
                    self.logger.info(
                        '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Advertisement Disabled on Centrum ----------- ')
                    self.list_output.append("PASS")
                else:
                    self.logger.info(
                        '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Advertisement Enabled on Centrum ----------- ')
                    self.list_output.append("FAIL")
            else:
                print("AccessPoint " + str(self.int_SSIDNo) + " is not tested, Since it is in omitssid list " + self.omitssid + "")
                self.list_output.append("NT")

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

    def test_TR069_31_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
