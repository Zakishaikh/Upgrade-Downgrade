import time
import traceback

import pytest
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


class Test_TR069_53:
    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_value = [1, 0]
    list_output = []
    list_screenshot = []
    no_rows = 1
    result = 0
    # list_screenshot = ['not changed'] * 6
    testcase_name = "test_TR069_53"
    rownum_Start = 56
    rownum_Finish = 56
    column_no = 5
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.order(53)
    @pytest.mark.sanity
    @pytest.mark.complete
    def test_TR069_53(self, setup):
        try:
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.logger.info("***************** " + self.testcase_name + " Started *****************")
            self.wait = WebDriverWait(self.driver, 10)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.av = ACS_Advanced_View(self.driver)
            self.gc = Test_Sanity_GetCurrent(self.driver)

            self.gc.test_Sanity_GetCurrent()

            self.lp.ACS_LoginPage()

            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableDataAccessPoint()
            self.av.ClickTableDataAccespoint_index(2)
            str_maxdevice_x = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//span[@tiptext='Device.WiFi.AccessPoint.2.SSIDAdvertisementEnabled']/../../td[2]")))
            str_maxdevice = str_maxdevice_x.get_attribute('innerHTML')
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")
            self.logger.info("************** Changing SSID Advertisement for AP 2 ****************")
            if str_maxdevice == str(self.list_value[0]):
                self.av.setAccessPointSSIDAdvertisementEnabled(2, self.list_value[1])
            else:
                self.av.setAccessPointSSIDAdvertisementEnabled(2, self.list_value[0])

            status = self.acs.TR069_Sendupdate()
            if status == 'PASS':
                self.list_output.append('PASS')
            else:
                self.list_output.append('FAIL')

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickSaveParameterButton()
            time.sleep(3)
            self.logger.info("************** Save Parameter Clicked ****************")

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

    def test_TR069_53_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
