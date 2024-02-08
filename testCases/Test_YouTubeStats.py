import time
from utilities.customLogger import LogGen
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import traceback
from selenium import common
from selenium.webdriver.common.by import By
import subprocess
import pywintypes
import console_ctrl
import requests
import win32api
import traceback


class Test_YouTubeStats:
    testcase_name = "test_YouTubeStats"
    logger = LogGen.loggen()
    overnight = 'No'   # Yes or No
    n = 10

    url = 'google.com'

    def test_YouTubeStats(self, setup):
        try:
            self.logger.info("************** " + self.testcase_name + " Started ****************")
            self.driver = setup
            self.wait = WebDriverWait(self.driver, 5)
            actions = ActionChains(self.driver)
            ping4, ping6 = Test_YouTubeStats.pingCheck(self.n, self.url, self.overnight)
            self.driver.get('https://www.youtube.com/watch?v=wnhvanMdx4s&ab_channel=RelaxationWindows4KNature')
            time.sleep(10)
            actions.send_keys('F').perform()
            time.sleep(5)
            for i in range(12):
                actions.send_keys(Keys.TAB).perform()
                time.sleep(1)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            for i in range(3):
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            for i in range(8):
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(5)
            element = self.driver.find_element(By.XPATH, "//video[@class='video-stream html5-main-video']")
            actions.context_click(on_element=element).perform()
            for i in range(7):
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
            actions.send_keys(Keys.ENTER).perform()
            for i in range(10):
                print(self.driver.find_element(By.XPATH, "//div[contains(text(),'Viewport / Frames')]/../span[1]").text)
                print(self.driver.find_element(By.XPATH, "//div[contains(text(),'Current / Optimal Res')]/../span[1]").text)
                print(self.driver.find_element(By.XPATH, "//div[contains(text(),'Connection Speed')]/../span[1]/span[2]").text)
                print(self.driver.find_element(By.XPATH, "//div[contains(text(),'Buffer Health')]/../span[1]/span[2]").text)
                time.sleep(5)
            out4, err4, out6, err6 = Test_YouTubeStats.pingClose(ping4, ping6)
            print('Output IPv4 = ' + out4.decode())
            print('Error IPv4 = ' + err4.decode())
            print('Output IPv6 = ' + out6.decode())
            print('Error IPv6 = ' + err6.decode())
            time.sleep(5)
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
            assert True
            self.driver.close()
            self.logger.error("************** " + self.testcase_name + " Passed ****************")
        finally:
            if self.result == 0:
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

    @staticmethod
    def pingCheck(n, url, overnight):
        overnight = overnight.lower()
        if overnight == 'yes':
            command4 = ["ping", "-t", "-4", url]
            ping4 = subprocess.Popen(command4, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            command6 = ["ping", "-t", "-6", url]
            ping6 = subprocess.Popen(command6, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
        else:
            command4 = ["ping", "-n", str(n), "-4", url]
            ping4 = subprocess.Popen(command4, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            command6 = ["ping", "-n", str(n), "-6", url]
            ping6 = subprocess.Popen(command6, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
        return ping4, ping6

    @staticmethod
    def pingClose(ping4, ping6):
        console_ctrl.send_ctrl_c(ping4.pid)
        try:
            win32api.TerminateProcess(int(ping4._handle), -1)
        except pywintypes.error:
            print(traceback.format_exc())
            pass
        out4, err4 = ping4.communicate()

        console_ctrl.send_ctrl_c(ping6.pid)
        try:
            win32api.TerminateProcess(int(ping6._handle), -1)
        except pywintypes.error:
            print(traceback.format_exc())
            pass
        out6, err6 = ping6.communicate()

        return out4, err4, out6, err6

