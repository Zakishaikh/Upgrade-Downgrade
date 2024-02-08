import subprocess
import traceback

import pytest
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData, SSIDConfigGet
from utilities.commonmethod import commonmethod
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_25_30:
    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    list_value = [1, 1, 1, 1, 1, 1]
    list_output = []
    no_rows = 6
    result = 0
    list_screenshot = ['not changed'] * 6
    testcase_name = "test_TR069_25_30"
    rownum_Start = 28
    rownum_Finish = 33
    column_no = 5
    list_JCstatus = []
    # list_deviceinfo=[]
    list_deviceinfo = []
    list_task_status = []
    logger = LogGen.loggen()

    # @pytest.mark.order(25)
    # @pytest.mark.device
    # @pytest.mark.complete
    def test_TR069_ACS_25_30(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + "****************")
            deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                          capture_output=True)
            print(deviceStatus)
            deviceStatus = subprocess.run("adb reboot ", shell=True, stdin=subprocess.PIPE,
                                          capture_output=True)
            print(deviceStatus)
            self.driver = setup
            self.lp = Test_LoginPage(self.driver)
            self.lp.ACS_LoginPage()
            self.wait = WebDriverWait(self.driver, 10)
            # time.sleep(2)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()

            # time.sleep(2)
            self.av = ACS_Advanced_View(self.driver)
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableDataAccessPoint()

            for i in range(1, self.no_rows + 1):
                if str(i) not in self.omitssid:
                    self.logger.info(
                        "************** Updating Wifi AccessPoint " + str(i) + " Enable Value ****************")
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.frame("frmButtons")
                    self.av.clickEditButton()
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.frame("frmDesktop")

                    self.av.ClickTableDataAccespoint_index(i)
                    # time.sleep(2)
                    self.av.setAccessPointSSIDAdvertisementEnabled(i, self.list_value[i - 1])
                    # time.sleep(2)
                    self.list_task_status.append(self.acs.TR069_Sendupdate())
                else:
                    self.list_task_status.append('NT')

            print(self.list_task_status)
            # status = self.acs.TR069_Sendupdate()

            self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            self.jc.clicknetworkMenu()
            # time.sleep(2)
            self.jc.clickwireless()
            # time.sleep(3)
            # self.jc.clicktable_accesspoint()
            self.list_JCstatus = self.jc.getAPAdvertisementStatus()
            # print('Length = ' + str(len(self.list_JCstatus)))

            for j in range(1, len(self.list_JCstatus) + 1):
                if str(j) not in str(self.omitssid):
                    if self.list_JCstatus[j - 1] == "Enabled":
                        self.logger.info(
                            '----------- Accesspoint Advertisement ' + str(j) + ' Enabled on Centrum ----------- ')
                        client_status = self.client_ssid_connect_25_30(j)
                        if client_status == 'PASS':
                            self.logger.info('----------- Accesspoint ' + str(j) + ' Connected on device ----------- ')
                            self.list_output.append("PASS")
                        else:
                            self.logger.info(
                                '----------- Accesspoint ' + str(j) + ' Connection Failed on device ----------- ')
                            self.list_output.append("FAIL")
                    else:
                        self.logger.info(
                            '----------- Accesspoint Advertisement ' + str(j) + ' Disabled on Centrum ----------- ')
                        self.list_output.append("FAIL")
                else:
                    print(
                        "AccessPoint " + str(j) + " is not tested, Since it is in omitssid list " + self.omitssid + "")
                    self.list_output.append("NT")

            print(self.list_output)
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
                    self.list_screenshot.append("fail")
                    list_row.append([self.rownum_Start, self.rownum_Finish, self.column_no])
                    list_output.append(self.list_output)
                    '''for i in range(4 - len(self.list_deviceinfo)):
                    self.list_deviceinfo.append(0)'''
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

    def test_TR069_88_93_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)

    def client_ssid_connect_25_30(self, j):
        list_name = SSIDConfigGet.getSSIDNAME()
        list_pass = SSIDConfigGet.getSSIDPASSWORD()
        self.logger.info('----------- Trying to Connect Accesspoint ' + str(j) + ' on device ----------- ')
        x = commonmethod.get_wifistatus(list_name[j - 1], list_pass[j - 1], r=0)
        if x == 'Connected':
            commonmethod.pingcheck()
            return 'PASS'
        else:
            return 'FAIL'
