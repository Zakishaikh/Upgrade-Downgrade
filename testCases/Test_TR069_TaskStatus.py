import time
import traceback

import pytest
from selenium import common

from pageObjects.ACS_Advanced_View import ACS_Advanced_View
from pageObjects.ACS_MainMenu import ACS_MainMenu
from utilities.ReadTestData import Excel_Env
from utilities.ReadTestData import ReadTestData
from utilities.customLogger import LogGen


class Test_TR069_TaskStatus:
    """ baseURL = ReadTestData.getACSURL()
    username = ReadTestData.getUserName()
    password = ReadTestData.getPassword()
    serial_no = ReadTestData.getSerialno()"""
    omitssid = str(ReadTestData.getomitssid())
    '''hgw_URL = ReadTestData.getHGWURL()
    username_HGW = ReadTestData.getUserNameHGW()
    password_HGW = ReadTestData.getPasswordHGW()'''
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    output = ''
    list_screenshot = []
    result = 0
    # list_screenshot = ['not changed'] * 6
    testcase_name = "test_TaskStatus"
    list_deviceinfo = []
    list_row = []
    logger = LogGen.loggen()

    @pytest.mark.skip(reason="Executing Twice")
    def test_TR069_TaskStatus(self, setup):
        try:
            self.driver = setup
            self.acs = ACS_MainMenu(self.driver)
            self.driver.switch_to.default_content()
            completed_task = int(float(self.acs.getcompletedtasknumber()))
            failed_task = int(float(self.acs.getfailedtasknumber()))
            time.sleep(2)
            # time.sleep(4)
            self.av = ACS_Advanced_View(self.driver)
            time.sleep(2)
            try:
                pending_task = int(float(self.acs.getpendingtasknumber()))
                while pending_task != 0:
                    print("waiting 30 seconds")
                    time.sleep(30)
                    self.driver.switch_to.default_content()
                    completed_task_new = int(float(self.acs.getcompletedtasknumber()))
                    failed_task_new = int(float(self.acs.getfailedtasknumber()))
                    if failed_task_new > failed_task:
                        print('Task Failed on ACS')
                        self.output = 'FAIL'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                        break
                    elif completed_task_new > completed_task:
                        print('Task Completed on ACS')
                        self.output = 'PASS'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                        break
                    pending_task = int(float(self.acs.getpendingtasknumber()))
                    print('Pending Tasks = ' + str(pending_task))
                    self.logger.info("************** Pending Tasks = " + str(pending_task) + " ****************")
                    self.driver.switch_to.default_content()
                    self.av.clickTableDataAdvanced()
            except common.exceptions.NoSuchElementException:
                if self.output == '':
                    return 'PASS'
                return self.output
            if self.output == '':
                return 'PASS'
            return self.output

        except common.exceptions.NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
