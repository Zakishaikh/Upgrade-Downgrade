import time

from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class ACS_Advanced_View:
    tabledata_search_xpath = "//span[@id='lmi1']"
    textbox_search_xpath = "//input[@id='tbDeviceID']"
    button_search_xpath = "//input[@id='btnSearch_btn']"

    textbox_securitykeypassphrase_xpath = "//tbody/tr[2]/td[2]/input[1]"
    textbox_securitymodeenabled_xpath = "//tbody/tr[3]/td[2]/input[1]"

    tabledata_advanced_xpath = "//span[@id='lmi5']"
    tablehead_wifi_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.']/../img"
    tabledata_accesspoint_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.AccessPoint.']/../img"
    tabledata_accesspoint2_xpath = "//span[contains(text(),'AccessPoint.2')]"
    button_click_SSID = ""
    textbox_accesspointenable_xpath = "//tbody/tr[3]/td[2]/input[1]"
    textbox_accesspointwpseneble_xpath = "/html/body/form/table[2]/tbody/tr/td[2]/span/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/input"
    textbox_accesspointSSIDAdvertisementEnabled_xpath = "//tbody/tr[5]/td[2]/input[1]"
    textbox_accesspointmaxassociateddevice_xpath = "//tbody/tr[4]/td[2]/input[1]"

    button_edit_xpath = "//input[@id='UcDeviceSettingsControls1_btnChange_btn']"
    button_sendupdates_xpath = "//input[@id='UcDeviceSettingsControls1_btnSendUpdate_btn']"
    button_sendupdatesok_xpath = "//input[@id='btnAlertOk_btn']"
    button_cancel_xpath = "//input[@id='UcDeviceSettingsControls1_btnCancel_btn']"
    button_getcurrent_xpath = "//input[@id='UcDeviceSettingsControls1_btnGetCurrent_btn']"
    button_saveparameter_xpath = "//input[@id='UcDeviceSettingsControls1_btnSaveParameters_btn']"

    tablehead_ip_xpath = "//tbody/tr/td/span[@fullname='Device.IP.']/../img"
    tablehead_ipinterface_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.']/../img"

    tablehead_ipinterface1_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.1.']/../img"
    tablehead_ipinterface1ipv4_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.1.IPv4Address.']/../img"
    tabledata_ipinterface1ipv41_xpath = "//span[@fullname='Device.IP.Interface.1.IPv4Address.1.']"
    textdata_ipinterface1ipv41_xpath = "//span[@tiptext='Device.IP.Interface.1.IPv4Address.1.IPAddress']/../../td[2]"
    tablehead_ipinterface1ipv6_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.1.IPv6Address.']/../img"
    tabledata_ipinterface1ipv61_xpath = '//span[@fullname="Device.IP.Interface.1.IPv6Address.1."]'
    textdata_ipinterface1ipv61_xpath = "//span[@tiptext='Device.IP.Interface.1.IPv6Address.1.IPAddress']/../../td[2]"

    tablehead_ipinterface2_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.2.']/../img"
    tablehead_ipinterface2ipv4_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.2.IPv4Address.']/../img"
    tabledata_ipinterface2ipv41_xpath = "//span[@fullname='Device.IP.Interface.2.IPv4Address.1.']"
    textdata_ipinterface2ipv41_xpath = "//span[@tiptext='Device.IP.Interface.2.IPv4Address.1.IPAddress']/../../td[2]"
    tablehead_ipinterface2ipv6_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Interface.2.IPv6Address.']/../img"
    tabledata_ipinterface2ipv61_xpath = '//span[@fullname="Device.IP.Interface.2.IPv6Address.1."]'
    textdata_ipinterface2ipv61_xpath = "//span[@tiptext='Device.IP.Interface.2.IPv6Address.1.IPAddress']/../../td[2]"

    tablehead_IPDiagnostics_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Diagnostics.']/../img"
    tablehead_IPDiagnosticsTraceRoute_xpath = "//tbody/tr/td/span[@fullname='Device.IP.Diagnostics.TraceRoute.']/../img"
    tabledata_IPDiagnosticsTraceRoute_xpath = "//span[@fullname='Device.IP.Diagnostics.TraceRoute.']"
    textbox_IPDiagnosticsTraceRouteDiagnosticsState_xpath = "//input[@paramname='Device.IP.Diagnostics.TraceRoute.DiagnosticsState']"
    textbox_IPDiagnosticsTraceRouteHost_xpath = "//input[@paramname='Device.IP.Diagnostics.TraceRoute.Host']"
    textbox_IPDiagnosticsTraceRouteProtocolVersion_xpath = "//input[@paramname='Device.IP.Diagnostics.TraceRoute.ProtocolVersion']"
    textbox_IPDiagnosticsTraceRouteMaxHopCount_xpath = "//input[@paramname='Device.IP.Diagnostics.TraceRoute.MaxHopCount']"

    tabledata_radio_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.Radio.']/../img"
    textbox_radioautochannelenable_xpath = "//tbody/tr[2]/td[2]/input[1]"
    textbox_radiochannel_xpath = "//tbody/tr[5]/td[2]/input[1]"

    tabledata_hosts_xpath = "//span[contains(text(),'Hosts')]"
    textdata_hostnoofentries_xpath = "//span[@tiptext='Device.Hosts.HostNumberOfEntries']/../../td[2]"

    tabledata_managementserver_xpath = "//span[@fullname='Device.ManagementServer.']"
    textdata_ConnectionRequestURL_xpath = "//span[@tiptext='Device.ManagementServer.ConnectionRequestURL']/../../td[2]/textarea[@paramname='Device.ManagementServer.ConnectionRequestURL']"
    textbox_managementserverURL1_xpath = "//textarea[@paramname='Device.ManagementServer.URL']"
    textbox_managementserverURL2_xpath = "//input[@paramname='Device.ManagementServer.URL']"
    textbox_PeriodicInformInterval_xpath = "//input[@paramname='Device.ManagementServer.PeriodicInformInterval']"

    tablehead_dhcpv4_xpath = "//tbody/tr/td/span[@fullname='Device.DHCPv4.']/../img"
    tabledata_dhcpv4server_xpath = "//tbody/tr[29]/td[1]/span[2]"
    textbox_dhcpv4serverenable_xpath = "/html[1]/body[1]/form[1]/table[2]/tbody[1]/tr[1]/td[2]/span[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]"
    tablehead_dhcpv4server_xpath = "//tbody/tr/td/span[@fullname='Device.DHCPv4.Server.']/../img"
    tablehead_dhcpv4pool_xpath = "//tbody/tr/td/span[@fullname='Device.DHCPv4.Server.Pool.']/../img"
    tabledata_dhcpv4pool1_xpath = "//span[contains(text(),'Pool.1')]"
    textbox_dhcpv4pool1maxadd_xpath = "//input[@paramname='Device.DHCPv4.Server.Pool.1.MaxAddress']"
    textbox_dhcpv4pool1minadd_xpath = "//input[@paramname='Device.DHCPv4.Server.Pool.1.MinAddress']"
    #textbox_accesspointSSIDAdvertisementEnabled_xpath = "//tbody/tr[5]/td[2]/input[1]"
    textbox_wps_xpath = "//tbody/tr[4]/td[2]/input[1]"

    #textbox_securitykeypassphrase_xpath = "//tbody/tr[2]/td[2]/input[1]"
    #textbox_securitymodeenabled_xpath = "//tbody/tr[3]/td[2]/input[1]"

    textdata_ssidstatsbytesreceived_xpath = "//span[@tiptext='Device.WiFi.SSID.1.Stats.BytesReceived']/../../td[2]"
    textdata_ssidstatsbytessent_xpath = "//span[@tiptext='Device.WiFi.SSID.1.Stats.BytesSent']/../../td[2]"
    textdata_ssidstatspacketsreceived_xpath = "//span[@tiptext='Device.WiFi.SSID.1.Stats.PacketsReceived']/../../td[2]"
    textdata_ssidstatspacketssent_xpath = "//span[@tiptext='Device.WiFi.SSID.1.Stats.PacketsSent']/../../td[2]"

    tablehead_ssid_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.SSID.']/../img"

    textbox_ssidname_xpath = "//tbody/tr[7]/td[2]/input[1]"

    tablehead_ethernet_xpath = "//tbody/tr/td/span[@fullname='Device.Ethernet.']/../img"
    tablehead_interface_xpath = "//tbody/tr/td/span[@fullname='Device.Ethernet.Interface.']/../img"
    tablehead_interface1_xpath = "//tbody/tr/td/span[@fullname='Device.Ethernet.Interface.1.']/../img"
    tablehead_interface2_xpath = "//tbody/tr/td/span[@fullname='Device.Ethernet.Interface.2.']/../img"
    tabledata_interface1stats_xpath = "//span[@fullname='Device.Ethernet.Interface.1.Stats.']"
    tabledata_interface2stats_xpath = "//span[@fullname='Device.Ethernet.Interface.2.Stats.']"
    textdata_interface1statsbytesreceived_xpath = "//span[@tiptext='Device.Ethernet.Interface.1.Stats.BytesReceived']/../../td[2]"
    textdata_interface2statsbytesreceived_xpath = "//span[@tiptext='Device.Ethernet.Interface.2.Stats.BytesReceived']/../../td[2]"
    textdata_interface1statsbytessend_xpath = "//span[@tiptext='Device.Ethernet.Interface.1.Stats.BytesSent']/../../td[2]"
    textdata_interface2statsbytessend_xpath = "//span[@tiptext='Device.Ethernet.Interface.2.Stats.BytesSent']/../../td[2]"

    tablehead_dns_xpath = "//tbody/tr/td/span[@fullname='Device.DNS.']/../img"
    tablehead_dnsClient_xpath = "//tbody/tr/td/span[@fullname='Device.DNS.Client.']/../img"
    tablehead_dnsClientServer_xpath = "//tbody/tr/td/span[@fullname='Device.DNS.Client.Server.']/../img"
    tabledata_dnsClientServerServer1_xpath = "//span[@fullname='Device.DNS.Client.Server.1.']"
    textbox_dnsserver1DNSSERVER_xpath = "//input[@paramname='Device.DNS.Client.Server.1.DNSServer']"
    tablehead_dnsdiagnostics_xpath = "//tbody/tr/td/span[@fullname='Device.DNS.Diagnostics.']/../img"
    tabledata_nslookupdiagnostics_xpath = "//span[@fullname='Device.DNS.Diagnostics.NSLookupDiagnostics.']"
    tablehead_nslookupdiagnostics_xpath = "//tbody/tr/td/span[@fullname='Device.DNS.Diagnostics.NSLookupDiagnostics.']/../img"
    tabledata_dnsresult_xpath = "//span[@fullname='Device.DNS.Diagnostics.NSLookupDiagnostics.Result.']"
    textbox_dnsdiagnosticstate_xpath = "//input[@paramname='Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState']"
    textbox_dnshostname_xpath = "//input[@paramname='Device.DNS.Diagnostics.NSLookupDiagnostics.HostName']"
    textbox_dnsnoofrepetitions_xpath = "//input[@paramname='Device.DNS.Diagnostics.NSLookupDiagnostics.NumberOfRepetitions']"

    tabledata_wangponlinkconfig_xpath = "//tbody/tr/td/span[@fullname='Device.X_RJIL_COM_WANGponLinkConfig.']"
    textbox_vlanidmark_xpath = "//tbody/tr/td/input[@paramname='Device.X_RJIL_COM_WANGponLinkConfig.VLANIDMark']"

    tabledata_Device_xpath = "//span[@fullname='Device.']"
    textdata_DeviceInterfaceStackNumberOfEntries_xpath = "//span[@tiptext='Device.InterfaceStackNumberOfEntries']/../../td[2]"

    tablehead_Routing_xpath = "//tbody/tr/td/span[@fullname='Device.Routing.']/../img"
    tablehead_RoutingRouter_xpath = "//tbody/tr/td/span[@fullname='Device.Routing.Router.']/../img"
    tablehead_RoutingRouter1_xpath = "//tbody/tr/td/span[@fullname='Device.Routing.Router.1.']/../img"
    tabledata_RoutingRouter1_xpath = "//span[@fullname='Device.Routing.Router.1.']"
    textdata_RoutingRouter1Enable_xpath = "//span[@tiptext='Device.Routing.Router.1.Enable']/../../td[2]"
    tablehead_RoutingRouter1IPv4Forwarding_xpath = "//tbody/tr/td/span[@fullname='Device.Routing.Router.1.IPv4Forwarding.']/../img"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def clickTableDataSearch(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_search_xpath)))
            # print('Located Search')
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_search_xpath).click()
            # print('Clicked Search')

    def setSearch(self, searchid):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_search_xpath)))
            # print('Located Search ID')
        finally:
            self.driver.find_element(By.XPATH, self.textbox_search_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_search_xpath).send_keys(searchid)
            # print('Clicked Search ID')

    def clickTableDataManagementServer(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_managementserver_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_managementserver_xpath).click()

    def selectManagementServerPeriodicInformEnableNotification(self, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@tiptext='Device.ManagementServer.PeriodicInformEnable']/../../td[3]/select")))
        finally:
            element = self.driver.find_element(By.XPATH, "//span[@tiptext='Device.ManagementServer.PeriodicInformEnable']/../../td[3]/select")
            se = Select(element)
            se.select_by_visible_text(value)

    def getConnectionRequestURL(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_ConnectionRequestURL_xpath)))
        finally:
            try:
                return self.driver.find_element(By.XPATH, self.textdata_ConnectionRequestURL_xpath).text
            except common.exceptions.NoSuchElementException:
                return self.driver.find_element(By.XPATH,
                                                "//span[@tiptext='Device.ManagementServer.ConnectionRequestURL']/../../td[2]").text
    '''try:
        return self.driver.find_element(By.XPATH, self.textdata_ConnectionRequestURL_xpath).text
    except common.exceptions.NoSuchElementException:
        return self.driver.find_element(By.XPATH, "//span[@tiptext='Device.ManagementServer.ConnectionRequestURL']/../../td[2]").text
'''
    def setManagementServerURL(self, url):
        try:
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.textbox_managementserverURL1_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.textbox_managementserverURL1_xpath).clear()
                self.driver.find_element(By.XPATH, self.textbox_managementserverURL1_xpath).send_keys(url)
        except common.exceptions.NoSuchElementException:
            try:
                self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.textbox_managementserverURL2_xpath)))
            finally:
                self.driver.find_element(By.XPATH, self.textbox_managementserverURL2_xpath).clear()
                self.driver.find_element(By.XPATH, self.textbox_managementserverURL2_xpath).send_keys(url)

    def setPeriodicInformInterval(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_PeriodicInformInterval_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_PeriodicInformInterval_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_PeriodicInformInterval_xpath).send_keys(value)

    def clickSearchButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_search_xpath)))
            # print('Located Search button')
        finally:
            self.driver.find_element(By.XPATH, self.button_search_xpath).click()
            # print('Clicked Search button')

    def clickTableDataAdvanced(self):
        time.sleep(5)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_advanced_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_advanced_xpath).click()

    def ClickTableDataAccespoint_index(self, i):
        #time.sleep(2)
        tempaccesspoint_xpath = "//span[@fullname='Device.WiFi.AccessPoint." + str(i) + ".']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempaccesspoint_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempaccesspoint_xpath).click()

    def clickTableHeadWifi(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_wifi_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_wifi_xpath).click()

    def clickTableDataAccessPoint(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_accesspoint_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_accesspoint_xpath).click()

    def clickTableDataAccessPoint2(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_accesspoint2_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_accesspoint2_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_accesspoint2_xpath).click()

    def clickEditButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_edit_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_edit_xpath).click()
            time.sleep(3)
        # self.driver.find_element(By.XPATH, self.button_edit_xpath).click()

    def setAccessPointEnable(self, i, value):
        # time.sleep(2)
        temp_xpath = '//input[@paramname="Device.WiFi.AccessPoint.' + str(i) + '.Enable"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)

    def getAccessPointEnable(self, i):
        temp_xpath = "//span[@tiptext='Device.WiFi.AccessPoint." + str(i) + ".Enable']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, temp_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, temp_xpath).text

    def getAccessPointSSIDAdvertisementEnabled(self, i):
        temp_xpath = "//span[@tiptext='Device.WiFi.AccessPoint." + str(i) + ".SSIDAdvertisementEnabled']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, temp_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, temp_xpath).text

    def setAccessPointMaxAssociatedDevice(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_accesspointmaxassociateddevice_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_accesspointmaxassociateddevice_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_accesspointmaxassociateddevice_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_accesspointmaxassociateddevice_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_accesspointmaxassociateddevice_xpath).send_keys(value)
'''
    def setAccessPointMaxAssocDevice(self, value, i):
        temp_xpath = "//input[@paramname='Device.WiFi.AccessPoint." + str(i) + ".MaxAssociatedDevices']"
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, temp_xpath).clear()
        self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
'''
    def setAccessPointWPSEnable(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_accesspointwpseneble_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(Keys.CONTROL + "a")
            self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(Keys.DELETE)
            self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, self.textbox_accesspointwpseneble_xpath).send_keys(value)'''

    def clickTableDataRadio(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_radio_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_radio_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_radio_xpath).click()

    def clickTableDataRadio_index(self, i):
        tempradio_xpath = "//span[@fullname='Device.WiFi.Radio." + str(i) + ".']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempradio_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempradio_xpath).click()
        # self.driver.find_element(By.XPATH, tempradio_xpath).click()

    def setRadioAutoChannelEnable(self, i, value):
        temp_xpath = '//input[@paramname="Device.WiFi.Radio.' + str(i) + '.AutoChannelEnable"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_radioautochannelenable_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_radioautochannelenable_xpath).send_keys(value)'''

    def clickSendUpdatesButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_sendupdates_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_sendupdates_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_sendupdates_xpath).click()

    def clickSendUpdatesOKButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_sendupdatesok_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_sendupdatesok_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_sendupdatesok_xpath).click()

    def clickAlert(self):
        time.sleep(4)
        alert = self.driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        time.sleep(3)

    def clickCancelButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_cancel_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_cancel_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_cancel_xpath).click()

    def clickGetCurrentButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_getcurrent_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_getcurrent_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_getcurrent_xpath).click()

    def clickSaveParameterButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_saveparameter_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.button_saveparameter_xpath).click()
        # self.driver.find_element(By.XPATH, self.button_saveparameter_xpath).click()

    def getPeriodicInformInterval(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@tiptext='Device.ManagementServer.PeriodicInformInterval']/../../td[2]")))
        finally:
            return self.driver.find_element(By.XPATH, "//span[@tiptext='Device.ManagementServer.PeriodicInformInterval']/../../td[2]").text

    def getManagementServerURL(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@tiptext='Device.ManagementServer.URL']/../../td[2]")))
        finally:
            return self.driver.find_element(By.XPATH, "//span[@tiptext='Device.ManagementServer.URL']/../../td[2]").text

    def setAccessPointSSIDAdvertisementEnabled(self, i, value):
        temp_xpath = '//input[@paramname="Device.WiFi.AccessPoint.' + str(i) + '.SSIDAdvertisementEnabled"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''try:
            self.driver.find_element(By.XPATH, self.textbox_accesspointSSIDAdvertisementEnabled_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_accesspointSSIDAdvertisementEnabled_xpath).send_keys(value)
        except StaleElementReferenceException:
            pass'''

    def clickTableHeadDHCPv4(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dhcpv4_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dhcpv4_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_dhcpv4_xpath).click()

    def clickTableDataDHCPv4Server(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_dhcpv4server_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_dhcpv4server_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_dhcpv4server_xpath).click()

    def setDHCPv4ServerEnable(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dhcpv4serverenable_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4serverenable_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4serverenable_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dhcpv4serverenable_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dhcpv4serverenable_xpath).send_keys(value)'''

    def clickTableHeadDHCPv4Server(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dhcpv4server_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dhcpv4server_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_dhcpv4server_xpath).click()

    def clickTableHeadDHCPv4Pool(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dhcpv4pool_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dhcpv4pool_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_dhcpv4pool_xpath).click()

    def clickTableDataDHCPv4Pool1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_dhcpv4pool1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_dhcpv4pool1_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_dhcpv4pool1_xpath).click()

    def setDHCPv4Pool1Add(self, i, value):
        if i == 0:
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).send_keys(value)
        elif i == 1:
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).send_keys(value)

    def setDHCPv4Pool1MaxAdd(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1maxadd_xpath).send_keys(value)'''

    def setDHCPv4Pool1MinAdd(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dhcpv4pool1minadd_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dhcpv4pool1minadd_xpath).send_keys(value)'''

    def ClickTableHeadAccespoint(self, i):
        tempaccesspoint_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.AccessPoint." + str(i) + ".']/../img"
        # time.sleep(2)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempaccesspoint_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempaccesspoint_xpath).click()
        # self.driver.find_element(By.XPATH, tempaccesspoint_xpath).click()

    def ClickTabledataAccespointAssociatedDevice(self, i):
        tempAssociatedDevice_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.AccessPoint." + str(i) + ".AssociatedDevice.']"
        # time.sleep(2)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempAssociatedDevice_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempAssociatedDevice_xpath).click()

    def ClickTableDataWPS(self, i):
        tempwps_xpath = "//span[@fullname='Device.WiFi.AccessPoint." + str(i) + ".WPS.']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempwps_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempwps_xpath).click()
        # self.driver.find_element(By.XPATH, tempwps_xpath).click()

    def setSecurityModeEnabled(self, i, value):
        # time.sleep(2)
        temp_xpath = '//input[@paramname="Device.WiFi.AccessPoint.' + str(i) + '.Security.ModeEnabled"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_securitymodeenabled_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_securitymodeenabled_xpath).send_keys(value)'''

    def ClickTableDataSecurity(self, i):
        y = ["1", "2", "3", "4", "5", "6"]
        tempsecurity_xpath = "//span[@fullname='Device.WiFi.AccessPoint." + y[i - 1] + ".Security.']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempsecurity_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempsecurity_xpath).click()
        # self.driver.find_element(By.XPATH, tempsecurity_xpath).click()

    def ClickAPSecurity(self, i):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class ='wizard_tree_enable'][normalize-space()='Security'])["+str(i)+"]")))
        finally:
            self.driver.find_element(By.XPATH, "(//span[@class ='wizard_tree_enable'][normalize-space()='Security'])["+str(i)+"]").click()
        # self.driver.find_element(By.XPATH, "(//span[@class ='wizard_tree_enable'][normalize-space()='Security'])["+str(i)+"]").click()

    def setWpsEnable(self, i, value):
        temp_xpath = '//input[@paramname="Device.WiFi.AccessPoint.' + str(i) + '.WPS.Enable"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_wps_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_wps_xpath).send_keys(value)'''

    def clickTableHeadSSID(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ssid_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ssid_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ssid_xpath).click()

    def clickTableDataSSID_index(self, index):
        tempSSID_xpath = "//span[contains(text(),'SSID." + str(index) + "')]"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSID_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempSSID_xpath).click()
        # self.driver.find_element(By.XPATH, tempSSID_xpath).click()

    def setSSIDName(self, i, value):
        temp_xpath = '//input[@paramname="Device.WiFi.SSID.' + str(i) + '.SSID"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_ssidname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_ssidname_xpath).send_keys(value)'''

    def clickSSID(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'SSID')]/preceding-sibling::img[1]")))
        finally:
            self.driver.find_element(By.XPATH, "//span[contains(text(),'SSID')]/preceding-sibling::img[1]").click()

        '''try:
            #element=self.driver.find_element(By.XPATH,'//*[@id="img_81436377"]')
            element = self.driver.find_element(By.XPATH, "// span[contains(text(),'SSID')]/preceding-sibling::img[1]")
            print("SSID Collapse Or Expand ")
            print(element.get_attribute("src"))
            time.sleep(5)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            if "Expand" in element.get_attribute("src"):
                print("Click on SSID")
                #self.driver.find_element(By.XPATH,'//*[@id="img_81436377"]').click()
                self.driver.find_element(By.XPATH, "// span[contains(text(),'SSID')]/preceding-sibling::img[1]").click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            pass'''

    '''def setAccessPointSSIDAdvertisementEnabled(self, value):
        self.driver.find_element(By.XPATH, self.textbox_accesspointSSIDAdvertisementEnabled_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_accesspointSSIDAdvertisementEnabled_xpath).send_keys(value)
'''

    def clickSSIDHEAD(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"SSID")]')))
        finally:
            self.driver.find_element(By.XPATH, '//span[contains(text(),"SSID")]').click()

    def clickTableHeadEthernet(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ethernet_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ethernet_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ethernet_xpath).click()

    def clickTableHeadInterface(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_interface_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_interface_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_interface_xpath).click()

    def clickTableHeadInterface1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_interface1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_interface1_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_interface1_xpath).click()

    def clickTableHeadInterface2(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_interface2_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_interface2_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_interface2_xpath).click()

    def clickTabledataInterface1Stats(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_interface1stats_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_interface1stats_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_interface1stats_xpath).click()

    def clickTabledataInterface2Stats(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_interface2stats_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_interface2stats_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_interface2stats_xpath).click()

    def getTextdataInterface1StatsBytesReceived(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_interface1statsbytesreceived_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_interface1statsbytesreceived_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_interface1statsbytesreceived_xpath).text

    def getTextdataInterface2StatsBytesReceived(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_interface2statsbytesreceived_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_interface2statsbytesreceived_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_interface2statsbytesreceived_xpath).text

    def getTextdataInterface1StatsBytesSend(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_interface1statsbytessend_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_interface1statsbytessend_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_interface1statsbytessend_xpath).text

    def getTextdataInterface2StatsBytesSend(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_interface2statsbytessend_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_interface2statsbytessend_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_interface2statsbytessend_xpath).text

    def setSecurityPassword(self, i, value):
        # time.sleep(2)
        temp_xpath = '//input[@paramname="Device.WiFi.AccessPoint.' + str(i) + '.Security.KeyPassphrase"]'
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).clear()
            self.driver.find_element(By.XPATH, temp_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_securitykeypassphrase_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_securitykeypassphrase_xpath).send_keys(value)'''

    '''def setSecurityModeEnabled(self, value):
        self.driver.find_element(By.XPATH, self.textbox_securitymodeenabled_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_securitymodeenabled_xpath).send_keys(value)
'''
    def ClickTableHeadSSIDNo(self, i):
        tempSSIDNo_xpath = "//tbody/tr/td/span[@fullname='Device.WiFi.SSID." + str(i) + ".']/../img"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSIDNo_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempSSIDNo_xpath).click()
        # self.driver.find_element(By.XPATH, tempSSIDNo_xpath).click()

    def ClickTableDataSSIDStats(self, i):
        tempSSIDStats_xpath = "//span[@fullname='Device.WiFi.SSID." + str(i) + ".Stats.']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, tempSSIDStats_xpath)))
        finally:
            self.driver.find_element(By.XPATH, tempSSIDStats_xpath).click()
        # self.driver.find_element(By.XPATH, tempSSIDStats_xpath).click()

    def getTextdataSSIDStatsBytesReceived(self, i):
        textdata_ssidstatsbytesreceived_xpath = "//span[@tiptext='Device.WiFi.SSID." + str(i) + ".Stats.BytesReceived']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, textdata_ssidstatsbytesreceived_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, textdata_ssidstatsbytesreceived_xpath).text
        # return self.driver.find_element(By.XPATH, textdata_ssidstatsbytesreceived_xpath).text

    def getTextdataSSIDStatsBytesSent(self, i):
        textdata_ssidstatsbytessent_xpath = "//span[@tiptext='Device.WiFi.SSID." + str(i) + ".Stats.BytesSent']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, textdata_ssidstatsbytessent_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, textdata_ssidstatsbytessent_xpath).text
        # return self.driver.find_element(By.XPATH, textdata_ssidstatsbytessent_xpath).text

    def getTextdataSSIDStatsPacketsReceived(self, i):
        textdata_ssidstatspacketsreceived_xpath = "//span[@tiptext='Device.WiFi.SSID." + str(i) + ".Stats.PacketsReceived']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, textdata_ssidstatspacketsreceived_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, textdata_ssidstatspacketsreceived_xpath).text
        # return self.driver.find_element(By.XPATH, textdata_ssidstatspacketsreceived_xpath).text

    def getTextdataSSIDStatsPacketsSent(self, i):
        textdata_ssidstatspacketssent_xpath = "//span[@tiptext='Device.WiFi.SSID." + str(i) + ".Stats.PacketsSent']/../../td[2]"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, textdata_ssidstatspacketssent_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, textdata_ssidstatspacketssent_xpath).text
        # return self.driver.find_element(By.XPATH, textdata_ssidstatspacketssent_xpath).text

    def clickTableheadDNS(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dns_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dns_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_dns_xpath).click()

    def clickTableheadDNSClient(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dnsClient_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dnsClient_xpath).click()

    def clickTableheadDNSClientServer(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dnsClientServer_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dnsClientServer_xpath).click()

    def clickTabledataDNSClientServerServer1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_dnsClientServerServer1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_dnsClientServerServer1_xpath).click()

    def setDNSServer1DNSSERVER(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dnsserver1DNSSERVER_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dnsserver1DNSSERVER_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dnsserver1DNSSERVER_xpath).send_keys(value)

    def clickTableheadDNSDiagnostics(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_dnsdiagnostics_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_dnsdiagnostics_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_dnsdiagnostics_xpath).click()

    def clickTabledataNSLookupDiagnostics(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_nslookupdiagnostics_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_nslookupdiagnostics_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_nslookupdiagnostics_xpath).click()

    def clickTableheadNSLookupDiagnostics(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_nslookupdiagnostics_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_nslookupdiagnostics_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_nslookupdiagnostics_xpath).click()

    def clickTabledataDNSResult(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_dnsresult_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_dnsresult_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_dnsresult_xpath).click()

    def setDNSDiagnosticState(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dnsdiagnosticstate_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dnsdiagnosticstate_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dnsdiagnosticstate_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dnsdiagnosticstate_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dnsdiagnosticstate_xpath).send_keys(value)'''

    def setDNSHostName(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dnshostname_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dnshostname_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dnshostname_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dnshostname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dnshostname_xpath).send_keys(value)'''

    def setDNSNoOfRepetitions(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_dnsnoofrepetitions_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_dnsnoofrepetitions_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_dnsnoofrepetitions_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_dnsnoofrepetitions_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dnsnoofrepetitions_xpath).send_keys(value)'''

    def clickTabledataWANGponLinkConfig(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_wangponlinkconfig_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_wangponlinkconfig_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_wangponlinkconfig_xpath).click()

    def setVLANIDMark(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_vlanidmark_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_vlanidmark_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_vlanidmark_xpath).send_keys(value)
        '''self.driver.find_element(By.XPATH, self.textbox_vlanidmark_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_vlanidmark_xpath).send_keys(value)
'''
    def clickTableheadIP(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ip_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ip_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ip_xpath).click()

    def clickTableheadIPInterface(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ipinterface_xpath).click()

    def clickTableheadIPInterface1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface1_xpath).click()

    def clickTableheadIPInterface1IPv4(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface1ipv4_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface1ipv4_xpath).click()

    def clickTabledataIPInterface1IPv41(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_ipinterface1ipv41_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_ipinterface1ipv41_xpath).click()

    def getTextdataIPInterface1IPv41(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_ipinterface1ipv41_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_ipinterface1ipv41_xpath).text

    def clickTableheadIPInterface1IPv6(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface1ipv6_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface1ipv6_xpath).click()

    def clickTabledataIPInterface1IPv61(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_ipinterface1ipv61_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_ipinterface1ipv61_xpath).click()

    def getTextdataIPInterface1IPv61(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_ipinterface1ipv61_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_ipinterface1ipv61_xpath).text

    def clickTableheadIPInterface2(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface2_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface2_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ipinterface2_xpath).click()

    def clickTableheadIPInterface2IPv4(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface2ipv4_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface2ipv4_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ipinterface2ipv4_xpath).click()

    def clickTabledataIPInterface2IPv41(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_ipinterface2ipv41_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_ipinterface2ipv41_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_ipinterface2ipv41_xpath).click()

    def getTextdataIPInterface2IPv41(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_ipinterface2ipv41_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_ipinterface2ipv41_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_ipinterface2ipv4_xpath).text

    def clickTableheadIPInterface2IPv6(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_ipinterface2ipv6_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_ipinterface2ipv6_xpath).click()
        # self.driver.find_element(By.XPATH, self.tablehead_ipinterface2ipv6_xpath).click()

    def clickTabledataIPInterface2IPv61(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_ipinterface2ipv61_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_ipinterface2ipv61_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_ipinterface2ipv61_xpath).click()

    def getTextdataIPInterface2IPv61(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_ipinterface2ipv61_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_ipinterface2ipv61_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_ipinterface2ipv6_xpath).text

    def clickTableheadIPDiagnostics(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_IPDiagnostics_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_IPDiagnostics_xpath).click()

    def clickTableheadIPDiagnosticsTraceRoute(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_IPDiagnosticsTraceRoute_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_IPDiagnosticsTraceRoute_xpath).click()

    def clickTabledataIPDiagnosticsTraceRoute(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_IPDiagnosticsTraceRoute_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_IPDiagnosticsTraceRoute_xpath).click()

    def setIPDiagnosticsTraceRouteDiagnosticsState(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_IPDiagnosticsTraceRouteDiagnosticsState_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteDiagnosticsState_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteDiagnosticsState_xpath).send_keys(value)

    def setIPDiagnosticsTraceRouteHost(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_IPDiagnosticsTraceRouteHost_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteHost_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteHost_xpath).send_keys(value)

    def setIPDiagnosticsTraceRouteProtocolVersion(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_IPDiagnosticsTraceRouteProtocolVersion_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteProtocolVersion_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteProtocolVersion_xpath).send_keys(value)

    def setIPDiagnosticsTraceRouteMaxHopCount(self, value):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.textbox_IPDiagnosticsTraceRouteMaxHopCount_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteMaxHopCount_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_IPDiagnosticsTraceRouteMaxHopCount_xpath).send_keys(value)

    def clickTabledataHosts(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_hosts_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_hosts_xpath).click()
        # self.driver.find_element(By.XPATH, self.tabledata_hosts_xpath).click()

    def getTextdataHostNoOfEntries(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_hostnoofentries_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_hostnoofentries_xpath).text
        # return self.driver.find_element(By.XPATH, self.textdata_hostnoofentries_xpath).text

    def getDeviceHistory(self):
        # time.sleep(3)
        list_devicehistory = []
        self.driver.switch_to.default_content()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@nameinner="Device History"]')))
        finally:
            self.driver.find_element(By.XPATH, '//span[@nameinner="Device History"]').click()
        # time.sleep(3)
        self.driver.switch_to.frame("frmDesktop")

        j = 2
        while True:
            try:
                # element = self.driver.find_element(By.XPATH, '//table[@id="tblItems"]/tbody/tr[' + str(j) + ']/td[1]')
                element = self.wait.until(EC.presence_of_element_located((By.XPATH, '//table[@id="tblItems"]/tbody/tr[' + str(j) + ']/td[1]')))
                devicehistory = element.get_attribute('innerHTML')
                # time.sleep(1)
                list_devicehistory.append(devicehistory)
                j += 1
            except (common.exceptions.NoSuchElementException, common.exceptions.StaleElementReferenceException, common.exceptions.TimeoutException):
                break
        return list_devicehistory

    def switch_to_DesktopFrame(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frmDesktop")))
        finally:
            self.driver.switch_to.frame("frmDesktop")

    def switch_to_ButtonFrame(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frmButtons")))
        finally:
            self.driver.switch_to.frame("frmButtons")

    def clickTabledataDevice(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_Device_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_Device_xpath).click()

    def getTextdataDeviceInterfaceStackNumberOfEntries(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_DeviceInterfaceStackNumberOfEntries_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_DeviceInterfaceStackNumberOfEntries_xpath).text

    def clickTableheadRouting(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_Routing_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_Routing_xpath).click()

    def clickTableheadRoutingRouter(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_RoutingRouter_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_RoutingRouter_xpath).click()

    def clickTableheadRoutingRouter1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_RoutingRouter1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_RoutingRouter1_xpath).click()

    def clickTabledataRoutingRouter1(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tabledata_RoutingRouter1_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tabledata_RoutingRouter1_xpath).click()

    def getRoutingRouter1Enable(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.textdata_RoutingRouter1Enable_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, self.textdata_RoutingRouter1Enable_xpath).text

    def clickTableheadRoutingRouter1IPv4Forwarding(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tablehead_RoutingRouter1IPv4Forwarding_xpath)))
        finally:
            self.driver.find_element(By.XPATH, self.tablehead_RoutingRouter1IPv4Forwarding_xpath).click()

    def clickTabledataRoutingRouter1IPv4ForwardingIndex(self, i):
        temp_xpath = "//span[@fullname='Device.Routing.Router.1.IPv4Forwarding." + str(i) + ".']"
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, temp_xpath)))
        finally:
            self.driver.find_element(By.XPATH, temp_xpath).click()

    def getRoutingRouter1IPv4ForwardingIndexStaticRoute(self, i):
        temp_xpath = "//span[@tiptext='Device.Routing.Router.1.IPv4Forwarding." + str(i) + ".StaticRoute']/../../td[2]"
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, temp_xpath)))
        finally:
            return self.driver.find_element(By.XPATH, temp_xpath).text
