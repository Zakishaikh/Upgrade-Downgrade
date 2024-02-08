# from datetime import datetime, timedelta
# from time import sleep
import sys
import PySimpleGUI as sg
import configparser
from os.path import exists

config = configparser.ConfigParser()
path = ".\\Configurations\\SSIDConfig.ini"
sg.theme('GreenMono')


class ssidconfigCheck:

    @staticmethod
    def changeconfig(l):
        layout = [
            [sg.Text('Enter Name for SSID 1')],
            [sg.InputText(default_text=l[0])],
            [sg.Text('Enter Name for SSID 2')],
            [sg.InputText(default_text=l[1])],
            [sg.Text('Enter Name for SSID 3')],
            [sg.InputText(default_text=l[2])],
            [sg.Text('Enter Name for SSID 4')],
            [sg.InputText(default_text=l[3])],
            [sg.Text('Enter Name for SSID 5')],
            [sg.InputText(default_text=l[4])],
            [sg.Text('Enter Name for SSID 6')],
            [sg.InputText(default_text=l[5])],
            [sg.Text('Enter Password for SSID 1')],
            [sg.InputText(default_text=l[6])],
            [sg.Text('Enter Password for SSID 2')],
            [sg.InputText(default_text=l[7])],
            [sg.Text('Enter Password for SSID 3')],
            [sg.InputText(default_text=l[8])],
            [sg.Text('Enter Password for SSID 4')],
            [sg.InputText(default_text=l[9])],
            [sg.Text('Enter Password for SSID 5')],
            [sg.InputText(default_text=l[10])],
            [sg.Text('Enter Password for SSID 6')],
            [sg.InputText(default_text=l[11])],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Enter Below Details to change Config', layout)
        event, values = window.read()
        window.close()
        ssidname_1 = str(values[0])
        ssidname_2 = str(values[1])
        ssidname_3 = str(values[2])
        ssidname_4 = str(values[3])
        ssidname_5 = str(values[4])
        ssidname_6 = str(values[5])
        ssidpassword_1 = str(values[6])
        ssidpassword_2 = str(values[7])
        ssidpassword_3 = str(values[8])
        ssidpassword_4 = str(values[9])
        ssidpassword_5 = str(values[10])
        ssidpassword_6 = str(values[11])
        # print(values)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            sys.exit()

        if ssidname_1 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_1", ssidname_1)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_1", l[0])

        if ssidname_2 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_2", ssidname_2)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_2", l[1])

        if ssidname_3 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_3", ssidname_3)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_3", l[2])

        if ssidname_4 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_4", ssidname_4)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_4", l[3])

        if ssidname_5 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_5", ssidname_5)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_5", l[4])

        if ssidname_6 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidname_6", ssidname_6)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidname_6", l[5])

        if ssidpassword_1 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_1", ssidpassword_1)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_1", l[6])

        if ssidpassword_2 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_2", ssidpassword_2)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_2", l[7])

        if ssidpassword_3 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_3", ssidpassword_3)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_3", l[8])

        if ssidpassword_4 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_4", ssidpassword_4)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_4", l[9])

        if ssidpassword_5 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_5", ssidpassword_5)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_5", l[10])

        if ssidpassword_6 != '':
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_6", ssidpassword_6)
        else:
            config.set("Home_Gateway_Automation_SSID", "ssidpassword_6", l[11])

        with open(path, "w") as config_file:
            config.write(config_file)

    @staticmethod
    def createconfig():
        layout = [
            [sg.Text('Enter Name for SSID 1')],
            [sg.InputText()],
            [sg.Text('Enter Name for SSID 2')],
            [sg.InputText()],
            [sg.Text('Enter Name for SSID 3')],
            [sg.InputText()],
            [sg.Text('Enter Name for SSID 4')],
            [sg.InputText()],
            [sg.Text('Enter Name for SSID 5')],
            [sg.InputText()],
            [sg.Text('Enter Name for SSID 6')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 1')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 2')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 3')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 4')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 5')],
            [sg.InputText()],
            [sg.Text('Enter Password for SSID 6')],
            [sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('Enter Below Details to create Config', layout)
        event, values = window.read()
        window.close()
        ssidname_1 = str(values[0])
        ssidname_2 = str(values[1])
        ssidname_3 = str(values[2])
        ssidname_4 = str(values[3])
        ssidname_5 = str(values[4])
        ssidname_6 = str(values[5])
        ssidpassword_1 = str(values[6])
        ssidpassword_2 = str(values[7])
        ssidpassword_3 = str(values[8])
        ssidpassword_4 = str(values[9])
        ssidpassword_5 = str(values[10])
        ssidpassword_6 = str(values[11])

        if event == sg.WIN_CLOSED or event == 'Cancel':
            sys.exit()

        if ssidname_1 == '' or ssidname_2 == '' or ssidname_3 == '' or ssidname_4 == '' or ssidname_5 == '' or ssidname_6 == '' or ssidpassword_1 == '' or ssidpassword_2 == '' or ssidpassword_3 == '' or ssidpassword_4 == '' or ssidpassword_5 == '' or ssidpassword_6 == '':
            sg.popup('Can\'t leave any boxes empty.')
            ssidconfigCheck.createconfig()

        config.add_section("Home_Gateway_Automation_Env")
        config.set("Home_Gateway_Automation_SSID", "ssidname_1", ssidname_1)
        config.set("Home_Gateway_Automation_SSID", "ssidname_2", ssidname_2)
        config.set("Home_Gateway_Automation_SSID", "ssidname_3", ssidname_3)
        config.set("Home_Gateway_Automation_SSID", "ssidname_4", ssidname_4)
        config.set("Home_Gateway_Automation_SSID", "ssidname_5", ssidname_5)
        config.set("Home_Gateway_Automation_SSID", "ssidname_6", ssidname_6)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_1", ssidpassword_1)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_2", ssidpassword_2)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_3", ssidpassword_3)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_4", ssidpassword_4)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_5", ssidpassword_5)
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_6", ssidpassword_6)
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
            l = [config.get("Home_Gateway_Automation_SSID", "ssidname_1"),
                 config.get("Home_Gateway_Automation_SSID", "ssidname_2"),
                 config.get("Home_Gateway_Automation_SSID", "ssidname_3"),
                 config.get("Home_Gateway_Automation_SSID", "ssidname_4"),
                 config.get("Home_Gateway_Automation_SSID", "ssidname_5"),
                 config.get("Home_Gateway_Automation_SSID", "ssidname_6"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_1"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_2"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_3"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_4"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_5"),
                 config.get("Home_Gateway_Automation_SSID", "ssidpassword_6")]
            # print(l)
            ssidconfigCheck.changeconfig(l)
            ssidconfigCheck.configfound()
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
                ssidconfigCheck.createconfig()
                ssidconfigCheck.configfound()
            elif event == sg.WIN_CLOSED or event == 'Cancel':
                sys.exit()
        except configparser.DuplicateSectionError:
            pass

    @staticmethod
    def configCheck():
        if exists(path):
            ssidconfigCheck.configfound()
        else:
            ssidconfigCheck.confignotfound()
