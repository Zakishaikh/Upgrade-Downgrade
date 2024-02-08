import configparser
from datetime import datetime


def logger(log_message):
    date_time = datetime.now()
    print("\n[" + str(date_time) + "] " + str(log_message))
    return


config = configparser.ConfigParser()
ACSURL = {"Rancore ACS": "http://10.64.218.26/CpeAdmin/Login.aspx",
          "IOT ACS": "http://iotacs.jioconnect.com/CpeAdmin/Login.aspx"}


class ReadTestData:
    """if not exists(".\\Configurations\\HGWAutomationConfig.ini"):
        # config = configparser.ConfigParser()
        print("Config file not available enter data ")
        try:
            acslist = ["Rancore ACS", "IOT ACS"]
            layout = [
                [sg.Text('Select ACS Server you want to perform')],
                [sg.Combo(acslist, size=(43, 20), default_value="Rancore ACS", readonly=True)],
                [sg.Text('Enter UserName of ACS Server')],
                [sg.InputText()],
                [sg.Text('Enter Password of ACS Server')],
                [sg.InputText()],
                [sg.Text('Enter UserName of JioFiber Home Gateway Portal ')],
                [sg.InputText()],
                [sg.Text('Enter Password of JioFiber Home Gateway Portal')],
                [sg.InputText()],
                [sg.Text('Enter Serial Number Of Your Router (Home Gateway)')],
                [sg.InputText()],
                [sg.Text('Enter SSID Number for which you want to omit the Edit parameter')],
                [sg.InputText()],
                [sg.Text('Enter Email Id')],
                [sg.InputText()],
                [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window('Enter Below Details:', layout)
            event, values = window.read()
            window.close()
            ACSURLType = str(values[0])
            UserName_ACS = str(values[1])
            Password_ACS = str(values[2])
            UserName_HGW = str(values[3])
            Password_HGW = str(values[4])
            serial_no = str(values[5])
            omitssid = str(values[6])
            emailid = str(values[7])
            if event is None or event == 'Cancel' or UserName_ACS == '' or Password_ACS == '' or UserName_HGW == '' or Password_HGW == '' or serial_no == '':
                sys.exit()
            logger("User Enter Details:-")
            logger("ACS Portal Type : " + str(ACSURLType))
            logger("UserName for ACS Portal : " + UserName_ACS)
            logger("Password for ACS Portal : " + Password_ACS)
            logger("UserName for JioCentrum Portal : " + UserName_HGW)
            logger("Password for JioCentrum Portal : " + Password_HGW)
            logger("Serial Number : " + serial_no)
            logger("SSID number for skipping Edit Paramenter Entered by you : " + omitssid)
            logger("Email ID Entered by you : " + emailid)
            config.add_section("Home_Gateway_Automation_Env")
            config.set("Home_Gateway_Automation_Env", "acsurltype", ACSURLType)
            config.set("Home_Gateway_Automation_Env", "username_acs", UserName_ACS)
            config.set("Home_Gateway_Automation_Env", "password_acs", Password_ACS)
            config.set("Home_Gateway_Automation_Env", "username_hgw", UserName_HGW)
            config.set("Home_Gateway_Automation_Env", "password_hgw", Password_HGW)
            config.set("Home_Gateway_Automation_Env", "serial_no", serial_no)
            config.set("Home_Gateway_Automation_Env", "omitssid", omitssid)
            config.set("Home_Gateway_Automation_Env", "tomail", emailid)
            with open(".\\Configurations\\HGWAutomationConfig.ini", "w") as config_file:
                config.write(config_file)
        except KeyboardInterrupt:
            pass
    else:
        config.read('.\\Configurations\\HGWAutomationConfig.ini')
    """

    config.read('.\\Configurations\\HGWAutomationConfig.ini')

    @staticmethod
    def getACSURL():
        acsurl = str(config.get("Home_Gateway_Automation_Env", "acsurltype"))
        if acsurl == 'Rancore ACS':
            return 'http://10.64.218.26/CpeAdmin/Login.aspx'
        if acsurl == 'IOT ACS':
            return 'http://iotacs.jioconnect.com/CpeAdmin/Login.aspx'

    @staticmethod
    def getUserName():
        UserName_ACS = str(config.get("Home_Gateway_Automation_Env", "username_acs"))
        return UserName_ACS

    @staticmethod
    def getPassword():
        Password_ACS = str(config.get("Home_Gateway_Automation_Env", "password_acs"))
        return Password_ACS

    @staticmethod
    def getSerialno():
        serial_no = str(config.get("Home_Gateway_Automation_Env", "serial_no"))
        return serial_no

    @staticmethod
    def getomitssid():
        omitssid = str(config.get("Home_Gateway_Automation_Env", "omitssid"))
        if "," in omitssid:
            omitssid = omitssid.split(",")
        elif ";" in omitssid:
            omitssid = omitssid.split(";")
        else:
            omitssid = omitssid.split()
        return omitssid

    @staticmethod
    def getHGWURL():
        ont_ip = "http://" + str(config.get("Home_Gateway_Automation_Env", "ont_ip")) + "/login"
        return ont_ip

    @staticmethod
    def getUserNameHGW():
        UserName_HGW = str(config.get("Home_Gateway_Automation_Env", "username_hgw"))
        return UserName_HGW

    @staticmethod
    def getPasswordHGW():
        Password_HGW = str(config.get("Home_Gateway_Automation_Env", "password_hgw"))
        return Password_HGW

    @staticmethod
    def toMail():
        config.read('.\\Configurations\\HGWAutomationConfig.ini')
        toMail = str(config.get("Home_Gateway_Automation_Env", "tomail"))
        return toMail

    @staticmethod
    def getFactoryResetPassword():
        Password = str(config.get("Home_Gateway_Automation_Env", "factory_pass"))
        return Password


class Excel_Env:
    config.read(".\\Configurations\\ExcelConfig.ini")

    @staticmethod
    def getExcelPath():
        path = str(config.get("Excel_Report_Info", "path"))
        return path

    @staticmethod
    def getExcelNewPath():
        new_path = str(config.get("Excel_Report_Info", "new_path"))
        return new_path

    @staticmethod
    def getsheet_name():
        sheet_name = str(config.get("Excel_Report_Info", "sheet_name"))
        return sheet_name

    @staticmethod
    def gettest_name():
        test_name = str(config.get("Excel_Report_Info", "test_name"))
        return test_name


class SSIDConfigGet:

    @staticmethod
    def getSSIDNAME():
        config.read(".\\Configurations\\SSIDConfig.ini")
        list_name = [SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_1")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_2")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_3")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_4")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_5")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_6")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_7")),
                     SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidname_8"))]
        return list_name

    @staticmethod
    def getSSIDPASSWORD():
        config.read(".\\Configurations\\SSIDConfig.ini")
        list_password = [SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_1")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_2")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_3")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_4")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_5")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_6")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_7")),
                         SSIDConfigGet.stringReplace(config.get("Home_Gateway_Automation_SSID", "ssidpassword_8"))]
        return list_password

    @staticmethod
    def stringReplace(s):
        s = s.replace('&amp;', '&')
        s = s.replace('&lt;', '<')
        s = s.replace('&gt;', '>')
        s = s.replace('[space]', ' ')
        return s
