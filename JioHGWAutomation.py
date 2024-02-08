import os
import shutil
import subprocess
import sys

import PySimpleGUI as sg

from utilities.ReadTestData import ReadTestData
from utilities.commonmethod import commonmethod
from utilities.configCheck import configCheck
from utilities.customLogger import LogGen
from utilities.ssidconfigCheck import ssidconfigCheck

logger = LogGen.loggen()
configCheck.configCheck()
ssidconfigCheck.configCheck()
toMail = ReadTestData.toMail()

Reports = ".//Reports//"
Excel = ".//Excel//"
if os.path.exists(Reports):
    shutil.rmtree(Reports)
    print("Reports Folder deleted")
else:
    print("Report folder is not available")

if os.path.exists(Excel):
    shutil.rmtree(Excel)
    print("Excel Folder deleted")
else:
    print("Excel folder is not available")
# shutil.rmtree(".//Reports//")
# shutil.rmtree(".//Excel//")
layout = [
    [sg.Text('Select One Automation Module:')],
    [sg.Checkbox("TR069"), sg.Checkbox("WIFI"), sg.Checkbox("Specific Testcases (Sanity)")],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Enter Below Details:', layout)
event, values = window.read()
window.close()

if event != 'Submit':
    sys.exit()

index = 0
if values[index]:
    logger.info('********************* SANITY TESTING STARTED *********************')
    deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                  capture_output=True)
    deviceAttached = str(deviceStatus.stdout.decode())
    print(deviceAttached)
    # print(" Device connected for adb")
    if len(deviceAttached) == 28:
        print('Device Not Connected. Please Connect an Android 11/12 Phone.')
        sys.exit()
    # command= "pytest -v --capture=tee-sys --html=Reports\reports.html ./testCases/Test_TR069_40_45.py"
    command = "pytest --capture=tee-sys -m \"complete\" --html=Reports/reports.html ./testCases/"

    p2 = subprocess.call(command, shell=True)
    for hfile in os.listdir(".//Reports//"):
        if hfile.startswith("JIO_HGWAutomation_"):
            print(hfile)
            # htfile=str(hfile)
            path = ".//Reports//"
            htfile = path + hfile
            print("HTML file")
            print(htfile)
            commonmethod.mailAlert(str(toMail), str(htfile))

    for efile in os.listdir(".//Excel//"):
        if efile.startswith("JIO_HGWAutomation_"):
            print(efile)
            # exfile=str(efile)
            path = ".//Excel//"
            exfile = path + efile
            print("EXCEL file")
            print(exfile)
            commonmethod.mailAlert(str(toMail), str(exfile))
    logger.info('********************* SANITY TESTING FINISHED *********************')

index += 1
if values[index]:
    logger.info('********************* WIFI TESTING STARTED *********************')
    deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                  capture_output=True)
    deviceAttached = str(deviceStatus.stdout.decode())
    print(deviceAttached)
    # print(" Device connected for adb")
    if len(deviceAttached) == 28:
        print('Device Not Connected. Please Connect an Android 11/12 Phone.')
        sys.exit()

    command = "pytest --capture=tee-sys -m \"wifi\" --html=Reports/reports.html ./testCases/"

    p2 = subprocess.call(command, shell=True)
    for hfile in os.listdir(".//Reports//"):
        if hfile.startswith("JIO_HGWAutomation_"):
            print(hfile)
            # htfile=str(hfile)
            path = ".//Reports//"
            htfile = path + hfile
            print("HTML file")
            print(htfile)
            commonmethod.mailAlert(str(toMail), str(htfile))

    for efile in os.listdir(".//Excel//"):
        if efile.startswith("JIO_HGWAutomation_"):
            print(efile)
            # exfile=str(efile)
            path = ".//Excel//"
            exfile = path + efile
            print("EXCEL file")
            print(exfile)
            commonmethod.mailAlert(str(toMail), str(exfile))
    logger.info('********************* WIFI TESTING FINISHED *********************')

index += 1
if values[index]:
    # report_name = "JIO_HGWAutomation_HTMLReport_" + str_localtime  # Current date time in local system
    list_testcase = ['01', '02', '03', '04', '05', '06', '07', '08', '18', '19', '20', '21', '22', '23', '24', '25',
                     '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41',
                     '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57',
                     '58', '59', '60', '61', '62', '63', '64', '65']
    layout = [
        [sg.Text('Select Testcases you want to perform')],
        [sg.Combo(list_testcase, size=(43, 20), default_value="01", readonly=True)],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Specific Testcases to run', layout)
    event, values = window.read()
    window.close()
    str_userinput = str(values[0])
    str_testcasepath = "testCases/Test_WIFI_" + str_userinput + ".py"
    if event == sg.WIN_CLOSED or event == 'Cancel':
        sys.exit()
    elif os.path.exists(str_testcasepath):
        logger.info('********************* SANITY ' + str_userinput + ' TESTING STARTED *********************')
        # print(str_testcasepath)
        command = "pytest -v --capture=tee-sys --html=Reports/reports.html " + str_testcasepath
        p2 = subprocess.call(command, shell=True)

        for hfile in os.listdir(".//Reports//"):
            if hfile.startswith("JIO_HGWAutomation_"):
                print(hfile)
                # htfile=str(hfile)
                path = ".//Reports//"
                htfile = path + hfile
                print("HTML file")
                print(htfile)
                commonmethod.mailAlert(str(toMail), str(htfile))

        for efile in os.listdir(".//Excel//"):
            if efile.startswith("JIO_HGWAutomation_"):
                print(efile)
                # exfile=str(efile)
                path = ".//Excel//"
                exfile = path + efile
                print("EXCEL file")
                print(exfile)
                commonmethod.mailAlert(str(toMail), str(exfile))
        logger.info('********************* SANITY ' + str_userinput + ' TESTING FINISHED *********************')
    else:
        print("Testcases not available.")

if index == '':
    flag = 0
    # logger("Plz Select atleast 1 sheet to continue")
    sys.exit()
