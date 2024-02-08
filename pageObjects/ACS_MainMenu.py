from selenium.common import NoSuchElementException, ElementClickInterceptedException, WebDriverException, exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen
from pageObjects.ACS_Advanced_View import ACS_Advanced_View
import traceback


class ACS_MainMenu:

    button_pendingtasknumber_xpath = "//tr[@id='tdTasksStatus']/td/table/tbody/tr[1]/td[2]/span"
    button_DeviceInfo_xpath = "//*[@id='lmi3']"
    button_DeviceStatus_xpath = "//*[@id='lblDeviceStatusOnline']"
    button_Recheck_Status = "//*[@id='btnReCheck_btn']"
    button_pendingtask_xpath = "//*[@id='tblTasksStatus']/table/tbody/tr[1]/td[1]/span"
    button_senttask_xpath = "//tr[@id='tdTasksStatus']/td/table/tbody/tr[2]/td[1]/span"
    button_completedtask_xpath = "//tr[@id='tdTasksStatus']/td/table/tbody/tr[3]/td[1]/span"
    button_rejectedtask_xpath = "//tr[@id='tdTasksStatus']/td/table/tbody/tr[4]/td[1]/span"
    button_failedtask_xpath = "//tr[@id='tdTasksStatus']/td/table/tbody/tr[5]/td[1]/span"
    Model_popup_xpath = '//*[@id="btnAlertOk_btn"]'
    logger = LogGen.loggen()
    output = ''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def deviceInfo(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_DeviceInfo_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_DeviceInfo_xpath).click()
            # time.sleep(5)
        '''try:
            element = self.driver.find_element(By.XPATH, self.button_DeviceInfo_xpath)
            time.sleep(10)
            element.click()
        except ElementClickInterceptedException:
            pass'''

    def btnpendingtask(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_pendingtasknumber_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_pendingtasknumber_xpath).click()
            time.sleep(5)
        '''try:
            self.driver.find_element(By.XPATH, self.button_pendingtask_xpath).click()
            time.sleep(10)
        except exceptions:
            pass'''

    def getpendingtasknumber(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.button_pendingtask_xpath)))
        finally:
            try:
                return self.driver.find_element(By.XPATH, self.button_pendingtask_xpath).text
            except NoSuchElementException:
                return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[1]/td[1]").text

    def getsenttasknumber(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[2]/td[1]")))
        finally:
            try:
                return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[2]/td[1]").text
            except NoSuchElementException:
                return self.driver.find_element(By.XPATH, self.button_senttask_xpath).text

    def getcompletedtasknumber(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.button_completedtask_xpath)))
        finally:
            try:
                return self.driver.find_element(By.XPATH, self.button_completedtask_xpath).text
            except NoSuchElementException:
                return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[3]/td[1]").text

    def getfailedtasknumber(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.button_failedtask_xpath)))
        finally:
            try:
                return self.driver.find_element(By.XPATH, self.button_failedtask_xpath).text
            except NoSuchElementException:
                return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[5]/td[1]").text
    '''try:
        return self.driver.find_element(By.XPATH, self.button_failedtask_xpath).text
    except NoSuchElementException:
        return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[5]/td[1]").text'''

    def getrejectedtasknumber(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.button_rejectedtask_xpath)))
        finally:
            try:
                return self.driver.find_element(By.XPATH, self.button_rejectedtask_xpath).text
            except NoSuchElementException:
                return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[4]/td[1]").text
    '''try:
        return self.driver.find_element(By.XPATH, self.button_rejectedtask_xpath).text
    except NoSuchElementException:
        return self.driver.find_element(By.XPATH, "//tr[@id='tdTasksStatus']/td/table/tbody/tr[4]/td[1]").text'''

    def modelpopup(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Model_popup_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.Model_popup_xpath).click()
        '''element = self.driver.find_element(By.XPATH, self.Model_popup_xpath)
        element.click()'''

    def devicestatus(self):
        sf = 0
        self.driver.switch_to.frame("frmDesktop")
        print("Switched to iframe 'frmDesktop' ")
        time.sleep(5)
        start = 0
        i = 0
        while i < 5:
            print("----Loop----")
            if sf == 1:
                sf = 0
                i = i - 1
            try:
                try:
                    element = self.driver.find_element(By.XPATH, self.button_DeviceStatus_xpath)
                    displaystatus = str(element.get_attribute("style"))
                    print(displaystatus)
                    if 'display: none' in displaystatus:
                        start = 1
                        print("Device Online Status Missing ")
                    else:
                        if start != 0:
                            print("Device Online")
                            return "Device Online"
                except NoSuchElementException:
                    start = 1
                    print("Device Online Status Missing ")
                    pass
                element = self.driver.find_element(By.XPATH, self.button_Recheck_Status)
                status = element.get_property('disabled')
                if str(status) == 'False':
                    element.click()
                else:
                    sf = 1
                print("Waiting for 60 seconds")
                time.sleep(60)
            except exceptions:
                print("Exception occurred")
                time.sleep(20)
                pass
            i += 1
        self.driver.switch_to.default_content()
        print("Switched to Main Frame ")
        time.sleep(60)
        print("Device Online Status Missing")
        return "Device Online Status Missing"

    def TR069_TaskStatus(self):
        av = ACS_Advanced_View(self.driver)
        acs = ACS_MainMenu(self.driver)
        # completed_task = 0
        # failed_task = 0
        # rejected_task = 0
        try:
            self.driver.switch_to.default_content()
            completed_task = int(float(acs.getcompletedtasknumber()))
            failed_task = int(float(acs.getfailedtasknumber()))
            rejected_task = int(float(acs.getrejectedtasknumber()))
            try:
                time.sleep(5)
                pending_task = int(float(acs.getpendingtasknumber()))
                sent_task = int(float(acs.getsenttasknumber()))
                while pending_task != 0 or sent_task != 0:
                    print("waiting 30 seconds")
                    time.sleep(30)
                    self.driver.switch_to.default_content()
                    completed_task_new = int(float(acs.getcompletedtasknumber()))
                    failed_task_new = int(float(acs.getfailedtasknumber()))
                    rejected_task_new = int(float(acs.getrejectedtasknumber()))
                    if failed_task_new > failed_task or rejected_task_new > rejected_task:
                        print('Task Failed on ACS')
                        self.logger.info("************** Task Failed on ACS ****************")
                        self.output = 'FAIL'
                        print(completed_task_new, completed_task, failed_task_new, failed_task, rejected_task_new, rejected_task)
                        # break
                    elif completed_task_new > completed_task:
                        self.logger.info("************** Task Passed on ACS ****************")
                        print('Task Completed on ACS')
                        self.output = 'PASS'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                        # break
                    pending_task = int(float(acs.getpendingtasknumber()))
                    print('Pending Tasks = ' + str(pending_task))
                    sent_task = int(float(acs.getsenttasknumber()))
                    print('Sent Tasks = ' + str(sent_task))
                    self.driver.switch_to.default_content()
                    av.clickTableDataAdvanced()
            except NoSuchElementException:
                if self.output == '':
                    self.logger.info("************** No Updates on ACS ****************")
                    return 'PASS'
                return self.output

            if self.output == '':
                self.logger.info("************** No Updates on ACS ****************")
                return 'PASS'
            return self.output

        except ElementClickInterceptedException:
            print("waiting 30 seconds")
            time.sleep(30)
            self.modelpopup()
            return self.TR069_TaskStatus()
        except NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")

    def TR069_Sendupdate(self):
        av = ACS_Advanced_View(self.driver)
        acs = ACS_MainMenu(self.driver)
        # completed_task = 0
        # failed_task = 0
        # rejected_task = 0
        try:
            self.driver.switch_to.default_content()
            completed_task = int(float(acs.getcompletedtasknumber()))
            failed_task = int(float(acs.getfailedtasknumber()))
            rejected_task = int(float(acs.getrejectedtasknumber()))

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            av.clickSendUpdatesButton()
            av.clickAlert()
            self.driver.switch_to.default_content()
            acs.modelpopup()
            try:
                time.sleep(5)
                pending_task = int(float(acs.getpendingtasknumber()))
                sent_task = int(float(acs.getsenttasknumber()))
                while pending_task != 0 or sent_task != 0:
                    print("waiting 30 seconds")
                    time.sleep(30)
                    self.driver.switch_to.default_content()
                    completed_task_new = int(float(acs.getcompletedtasknumber()))
                    failed_task_new = int(float(acs.getfailedtasknumber()))
                    rejected_task_new = int(float(acs.getrejectedtasknumber()))
                    if failed_task_new > failed_task or rejected_task_new > rejected_task:
                        print('Task Failed on ACS')
                        self.logger.info("************** Task Failed on ACS ****************")
                        self.output = 'FAIL'
                        print(completed_task_new, completed_task, failed_task_new, failed_task, rejected_task_new, rejected_task)
                        # break
                    elif completed_task_new > completed_task:
                        self.logger.info("************** Task Passed on ACS ****************")
                        print('Task Completed on ACS')
                        self.output = 'PASS'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                        # break
                    pending_task = int(float(acs.getpendingtasknumber()))
                    print('Pending Tasks = ' + str(pending_task))
                    sent_task = int(float(acs.getsenttasknumber()))
                    print('Sent Tasks = ' + str(sent_task))
                    self.driver.switch_to.default_content()
                    av.clickTableDataAdvanced()
            except NoSuchElementException:
                if self.output == '':
                    self.logger.info("************** No Updates on ACS ****************")
                    return 'PASS'
                return self.output

            if self.output == '':
                self.logger.info("************** No Updates on ACS ****************")
                return 'PASS'
            return self.output

        except ElementClickInterceptedException:
            print("waiting 30 seconds")
            time.sleep(30)
            self.modelpopup()
            return self.TR069_TaskStatus()
        except NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")

    def TR069_Getcurrent(self):
        av = ACS_Advanced_View(self.driver)
        acs = ACS_MainMenu(self.driver)
        # completed_task = 0
        # failed_task = 0
        # rejected_task = 0
        try:
            self.driver.switch_to.default_content()
            completed_task = int(float(acs.getcompletedtasknumber()))
            failed_task = int(float(acs.getfailedtasknumber()))
            rejected_task = int(float(acs.getrejectedtasknumber()))

            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("frmButtons")
            av.clickGetCurrentButton()
            self.driver.switch_to.default_content()
            acs.modelpopup()
            try:
                time.sleep(5)
                pending_task = int(float(acs.getpendingtasknumber()))
                sent_task = int(float(acs.getsenttasknumber()))
                while pending_task != 0 or sent_task != 0:
                    print("waiting 30 seconds")
                    time.sleep(30)
                    self.driver.switch_to.default_content()
                    completed_task_new = int(float(acs.getcompletedtasknumber()))
                    failed_task_new = int(float(acs.getfailedtasknumber()))
                    rejected_task_new = int(float(acs.getrejectedtasknumber()))
                    if failed_task_new > failed_task or rejected_task_new > rejected_task:
                        print('Task Failed on ACS')
                        self.logger.info("************** Task Failed on ACS ****************")
                        self.output = 'FAIL'
                        print(completed_task_new, completed_task, failed_task_new, failed_task, rejected_task_new, rejected_task)
                        # break
                    elif completed_task_new > completed_task:
                        self.logger.info("************** Task Passed on ACS ****************")
                        print('Task Completed on ACS')
                        self.output = 'PASS'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                        # break
                    pending_task = int(float(acs.getpendingtasknumber()))
                    print('Pending Tasks = ' + str(pending_task))
                    sent_task = int(float(acs.getsenttasknumber()))
                    print('Sent Tasks = ' + str(sent_task))
                    self.driver.switch_to.default_content()
                    av.clickTableDataAdvanced()
            except NoSuchElementException:
                if self.output == '':
                    self.logger.info("************** No Updates on ACS ****************")
                    return 'PASS'
                return self.output

            if self.output == '':
                self.logger.info("************** No Updates on ACS ****************")
                return 'PASS'
            return self.output

        except ElementClickInterceptedException:
            print("waiting 30 seconds")
            time.sleep(30)
            self.modelpopup()
            return self.TR069_TaskStatus()
        except NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")

    def TR069_TaskStatusRebootReset(self):
        av = ACS_Advanced_View(self.driver)
        acs = ACS_MainMenu(self.driver)
        try:
            self.driver.switch_to.default_content()
            completed_task = int(float(acs.getcompletedtasknumber()))
            failed_task = int(float(acs.getfailedtasknumber()))
            rejected_task = int(float(acs.getrejectedtasknumber()))
            try:
                time.sleep(5)
                pending_task = int(float(acs.getpendingtasknumber()))
                sent_task = int(float(acs.getsenttasknumber()))
                while pending_task != 0 or sent_task != 0:
                    print("waiting 30 seconds")
                    time.sleep(30)
                    self.driver.switch_to.default_content()
                    completed_task_new = int(float(acs.getcompletedtasknumber()))
                    failed_task_new = int(float(acs.getfailedtasknumber()))
                    rejected_task_new = int(float(acs.getrejectedtasknumber()))
                    if failed_task_new > failed_task or rejected_task_new > rejected_task:
                        print('Task Failed on ACS')
                        self.logger.info("************** Task Failed on ACS ****************")
                        self.output = 'FAIL'
                        print(completed_task_new, completed_task, failed_task_new, failed_task, rejected_task_new,
                              rejected_task)
                    elif completed_task_new > completed_task:
                        self.logger.info("************** Task Passed on ACS ****************")
                        print('Task Completed on ACS')
                        self.output = 'PASS'
                        print(completed_task_new, completed_task, failed_task_new, failed_task)
                    pending_task = int(float(acs.getpendingtasknumber()))
                    print('Pending Tasks = ' + str(pending_task))
                    sent_task = int(float(acs.getsenttasknumber()))
                    print('Sent Tasks = ' + str(sent_task))
                    self.driver.switch_to.default_content()
                    av.clickTableDataAdvanced()
            except NoSuchElementException:
                if self.output == '':
                    self.logger.info("************** No Updates on ACS ****************")
                    return 'PASS'
                return self.output

            if self.output == '':
                self.logger.info("************** No Updates on ACS ****************")
                return 'PASS'
            return self.output

        except ElementClickInterceptedException:
            self.modelpopup()
            return 'PASS'
        except NoSuchElementException:
            print(traceback.format_exc())
            print("No such element")
        except WebDriverException:
            print(traceback.format_exc())
            print("Web driver error")
        except AttributeError:
            print(traceback.format_exc())
            print("Driver error")
