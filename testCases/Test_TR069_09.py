# from selenium import webdriver
import time
import traceback
import pytest
from selenium import common
# from pageObjects.LoginPage import LoginPage
# from pageObjects.ASCSearch import ASC_Search
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from testCases.Test_DeviceInfo import Test_DeviceInfo
from testCases.Test_LoginPage import Test_LoginPage
from testCases.Test_Sanity_GetCurrent import Test_Sanity_GetCurrent
from utilities.ReadTestData import Excel_Env
# from pageObjects.ACSDeviceInfo import ASC_Device_Info
from utilities.customLogger import LogGen
from utilities.outputVariables import *
from utilities.updateExcel import updateExcel


class Test_TR069_09:
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    rownum_Start = 10
    rownum_Finish = 10
    column_no = 5
    testcase_name = "test_TR069_ACS_09"
    no_rows = 1
    result = 0
    logger = LogGen.loggen()

    list_no = []
    list_output = []
    list_screenshot = []
    list_deviceinfo = []
    int_bytessent = 0
    int_bytesreceived = 0
    int_bytessent_yt = 0
    int_bytesreceived_yt = 0

    @pytest.mark.order(9)
    @pytest.mark.complete
    @pytest.mark.sanity
    def test_TR069_09(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + "****************")
            self.driver = setup

            self.gc = Test_Sanity_GetCurrent(self.driver)
            self.gc.test_Sanity_GetCurrent()

            self.lp = Test_LoginPage(self.driver)
            self.lp.ACS_LoginPage()

            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            self.av = ACS_Advanced_View(self.driver)
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadEthernet()
            self.av.clickTableHeadInterface()
            self.av.clickTableHeadInterface1()
            self.av.clickTabledataInterface1Stats()

            self.int_bytesreceived = self.av.getTextdataInterface1StatsBytesReceived()
            self.int_bytessent = self.av.getTextdataInterface1StatsBytesSend()
            print("Bytes Received and sent before playing YouTube Video")
            print("Bytes Received = " + str(self.int_bytesreceived))
            print("Bytes Sent = " + str(self.int_bytessent))

            self.driver.get("https://www.youtube.com/watch?v=VVsC2fD1BjA&ab_channel=ScenicRelaxation")

            self.logger.info("YouTube content playing for 5 min")
            time.sleep(30)

            self.lp.ACS_LoginPage()

            self.av = ACS_Advanced_View(self.driver)
            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()

            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadEthernet()
            self.av.clickTableHeadInterface()
            self.av.clickTableHeadInterface1()
            self.av.clickTabledataInterface1Stats()

            status = self.acs.TR069_Getcurrent()
            print(status)

            self.lp.ACS_LoginPage()

            self.driver.switch_to.default_content()
            self.av.clickTableDataAdvanced()
            self.driver.switch_to.frame("frmDesktop")
            self.av.clickTableHeadEthernet()
            self.av.clickTableHeadInterface()
            self.av.clickTableHeadInterface1()
            self.av.clickTabledataInterface1Stats()
            self.int_bytesreceived_yt = self.av.getTextdataInterface1StatsBytesReceived()
            self.int_bytessent_yt = self.av.getTextdataInterface1StatsBytesSend()
            print("Bytes Received and sent after  playing YouTube Video")
            print("Bytes Received = " + str(self.int_bytesreceived_yt))
            print("Bytes Sent = " + str(self.int_bytessent_yt))
            if self.int_bytesreceived == self.int_bytesreceived_yt and self.int_bytessent == self.int_bytessent_yt:
                self.list_output.append('FAIL')
                self.logger.error("Byte sent and Received before playing YouTube video : "
                                  " " + self.int_bytesreceived + " " + self.int_bytessent + " ")
                self.logger.error("Byte sent and Received after playing YouTube video : "
                                  " " + self.int_bytesreceived_yt + " " + self.int_bytessent_yt + " ")
                self.logger.error("************** " + self.testcase_name + " Failed ****************")
            else:
                self.list_output.append('PASS')
                self.logger.info("Byte sent and received before playing YouTube video : "
                                 " " + self.int_bytesreceived + " " + self.int_bytessent + " ")
                self.logger.info("Byte sent and received after playing YouTube video : "
                                 " " + self.int_bytesreceived_yt + " " + self.int_bytessent_yt + " ")
                self.logger.info("************** " + self.testcase_name + " Passed ****************")

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
            if "FAIL" in self.list_output:
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
                self.logger.error("**************" + self.testcase_name + " Failed ****************")
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

    def test_TR069_09_excel(self, setup):
        self.di = Test_DeviceInfo(setup)
        list_deviceinfo = self.di.DeviceInfo()
        updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row,
                                  list_deviceinfo)
