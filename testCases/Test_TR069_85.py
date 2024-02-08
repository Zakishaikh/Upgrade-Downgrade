import traceback
import time
import pytest
from selenium import common
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
from pageObjects.ACS_Device_Info import ACS_Device_Info
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless


class Test_TR069_85:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_output = []
    list_screenshot = []
    list_Enable = []
    no_rows = 1
    result = 0
    int_Enable = 0
    str_search = 'Basic'
    testcase_name = "test_TR069_85"
    rownum_Start = 88
    rownum_Finish = 88
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(85)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_85(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.gc = Test_Sanity_GetCurrent(self.driver)
            self.wait = WebDriverWait(self.driver, 10)
            actions = ActionChains(self.driver)
            self.acs = ACS_MainMenu(self.driver)
            self.av = ACS_Advanced_View(self.driver)
            self.di = ACS_Device_Info(self.driver)
            self.logger.info("************** " + self.testcase_name + " Started ****************")

            self.lp.ACS_LoginPage()
            self.di.clickFactoryReset()
            status = self.acs.TR069_TaskStatus()
            print(status)
            self.logger.info("************************* waiting 300 seconds *************************")
            print('-----Factory Reset sent waiting 300 seconds-----')
            time.sleep(300)
            self.lp.ACS_LoginPage()
            self.list_devicehistory = self.av.getDeviceHistory()
            print(self.list_devicehistory)
            if '1 BOOT' in self.list_devicehistory and '0 BOOTSTRAP' in self.list_devicehistory:
                self.logger.info("************************* Factory Reset Passed *************************")
                self.list_output.append('PASS')
                self.lp.JioCentrum_FactoryResetLogin()
            else:
                self.logger.info(
                    " ************************* Factory Reset Failed  *************************")
                self.list_output.append('FAIL')
            self.lp.JioCentrum_FactoryResetLogin()

            self.gc.test_Sanity_GetCurrent()
            self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableDataRadio()
            self.av.clickTableDataRadio_index(1)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")

            self.logger.info(
                "************** Updating Wifi Radio 1 AutoChannel Enable Value ****************")
            self.av.setRadioAutoChannelEnable(1, self.int_Enable)
            status = self.acs.TR069_Sendupdate()
            print('Radio AutoChannel Enable Task Status = ' + status)
            self.logger.info('Radio AutoChannel Enable Task Status = ' + status)

            self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            self.jc.setSearch(self.str_search)
            time.sleep(2)
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(2)
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(2)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(5)
            str_mode = self.jc.getBasicConfigurationMode()
            if str_mode == 'ng':
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

    def test_TR069_85_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
