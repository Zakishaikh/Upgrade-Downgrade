import os

import pytest
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from selenium import common
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import traceback
from utilities.outputVariables import *


# Hfilename=[]
def __init__(self, driver):
    self.driver = driver


@pytest.fixture()
def setup():
    try:
        # ser = Service(executable_path=ChromeDriverManager().install())
        ser = Service(".\\chromedriver.exe")
        op = webdriver.ChromeOptions()
        op.add_argument('--ignore-certificate-errors-spki-list')
        op.add_argument('--ignore-ssl-errors')
        # op.add_argument('log-level=3')
        s = webdriver.Chrome(service=ser, options=op)
    except common.exceptions.WebDriverException:
        print(traceback.format_exc())
        print("Chrome Driver Error")
        print("Trying to start Chrome Again")
        try:
            ser = Service(".\\chromedriver.exe")
            op = webdriver.ChromeOptions()
            op.add_argument('--ignore-certificate-errors-spki-list')
            op.add_argument('--ignore-ssl-errors')
            # op.add_argument('log-level=3')
            s = webdriver.Chrome(service=ser, options=op)
        except common.exceptions.WebDriverException:
            print(traceback.format_exc())
            print("Chrome Driver Error")
            print("Chrome Start Failed")
        else:
            return s
    else:
        return s


@pytest.fixture()
def setup1():
    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()
    return driver


#######Pytest HTML Report ############
def pytest_configure(config):
    config._metadata['Project Name'] = "HGW Automation"
    config._metadata['Module Name'] = "Update SSID"
    config._metadata['Tester'] = "TOP VOD Apps Team"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Tester", None)


def pytest_html_report_title(report):
    # reportdatetime.append(str(datetime.now().strftime("%d%m%Y%H%M")))

    report.title = 'JIO_HGWAutomation_HTMLReport_' + str(str_localtime) + ''


def pytest_configure(config):
    # to remove environment section
    # htmldatetime = str(datetime.now().strftime("%d%m%Y%H%M"))
    config._metadata = None

    if not os.path.exists('Reports'):
        os.makedirs('Reports')

    config.option.htmlpath = 'Reports/' 'JIO_HGWAutomation_HTMLReport_' + str(str_localtime) + ".html"
    print("HTML File name as below conftest")

    # Hfilename1 = '.\\Reports\\' 'JIO_HGWAutomation_HTMLReport_' + str(str_localtime) + '.html'
    # Hfilename.append(Hfilename1)
    @staticmethod
    def mailAlert1(toMail, filename):
        try:
            upload_URL = 'http://10.135.141.141:5000/Mail_alert_HGW_API'
            multipart_data = MultipartEncoder(
                fields={
                    # a file upload field
                    'upload': (filename, open(filename, 'rb')),

                    # plain text fields
                    'To': toMail

                }
            )

            headers = {'Content-Type': multipart_data.content_type}
            response = requests.post(upload_URL, data=multipart_data, headers=headers, timeout=30.000)
            print(response.text)
            print(response.status_code)
        except requests.exceptions.ConnectionError:
            print('This Site Can\'t be reached')

    #   mailAlert(toMail, filename)
    #  mailAlert(toMail, file)
