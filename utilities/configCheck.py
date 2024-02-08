# from datetime import datetime, timedelta
# from time import sleep
import sys
import PySimpleGUI as sg
import configparser
from os.path import exists

config = configparser.ConfigParser()
path = ".\\Configurations\\HGWAutomationConfig.ini"
sg.theme('GreenMono')


class configCheck:

    @staticmethod
    def changeconfig(l):
        acslist = ["Rancore ACS", "IOT ACS"]
        layout = [
            [sg.Text('Select ACS Server you want to perform')],
            [sg.Combo(acslist, size=(43, 20), default_value=l[0], readonly=True)],
            [sg.Text('Enter UserName of ACS Server')],
            [sg.InputText(default_text=l[1])],
            [sg.Text('Enter Password of ACS Server')],
            [sg.InputText(default_text=l[2])],
            [sg.Text('Enter UserName of DUT GUI')],
            [sg.InputText(default_text=l[3])],
            [sg.Text('Enter Password of DUT GUI')],
            [sg.InputText(default_text=l[4])],
            [sg.Text('Enter Serial Number Of Your DUT')],
            [sg.InputText(default_text=l[5])],
            [sg.Text('Enter SSID Number for which you want to omit the Edit parameter')],
            [sg.InputText(default_text=l[6])],
            [sg.Text('Enter Destination Email Ids seperated by semicolon (;)')],
            [sg.InputText(default_text=l[7])],
            [sg.Text('Enter Factory Reset Password Of Your DUT')],
            [sg.InputText(default_text=l[8])],
            [sg.Text('Enter DUT GUI URL')],
            [sg.InputText(default_text=l[9])],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Enter Below Details to change Config', layout)
        event, values = window.read()
        window.close()
        ACSURLType = str(values[0])
        UserName_ACS = str(values[1])
        Password_ACS = str(values[2])
        UserName_HGW = str(values[3])
        Password_HGW = str(values[4])
        serial_no = str(values[5])
        omitssid = str(values[6])
        tomail = str(values[7])
        factory_pass = str(values[8])
        ont_ip = str(values[9])
        # print(values)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            sys.exit()

        if ACSURLType != '':
            config.set("Home_Gateway_Automation_Env", "acsurltype", ACSURLType)
        else:
            config.set("Home_Gateway_Automation_Env", "acsurltype", l[0])

        if UserName_ACS != '':
            config.set("Home_Gateway_Automation_Env", "username_acs", UserName_ACS)
        else:
            config.set("Home_Gateway_Automation_Env", "username_acs", l[1])

        if Password_ACS != '':
            config.set("Home_Gateway_Automation_Env", "password_acs", Password_ACS)
        else:
            config.set("Home_Gateway_Automation_Env", "password_acs", l[2])

        if UserName_HGW != '':
            config.set("Home_Gateway_Automation_Env", "username_hgw", UserName_HGW)
        else:
            config.set("Home_Gateway_Automation_Env", "username_hgw", l[3])

        if Password_HGW != '':
            config.set("Home_Gateway_Automation_Env", "password_hgw", Password_HGW)
        else:
            config.set("Home_Gateway_Automation_Env", "password_hgw", l[4])

        if serial_no != '':
            config.set("Home_Gateway_Automation_Env", "serial_no", serial_no)
        else:
            config.set("Home_Gateway_Automation_Env", "serial_no", l[5])

        config.set("Home_Gateway_Automation_Env", "omitssid", omitssid)

        if tomail != '':
            config.set("Home_Gateway_Automation_Env", "tomail", tomail)
        else:
            config.set("Home_Gateway_Automation_Env", "tomail", l[7])

        if factory_pass != '':
            config.set("Home_Gateway_Automation_Env", "factory_pass", factory_pass)
        else:
            config.set("Home_Gateway_Automation_Env", "factory_pass", l[8])

        if ont_ip != '':
            config.set("Home_Gateway_Automation_Env", "ont_ip", ont_ip)
        else:
            config.set("Home_Gateway_Automation_Env", "ont_ip", l[9])

        with open(path, "w") as config_file:
            config.write(config_file)

    @staticmethod
    def createconfig():
        acslist = ["Rancore ACS", "IOT ACS"]
        layout = [
            [sg.Text('Select ACS Server you want to perform')],
            [sg.Combo(acslist, size=(43, 20), default_value="Rancore ACS", readonly=True)],
            [sg.Text('Enter UserName of ACS Server')],
            [sg.InputText()],
            [sg.Text('Enter Password of ACS Server')],
            [sg.InputText()],
            [sg.Text('Enter UserName of DUT GUI')],
            [sg.InputText()],
            [sg.Text('Enter Password of DUT GUI')],
            [sg.InputText()],
            [sg.Text('Enter Serial Number Of Your DUT')],
            [sg.InputText()],
            [sg.Text('Enter SSID Number for which you want to omit the Edit parameter')],
            [sg.InputText()],
            [sg.Text('Enter Destination Email Ids seperated by semicolon (;)')],
            [sg.InputText()],
            [sg.Text('Enter Factory Reset Password Of Your DUT')],
            [sg.InputText()],
            [sg.Text('Enter DUT GUI URL')],
            [sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Enter Below Details to create Config', layout)
        event, values = window.read()
        window.close()
        ACSURLType = str(values[0])
        UserName_ACS = str(values[1])
        Password_ACS = str(values[2])
        UserName_HGW = str(values[3])
        Password_HGW = str(values[4])
        serial_no = str(values[5])
        omitssid = str(values[6])
        tomail = str(values[7])
        factory_pass = str(values[8])
        ont_ip = str(values[9])

        if event == sg.WIN_CLOSED or event == 'Cancel':
            sys.exit()

        if UserName_ACS == '' or Password_ACS == '' or UserName_HGW == '' or Password_HGW == '' or serial_no == '' or tomail == '' or factory_pass == '' or ont_ip == '':
            sg.popup('Can\'t leave any boxes empty except Omit SSID.')
            configCheck.createconfig()

        config.add_section("Home_Gateway_Automation_Env")
        config.set("Home_Gateway_Automation_Env", "acsurltype", ACSURLType)
        config.set("Home_Gateway_Automation_Env", "username_acs", UserName_ACS)
        config.set("Home_Gateway_Automation_Env", "password_acs", Password_ACS)
        config.set("Home_Gateway_Automation_Env", "username_hgw", UserName_HGW)
        config.set("Home_Gateway_Automation_Env", "password_hgw", Password_HGW)
        config.set("Home_Gateway_Automation_Env", "serial_no", serial_no)
        config.set("Home_Gateway_Automation_Env", "omitssid", omitssid)
        config.set("Home_Gateway_Automation_Env", "tomail", tomail)
        config.set("Home_Gateway_Automation_Env", "factory_pass", factory_pass)
        config.set("Home_Gateway_Automation_Env", "ont_ip", ont_ip)
        with open(path, "w") as config_file:
            config.write(config_file)

    @staticmethod
    def configfound():
        f = open(path, "r")
        layout = [
            [sg.Text(f.read(), font='Any 15')],
            [sg.Button('Change', key='Change'), sg.Button('Continue'), sg.Cancel()]
        ]
        window = sg.Window('Config Found', layout)
        event, values = window.read()
        window.close()
        if event == 'Change':
            config.read(path)
            l = [config.get("Home_Gateway_Automation_Env", "acsurltype"),
                 config.get("Home_Gateway_Automation_Env", "username_acs"),
                 config.get("Home_Gateway_Automation_Env", "password_acs"),
                 config.get("Home_Gateway_Automation_Env", "username_hgw"),
                 config.get("Home_Gateway_Automation_Env", "password_hgw"),
                 config.get("Home_Gateway_Automation_Env", "serial_no"),
                 config.get("Home_Gateway_Automation_Env", "omitssid"),
                 config.get("Home_Gateway_Automation_Env", "tomail"),
                 config.get("Home_Gateway_Automation_Env", "factory_pass"),
                 config.get("Home_Gateway_Automation_Env", "ont_ip")]
            # print(l)
            configCheck.changeconfig(l)
            configCheck.configfound()
        elif event == 'Continue':
            pass
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            sys.exit()

    @staticmethod
    def confignotfound():
        try:
            layout = [
                [sg.Text('Config File Not Found. To create one press Create.', font='Any 15')],
                [sg.Button('Create', key='Create'), sg.Cancel()]
            ]
            window = sg.Window('Config Not Found', layout)
            event, values = window.read()
            window.close()
            if event == 'Create':
                configCheck.createconfig()
                configCheck.configfound()
            elif event == sg.WIN_CLOSED or event == 'Cancel':
                sys.exit()
        except configparser.DuplicateSectionError:
            pass

    @staticmethod
    def configCheck():
        if exists(path):
            configCheck.configfound()
        else:
            configCheck.confignotfound()
