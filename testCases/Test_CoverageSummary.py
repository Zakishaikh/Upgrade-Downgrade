import time
import traceback
from datetime import time

import pytest
from selenium import common

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_Device_Info import ACS_Device_Info
from pageObjects.LoginPage import ACS_LoginPage
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen


class Test_CoverageSummary:
    baseURL = ReadTestData.getACSURL()
    username = ReadTestData.getUserName()
    password = ReadTestData.getPassword()
    serial_no = ReadTestData.getSerialno()
    result = 0
    file = []
    list_deviceinfo = []
    logger = LogGen.loggen()

    @pytest.mark.mahi(2)
    def test_coverageSummary(self, setup):
        try:
            self.logger.info("************** Test TR069 ACS 46-51 ****************")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = ACS_LoginPage(self.driver)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)
            self.sw = ACS_Advanced_View(self.driver)
            self.sw.clickTableDataSearch()
            self.driver.switch_to.frame("frmDesktop")
            time.sleep(4)
            self.sw.setSearch(self.serial_no)
            time.sleep(3)
            self.sw.clickSearchButton()
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.di = ACS_Device_Info(self.driver)
            # self.di.click_TableDataDeviceInfo()
            self.driver.switch_to.frame("frmDesktop")
            time.sleep(3)
            # self.description = self.di.text_description_xpath
            self.list_deviceinfo.append(self.di.getTextHardwareVersion())
            self.list_deviceinfo.append(self.di.getTextSoftwareVersion())
            self.list_deviceinfo.append(self.di.getTextManufacturer())
            self.list_deviceinfo.append(self.di.getTextModelName())
            time.sleep(3)
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
            self.driver.close()
        finally:
            if self.result == 0:
                self.list_deviceinfo = [0, 0, 0, 0]
                # updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)

        # list_deviceinfo.append(self.list_deviceinfo)


'''    def test_CoverageSumary_excel(self):
            updateExcel.writedata_coverageSummary(file,list_deviceinfo)'''
