import subprocess
import time
import traceback

import pytest
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from testCases.Test_TR069_EnableAccesspoint import Test_TR069_EnableAccesspoint
from utilities.ReadTestData import ReadTestData, Excel_Env, SSIDConfigGet
from utilities.WriteTestData import SSIDConfigSet
from utilities.commonmethod import commonmethod
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_19_24:

    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    ssid_JioCentrum_list = []
    ssid_acs_list = []
    list_output = []
    no_rows = 6
    result = 0
    list_screenshot = ['not changed'] * 6
    testcase_name = "test_TR069_19_24"
    rownum_Start = 22
    rownum_Finish = 27
    column_no = 5
    list_deviceinfo = []
    list_task_status = []
    logger = LogGen.loggen()

    # @pytest.mark.order(19)
    # @pytest.mark.device
    # @pytest.mark.complete
    def test_TR069_19_24(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + "****************")
            deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                          capture_output=True)
            print(deviceStatus)
            # print(" Device connected for adb")
            deviceStatus = subprocess.run("adb reboot ", shell=True, stdin=subprocess.PIPE,
                                          capture_output=True)
            print(deviceStatus)
            self.driver = setup
            self.ea = Test_TR069_EnableAccesspoint(self.driver)
            self.ea.test_TR069_EnableAccesspoint()
            self.lp = Test_LoginPage(self.driver)
            self.lp.ACS_LoginPage()
            self.wait = WebDriverWait(self.driver, 10)
            # time.sleep(2)
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            # time.sleep(2)
            # time.sleep(4)
            self.av = ACS_Advanced_View(self.driver)
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            # time.sleep(2)
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()
            self.av.clickTableHeadSSID()
            # self.av.clickSSID()
            for i in range(1, self.no_rows + 1):
                if str(i) not in self.omitssid:
                    self.logger.info(
                        "************** Updating Wifi SSID " + str(i) + " Name ****************")
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.frame("frmButtons")
                    self.av.clickEditButton()
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.frame("frmDesktop")

                    self.av.clickTableDataSSID_index(i)

                    dt = datetime.now()
                    minute = str(dt.minute)
                    second = str(dt.second)
                    SSID = "Jio@" + str(minute) + str(second)
                    time.sleep(2)
                    self.av.setSSIDName(i, SSID)

                    self.driver.save_screenshot(".\\Screenshots\\" + self.testcase_name + str(i) + ".png")
                    self.list_task_status.append(self.acs.TR069_Sendupdate())
                    # time.sleep(2)
                else:
                    self.av.clickTableDataSSID_index(i)
                    element_x = self.wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//span[@tiptext='Device.WiFi.SSID." + str(i) + ".SSID']/../../td[2]")))
                    SSID = str(element_x.get_attribute('innerHTML'))
                    self.list_task_status.append('NT')
                self.ssid_acs_list.append(SSID)

            print("Updated SSID List " + str(self.ssid_acs_list))
            print(self.list_task_status)

            self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            self.jc.clicknetworkMenu()
            # time.sleep(3)
            self.jc.clickwireless()
            # time.sleep(3)
            self.jc.profilebtn()
            self.ssid_JioCentrum_list = self.jc.getSSIDNames()
            print(self.ssid_acs_list)
            print(self.ssid_JioCentrum_list)
            for i in range(1, len(self.ssid_acs_list)+1):
                if str(i) not in self.omitssid:
                    if self.ssid_acs_list[i-1] == self.ssid_JioCentrum_list[i-1] and self.list_task_status[i-1] == 'PASS':
                        client_status = self.client_ssid_connect_19_24(i)
                        if client_status == 'PASS':
                            self.logger.info('----------- Accesspoint ' + str(i) + ' Connected on device ----------- ')
                            print("SSID" + str(i) + "Connection Passed")
                            self.list_output.append("PASS")
                        else:
                            print("SSID" + str(i) + "Connection Failed")
                            self.logger.info('----------- Accesspoint ' + str(i) + ' Connection Failed on device ----------- ')
                            self.list_output.append("FAIL")
                    else:
                        print("SSID" + str(i) + " Failed")
                        self.list_output.append("FAIL")
                        # self.list_deviceinfo
                else:
                    print("AccessPoint " + str(i) + "is not tested, Since it is in omitssid list " + self.omitssid + "")
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
                    self.list_screenshot.append("FAIL")
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

    def test_TR069_19_24_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name,
                                  self.sheet_name, list_output, list_row, list_deviceinfo)

    def client_ssid_connect_19_24(self, j):
        list_pass = SSIDConfigGet.getSSIDPASSWORD()
        self.logger.info('----------- Trying to Connect Accesspoint ' + str(j) + ' on device ----------- ')
        x = commonmethod.get_wifistatus(self.ssid_JioCentrum_list[j-1], list_pass[j-1], r=0)
        if x == 'Connected':
            self.logger.info('SSID ' + str(j) + ' Name = ' + self.ssid_JioCentrum_list[j-1])
            SSIDConfigSet.setSSIDNAME(j, self.ssid_JioCentrum_list[j-1])
            status = commonmethod.pingcheck()
            if status == 'PASS':
                return 'PASS'
            else:
                return 'FAIL'
        else:
            return 'FAIL'