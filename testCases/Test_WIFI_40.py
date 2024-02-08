import time
import pytest
from pageObjects.ACS_Device_Info import ACS_Device_Info
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from pageObjects.ACS_FileDownload import ACS_File_Download
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.JioCentrum_Network_Wireless import JioCentrum_Network_Wireless
from utilities.WriteTestData import SSIDConfigSet
from utilities.customLogger import LogGen
from utilities.updateExcel import updateExcel
from utilities.commonmethod import commonmethod
from utilities.outputVariables import *
from utilities.ReadTestData import Excel_Env, SSIDConfigGet
import traceback
from selenium import common


class Test_WIFI_40:

    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = 'WIFI'
    test_name = Excel_Env.gettest_name()
    list_output = []
    rownum_Start = 43
    rownum_Finish = 43
    column_no = 5
    result = 0
    no_rows = 1
    testcase_name = "test_WIFI_40"
    logger = LogGen.loggen()
    int_SSIDNo = 7
    str_WirelessBand = '5GHZ'
    str_WirelessName = ' Test_40 IDCPE 07'
    list_screenshot = []
    list_deviceinfo = []

    @pytest.mark.order(23)
    @pytest.mark.wifi
    def test_WIFI_40(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + " Started ****************")
            self.driver = setup
            commonmethod.ForgotAllNetwork()
            self.lp = Test_LoginPage(self.driver)
            self.gui = JioCentrum_Network_Wireless(self.driver)

            self.lp.JioCentrum_LoginPage()
            self.gui.clickMenuList()
            self.gui.clickNetworkSetting()
            self.gui.clickWireless()
            self.gui.clickWirelessGeneral()
            self.gui.selectWirelessBand(self.str_WirelessBand)
            q = self.gui.clickSameSettings()
            if q == 'clicked':
                self.gui.clickWirelessApply()

            self.gui.clickWirelessGuest()
            self.gui.clickGuestAPModify(self.int_SSIDNo)
            time.sleep(4)
            self.gui.clickWirelessGuestWifiActiveSlider()
            self.gui.setWirelessGuestWifiNetworkName(self.str_WirelessName)
            self.gui.clickWirelessGuestHideSSID()
            self.gui.clickWirelessGuestOK()
            self.gui.clickJioImage()
            list_Pass = SSIDConfigGet.getSSIDPASSWORD()
            x = commonmethod.connectWifiAndroid11(self.str_WirelessName, list_Pass[self.int_SSIDNo-1], 'wpa2', r=0)
            if x == 'Connected':
                self.logger.info('SSID ' + str(self.int_SSIDNo) + ' Name = ' + self.str_WirelessName)
                self.logger.info('SSID ' + str(self.int_SSIDNo) + ' Password = ' + list_Pass[self.int_SSIDNo-1])
                SSIDConfigSet.setSSIDNAME(str(self.int_SSIDNo), self.str_WirelessName)
                SSIDConfigSet.setSSIDPASSWORD(str(self.int_SSIDNo), list_Pass[self.int_SSIDNo-1])
                self.logger.info(
                    '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Connected on device ----------- ')
                self.list_output.append("FAIL")
            elif x == 'Internet':
                self.logger.info('SSID ' + str(self.int_SSIDNo) + ' Name = ' + self.str_WirelessName)
                self.logger.info('SSID ' + str(self.int_SSIDNo) + ' Password = ' + list_Pass[self.int_SSIDNo-1])
                SSIDConfigSet.setSSIDNAME(str(self.int_SSIDNo), self.str_WirelessName)
                SSIDConfigSet.setSSIDPASSWORD(str(self.int_SSIDNo), list_Pass[self.int_SSIDNo-1])
                self.logger.info(
                    '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Connected on device but Internet Not Available ----------- ')
                self.list_output.append("FAIL")
            else:
                print('SSID ' + str(self.int_SSIDNo) + ' Connection Failed')
                self.logger.info(
                    '----------- Accesspoint ' + str(self.int_SSIDNo) + ' Connection Failed on device ----------- ')
                self.list_output.append("PASS")

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

    def test_WIFI_40_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
