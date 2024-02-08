import configparser
from datetime import datetime
from utilities.ReadTestData import SSIDConfigGet


def logger(log_message):
    date_time = datetime.now()
    print("\n[" + str(date_time) + "] " + str(log_message))
    return


config = configparser.ConfigParser()


class SSIDConfigSet:

    config.read(".\\Configurations\\SSIDConfig.ini")

    @staticmethod
    def setSSIDNAME(i, ssid):
        ssid = ssid.replace(' ', '[space]')
        path1 = '.\\Configurations\\SSIDConfig.ini'
        config.set("Home_Gateway_Automation_SSID", "ssidname_" + str(i), ssid)
        with open(path1, "w") as config_file:
            config.write(config_file)

    @staticmethod
    def setSSIDPASSWORD(i, password):
        password = password.replace(' ', '[space]')
        path1 = '.\\Configurations\\SSIDConfig.ini'
        config.set("Home_Gateway_Automation_SSID", "ssidpassword_" + str(i), password)
        with open(path1, "w") as config_file:
            config.write(config_file)