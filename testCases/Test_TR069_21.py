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


class Test_TR069_21:
    omitssid = str(ReadTestData.getomitssid())
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    ssid_JioCentrum_list = []
    list_output = []
    no_rows = 1
    result = 0
    testcase_name = "test_TR069_21"
    rownum_Start = 24
    rownum_Finish = 24
    column_no = 5
    int_SSIDNo = 3
    list_deviceinfo = []
    logger = LogGen.loggen()

    @pytest.mark.order(21)
    @pytest.mark.device
    @pytest.mark.complete
    def test_TR069_21(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + "****************")
            deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                          capture_output=True)
            print(deviceStatus)
            self.driver = setup
            self.ea = Test_TR069_EnableAccesspoint(self.driver)
            self.lp = Test_LoginPage(self.driver)
            self.wait = WebDriverWait(self.driver, 10)
            self.acs = ACS_MainMenu(self.driver)
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
            self.av.ClickTableDataAccespoint_index(self.int_SSIDNo)
            str_EnableValue = self.av.getAccessPointEnable(self.int_SSIDNo)
            str_AdvertisementValue = self.av.getAccessPointSSIDAdvertisementEnabled(self.int_SSIDNo)

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            self.av.clickEditButton()
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmDesktop")

            if str_EnableValue == '0':
                self.logger.info('---------AccessPoint Enable = 0 changing it to 1-----------')
                print('---------AccessPoint Enable = 0 changing it to 1-----------')
                self.av.setAccessPointEnable(self.int_SSIDNo, '1')
            else:
                self.logger.info('---------AccessPoint Enable = 1-----------')
                print('---------AccessPoint Enable = 1-----------')
            if str_AdvertisementValue == '0':
                self.logger.info('---------AccessPoint SSIDAdvertisement Enable = 0 changing it to 1-----------')
                print('---------AccessPoint SSIDAdvertisement Enable = 0 changing it to 1-----------')
                self.av.setAccessPointSSIDAdvertisementEnabled(self.int_SSIDNo, '1')
            else:
                self.logger.info('---------AccessPoint SSIDAdvertisement Enable = 1-----------')
                print('---------AccessPoint SSIDAdvertisement Enable = 1-----------')

            '''self.lp.ACS_LoginPage()
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadWifi()'''
            self.av.clickTableHeadSSID()

            if str(self.int_SSIDNo) not in self.omitssid:
                self.logger.info(
                    "************** Updating Wifi SSID " + str(self.int_SSIDNo) + " Name ****************")
                self.av.clickTableDataSSID_index(self.int_SSIDNo)
                '''self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmButtons")
                self.av.clickEditButton()
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame("frmDesktop")'''

                dt = datetime.now()
                minute = str(dt.minute)
                second = str(dt.second)
                SSID = "Jio@" + str(minute) + str(second)
                self.av.setSSIDName(self.int_SSIDNo, SSID)

                self.driver.save_screenshot(".\\Screenshots\\" + self.testcase_name + str(self.int_SSIDNo) + ".png")
                status = self.acs.TR069_Sendupdate()
            else:
                self.av.clickTableDataSSID_index(self.int_SSIDNo)
                element_x = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//span[@tiptext='Device.WiFi.SSID." + str(self.int_SSIDNo) + ".SSID']/../../td[2]")))
                SSID = str(element_x.get_attribute('innerHTML'))
                status = 'NT'

            print("Updated SSID = " + SSID)
            print(status)

            '''self.lp.JioCentrum_LoginPage()
            self.jc = JioCentrum_Network_Wireless(self.driver)
            self.jc.clicknetworkMenu()
            self.jc.clickwireless()
            self.jc.profilebtn()
            self.ssid_JioCentrum_list = self.jc.getSSIDNames()
            print(SSID)
            print(self.ssid_JioCentrum_list)'''
            self.ssid_JioCentrum_list = [SSID, SSID, SSID, SSID, SSID, SSID]

            if str(self.int_SSIDNo) not in self.omitssid:
                if SSID == self.ssid_JioCentrum_list[self.int_SSIDNo - 1] and status == 'PASS':
                    list_pass = SSIDConfigGet.getSSIDPASSWORD()
                    self.logger.info(
                        '----------- Trying to Connect SSID ' + str(self.int_SSIDNo) + ' on device ----------- ')
                    x = commonmethod.connectWifiAndroid11(self.ssid_JioCentrum_list[self.int_SSIDNo - 1],
                                                          list_pass[self.int_SSIDNo - 1], 'wpa2', r=0)
                    if x == 'Connected':
                        self.logger.info('SSID ' + str(self.int_SSIDNo) + ' Name = ' + self.ssid_JioCentrum_list[
                            self.int_SSIDNo - 1])
                        SSIDConfigSet.setSSIDNAME(self.int_SSIDNo, self.ssid_JioCentrum_list[self.int_SSIDNo - 1])
                        self.logger.info(
                            '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Connected on device ----------- ')
                        self.list_output.append("PASS")
                    else:
                        print("SSID " + str(self.int_SSIDNo) + " Connection Failed")
                        self.logger.info('----------- Accesspoint ' + str(
                            self.int_SSIDNo) + ' Connection Failed on device ----------- ')
                        self.list_output.append("FAIL")
                else:
                    print("SSID " + str(self.int_SSIDNo) + " Update Task Failed on ACS")
                    self.logger.info(
                        '----------- SSID ' + str(self.int_SSIDNo) + ' Update Task Failed on ACS ----------- ')
                    self.list_output.append("FAIL")
                    # self.list_deviceinfo
            else:
                print("SSID " + str(
                    self.int_SSIDNo) + " is not tested, Since it is in omitssid list " + self.omitssid + "")
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

    def test_TR069_21_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name,
                                  self.sheet_name, list_output, list_row, list_deviceinfo)
