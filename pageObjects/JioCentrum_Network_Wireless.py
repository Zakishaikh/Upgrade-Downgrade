import time
from datetime import datetime

from selenium.common import StaleElementReferenceException, \
    NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

ssid_JioCentrum_list_1 = []


# ExcelTestResult = []
class JioCentrum_Network_Wireless:
    button_MenuList_xpath = "//div[@id='h_menu_list']"
    button_NetworkSetting_xpath = "//a[contains(text(),'Network Setting')]"
    button_Wireless_xpath = "//span[contains(text(),'Wireless')]"
    button_WirelessGeneral_xpath = "//a[@id='tab_Wireless_General_Tab']"
    button_WirelessGuest_xpath = "//a[@id='tab_Wireless_Guest_Tab']"
    select_WirelessBand_xpath = "//select[@id='wifi_radio_general']"
    textbox_WirelessWifiNetworkName_xpath = "//input[@id='wifi_ssid_000_11general11_000']"
    button_WirelessSecurityLevelMoreSecure_xpath = "//div[@id='Network_Wireless_General_securitylevel']/div[2]/div[@class='colorbar last']"
    select_WirelessSecurityMode_xpath = "//select[@id='wifiSelectSecmode_general_000_11general11_000']"
    button_WirelessSecurityLevelNoSecurity_xpath = "//div[@id='Network_Wireless_General_securitylevel']/div[2]/div[@class='colorbar first']"
    textbox_WirelessPassword_xpath = "//input[@id='wifi_wpa_psk_000_11general11_000']"
    button_WirelessApply_xpath = "//button[@id='applyWifiBtn']"
    textbox_WirelessGuestWifiNetworkName_xpath = "//input[@id='wifi_ssid_0110moreap0110']"
    select_WirelessGuestSecurityMode_xpath = "//select[@id='wifiSelectSecmode_general_0110moreap0110']"
    textbox_WirelessGuestPassword_xpath = "//input[@id='wifi_wpa_psk_0110moreap0110']"
    button_WirelessGuestOK_xpath = "//button[@id='Network_Wireless_APEdit_ApplyBtn']"
    button_CardWifi_xpath = "//div[@id='card_wifi']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def clickAlert(self):
        time.sleep(3)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(3)
        self.driver.switch_to.default_content()

    def clickCardWifi(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_CardWifi_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_CardWifi_xpath).click()

    def clickCardWifiSameSettings(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='WiFiSettings_wifikeepsame_label']")))
        finally:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='WiFiSettings_wifikeepsame_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='WiFiSettings_wifikeepsame_label']").click()
                return 'clicked'
            return 'not clicked'

    def clickMenuList(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_MenuList_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_MenuList_xpath).click()
            time.sleep(4)

    def clickNetworkSetting(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_NetworkSetting_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_NetworkSetting_xpath).click()

    def clickWireless(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_Wireless_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_Wireless_xpath).click()

    def clickWirelessGeneral(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_WirelessGeneral_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_WirelessGeneral_xpath).click()

    def clickSameSettings(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='oneSsid_label']")))
        finally:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='oneSsid_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='oneSsid_label']").click()
                return 'clicked'
            return 'not clicked'

    def selectWirelessBand(self, value):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_WirelessBand_xpath)))
        finally:
            value = value.lower()
            if value == '2.4ghz':
                element = self.driver.find_element(By.ID, "wifi_radio_general")
                se = Select(element)
                se.select_by_visible_text("2.4GHz")
            else:
                element = self.driver.find_element(By.ID, "wifi_radio_general")
                se = Select(element)
                se.select_by_visible_text("5GHz")

    def clickWirelessWifiActiveSlider(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='ssid_state_general_enable']")))
        finally:
            element = self.driver.find_element(By.XPATH, "//label[@id='ssid_state_general_enable']")
            status = element.get_attribute('class')
            print(status)
            if status == "switch  ":
                self.driver.find_element(By.XPATH, "//label[@id='ssid_state_general_enable']/span").click()

    def setWirelessWifiNetworkName(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_WirelessWifiNetworkName_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_WirelessWifiNetworkName_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_WirelessWifiNetworkName_xpath).send_keys(value)

    def clickWirelessSecurityLevelMoreSecure(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_WirelessSecurityLevelMoreSecure_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_WirelessSecurityLevelMoreSecure_xpath).click()

    def selectWirelessSecurityMode(self, mode):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_WirelessSecurityMode_xpath)))
        finally:
            mode = mode.lower()
            if mode == 'wpa2-psk':
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_000_11general11_000")
                se = Select(element)
                se.select_by_visible_text("WPA2-PSK")
            elif mode == 'wpa/wpa2-psk':
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_000_11general11_000")
                se = Select(element)
                se.select_by_visible_text("WPA/WPA2-PSK")
            else:
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_000_11general11_000")
                se = Select(element)
                se.select_by_visible_text("WPA3-SAE")

    def clickWirelessSecurityLevelNoSecurity(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_WirelessSecurityLevelNoSecurity_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_WirelessSecurityLevelNoSecurity_xpath).click()

    def clickWirelessGeneratePasswordAutomatically(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='wifi_wpa_autogen_psk_000_11general11_000_label']")))
        finally:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='wifi_wpa_autogen_psk_000_11general11_000_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='wifi_wpa_autogen_psk_000_11general11_000_label']").click()

    def setWirelessPassword(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_WirelessPassword_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_WirelessPassword_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_WirelessPassword_xpath).send_keys(value)

    def clickWirelessApply(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_WirelessApply_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_WirelessApply_xpath).click()
            time.sleep(5)

    def clickJioImage(self):
        while True:
            try:
                self.driver.find_element(By.XPATH, "//div[@id='cardpage']/span[1]/img[1]").click()
            except ElementClickInterceptedException:
                time.sleep(10)
            else:
                break

    def clickWirelessGuest(self):
        while True:
            try:
                self.driver.find_element(By.XPATH, self.button_WirelessGuest_xpath).click()
            except ElementClickInterceptedException:
                time.sleep(10)
            else:
                break

    def clickGuestAPModify(self, i):
        if i > 5:
            i = i - 5
        else:
            i = i - 1
        tempSSIDModify_xpath = "//span[@id='Network_Wireless_Guest_Edit" + str(i) + "']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSIDModify_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, tempSSIDModify_xpath).click()

    def clickWirelessGuestWifiActiveSlider(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='ssid_state_MoreAPedit_enable']")))
        finally:
            element = self.driver.find_element(By.XPATH, "//label[@id='ssid_state_MoreAPedit_enable']")
            status = element.get_attribute('class')
            print(status)
            if status == "switch  ":
                print('Slider Clicked')
                self.driver.find_element(By.XPATH, "//label[@id='ssid_state_MoreAPedit_enable']/span").click()

    def setWirelessGuestWifiNetworkName(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_WirelessGuestWifiNetworkName_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_WirelessGuestWifiNetworkName_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_WirelessGuestWifiNetworkName_xpath).send_keys(value)

    def clickWirelessGuestHideSSID(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='wifi_hide_ssid_0110moreap0110_label']")))
        except TimeoutException:
            element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[@id='wlEnableGuest_0110moreap0110_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='wlEnableGuest_0110moreap0110_label']").click()
        else:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='wifi_hide_ssid_0110moreap0110_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='wifi_hide_ssid_0110moreap0110_label']").click()

    def selectWirelessGuestSecurityMode(self, mode):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_WirelessGuestSecurityMode_xpath)))
        finally:
            mode = mode.lower()
            if mode == 'wpa2-psk':
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_0110moreap0110")
                se = Select(element)
                se.select_by_visible_text("WPA2-PSK")
            elif mode == 'wpa/wpa2-psk':
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_0110moreap0110")
                se = Select(element)
                se.select_by_visible_text("WPA/WPA2-PSK")
            else:
                element = self.driver.find_element(By.ID, "wifiSelectSecmode_general_0110moreap0110")
                se = Select(element)
                se.select_by_visible_text("WPA3-SAE")

    def clickWirelessGuestGeneratePasswordAutomatically(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id='wifi_wpa_autogen_psk_0110moreap0110_label']")))
        finally:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[@id='wifi_wpa_autogen_psk_0110moreap0110_label']")))
            status = element.get_attribute('class')
            if status == "custom-control custom-checkbox active ":
                self.driver.find_element(By.XPATH, "//label[@id='wifi_wpa_autogen_psk_0110moreap0110_label']").click()

    def setWirelessGuestPassword(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_WirelessGuestPassword_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_WirelessGuestPassword_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_WirelessGuestPassword_xpath).send_keys(value)

    def clickWirelessGuestOK(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_WirelessGuestOK_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_WirelessGuestOK_xpath).click()

    def getGuestSSIDName(self, i):
        if i > 5:
            i = i - 5
        else:
            i = i - 1
        tempSSIDName_xpath = "//table[@id='Network_Wireless_Guest_Table']/tbody[1]/tr[" + str(i) + "]/td[3]"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSIDName_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, tempSSIDName_xpath).text

    def getGuestSSIDSecurity(self, i):
        if i > 5:
            i = i - 5
        else:
            i = i - 1
        tempSSIDSecurity_xpath = "//table[@id='Network_Wireless_Guest_Table']/tbody[1]/tr[" + str(i) + "]/td[4]"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSIDSecurity_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, tempSSIDSecurity_xpath).text

    def getSSID1Name(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='card_24gwifiname']")))
        finally:
            return self.driver.find_element(By.XPATH, "//div[@id='card_24gwifiname']").text

    def getSSID5Name(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='card_5gwifiname']")))
        finally:
            return self.driver.find_element(By.XPATH, "//div[@id='card_5gwifiname']").text