import logging
import subprocess
import sys
import time
import traceback
from datetime import datetime
from time import sleep
import re
import pywintypes
import requests
import win32api
from requests_toolbelt.multipart.encoder import MultipartEncoder

from utilities.customLogger import LogGen

logger = LogGen.loggen()


class commonmethod:

    @staticmethod
    def mac_split(mac):
        x = mac.split(":")
        print(x)
        Mac_Add_split = x[1]
        for i in range(2, 5):
            Mac_Add_split = Mac_Add_split + ':' + x[i]
        # print(Mac_Add_split)
        return Mac_Add_split

    @staticmethod
    def mailAlert(toMail, filename):
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

    @staticmethod
    def logger(log_message):
        date_time = datetime.now()
        print("\n[" + str(date_time) + "] " + str(log_message))
        return

    @staticmethod
    def STB_Text_Event(inputtext):
        p = subprocess.run('adb shell input text ' + inputtext, shell=True, stdin=subprocess.PIPE, capture_output=True)
        p = str(p.stdout.decode())
        if p != '':
            subprocess.run('adb shell input text ' + inputtext)
        else:
            print('Searched text ' + str(inputtext))
            sleep(1)
        return

    @staticmethod
    def STB_Key_Event(keyinput):
        key_action = {'28': 'KEYCODE_CLEAR', '3': 'ACTION_HOME', '4': 'ACTION_BACK', '19': 'ACTION_UP',
                      '20': 'ACTION_DOWN', '21': 'ACTION_LEFT', '22': 'ACTION_RIGHT', 'KEYCODE_HOME': 'ACTION_HOME',
                      'KEYCODE_BACK': 'ACTION_BACK', '23': 'ACTION_OK', '66': 'ACTION_ENTER', '24': 'ACTION_VOLUME_UP',
                      '25': 'ACTION_VOLUME_DOWN'}
        p = subprocess.run('adb shell input keyevent ' + keyinput, shell=True, stdin=subprocess.PIPE,
                           capture_output=True)
        p = str(p.stdout.decode())
        if p != '':
            subprocess.run('adb shell input keyevent ' + keyinput)
        if keyinput in key_action:
            print('KeyEvent { action=' + key_action[keyinput] + ', keyCode=' + keyinput + ' }')
        else:
            print('KeyEvent { keyCode=' + keyinput + ' }')
        sleep(1)
        return

    @staticmethod
    def get_clientSSID_list(ssid_list):
        deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                      capture_output=True)
        print(deviceStatus)
        if 'offline' in str(deviceStatus.stdout):
            logging.info('------ STB OFFLINE ------')
            print('STB OFFLINE')
            sys.exit()

        print(" Device connected for adb")
        subprocess.run('adb shell am force-stop com.rjil.jiostbsetting')
        sleep(2)
        subprocess.run('adb shell am start com.rjil.jiostbsetting/.MainActivity')
        sleep(5)
        commonmethod.STB_Key_Event('19')
        commonmethod.STB_Key_Event('19')
        commonmethod.STB_Key_Event('20')
        # STB_Key_Event('20')
        commonmethod.STB_Key_Event('23')
        commonmethod.STB_Key_Event('23')
        sleep(10)
        s2 = ""
        print(s2)
        for i in range(8):
            subprocess.run("adb shell input keyevent 20")
            sleep(2)
        # sleep(2)
        try:
            z = 0
            st = []
            n2 = []
            o2 = []
            print(o2)
            while True:
                o2 = ",".join(n2)
                print("dump 1")
                dump = subprocess.run("adb shell uiautomator dump", shell=True, stdin=subprocess.PIPE,
                                      capture_output=True)
                print(dump)
                if 'ERROR' in str(dump.stderr):
                    print("dump 2")
                    sleep(5)
                    dump2 = subprocess.run("adb shell uiautomator dump", shell=True, stdin=subprocess.PIPE,
                                           capture_output=True)
                    print(dump2)
                    if 'ERROR' in str(dump2.stderr):
                        return n2, st

                subprocess.run("adb pull /sdcard/window_dump.xml window_dump.txt")
                s = open("window_dump.txt", 'r')
                s = str(s.read()).split("x=\"2\" text")
                e = open("window_dump.txt", 'r')
                e = str(e.read()).split("x=\"3\" text")
                for w in range(len(s)):
                    if 'com.rjil.jiostbsetting:id/tv_item_tip' in s[w]:
                        n2.append(s[w].split("resource-id")[0][2:].split('"')[0])
                        st.append('')
                for w in range(len(e)):
                    if 'com.rjil.jiostbsetting:id/tv_item_value' in e[w]:
                        st[z] = e[w].split("resource-id")[0][2:].split('"')[0]
                        z += 1

                temp = []
                for x in n2:
                    if x not in temp:
                        temp.append(x)
                    else:
                        try:
                            st.pop([i for i, n in enumerate(n2) if n == 's'][1])
                        except IndexError:
                            pass
                n2 = temp
                print(n2)
                print(st)
                if ssid_list in n2:
                    return n2, st
                if ",".join(n2) == o2:
                    return n2, st
                for i in range(9):
                    subprocess.run("adb shell input keyevent 20")
                    sleep(2)
                sleep(2)
        except IndexError:
            return "None"
        except Exception as err:
            print(err)
            pass

    @staticmethod
    def get_wifistatus(ssid, str_keypass, r):
        # print('------------ ' + str(r))
        if r > 4:
            return 'FAIL'
        status = ''
        client_ssid_list, st = commonmethod.get_clientSSID_list(ssid)
        print("Inside Common Method")
        print(client_ssid_list, st)
        sequencenumber = None
        try:
            sequencenumber = client_ssid_list.index(ssid)
            print("Sequence Number for " + str(ssid) + " is " + str(sequencenumber))
        except ValueError:
            for k in range(6):
                try:
                    sequencenumber = client_ssid_list.index(ssid)
                    print("Sequence Number for " + str(ssid) + " is " + str(sequencenumber))
                except ValueError:
                    print("Rebooting STB since SSID is not available")
                    deviceStatus = subprocess.run("adb devices ", shell=True, stdin=subprocess.PIPE,
                                                  capture_output=True)
                    print(deviceStatus)
                    print(" Device connected for adb")
                    deviceStatus = subprocess.run("adb reboot ", shell=True, stdin=subprocess.PIPE,
                                                  capture_output=True)
                    print(deviceStatus)
                    sleep(60)
                    client_ssid_list, st = commonmethod.get_clientSSID_list(ssid)
                    if ssid not in client_ssid_list:
                        # return "FAIL"
                        pass
                    else:
                        print("Inside Common Method")
                        print(client_ssid_list, st)
                        sequencenumber = client_ssid_list.index(ssid)
                        print("Sequence Number for " + str(ssid) + " is " + str(sequencenumber))
                        break
        if sequencenumber is None:
            return 'FAIL'
        # lenssid=len(client_ssid_list)-sequencenumber
        # print("Up count" + str(lenssid) + "for UP")
        for i in range(0, len(client_ssid_list) - sequencenumber - 1):
            commonmethod.STB_Key_Event('19')
            # sleep(2)
        try:
            if st[sequencenumber] == 'Connected':
                return 'Connected'
            elif st[sequencenumber] == 'Saved':
                subprocess.run("adb shell input keyevent 23 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                subprocess.run("adb shell input keyevent 20 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                subprocess.run("adb shell input keyevent 23 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                subprocess.run("adb shell input keyevent 19 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                subprocess.run("adb shell input keyevent 23 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(10)
                # print('-------------' + str(r))
                status = commonmethod.get_wifistatus(ssid, str_keypass, r)
            elif st[sequencenumber] == '':
                # if r < 3:
                r += 1
                subprocess.run("adb shell input keyevent 23 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                c = "adb shell input text " + str(str_keypass)
                subprocess.run(c, shell=True, stdin=subprocess.PIPE, capture_output=True)
                sleep(1)
                subprocess.run("adb shell input keyevent 66 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
                print('------Connecting to ' + str(ssid) + '------')
                sleep(20)
                print('------------- Attempt = ' + str(r))
                status = commonmethod.get_wifistatus(ssid, str_keypass, r)
                '''else:
                    status = 'FAIL'
                    print('-----FAIL-----' + str(r))'''
        except IndexError:
            # if r < 3:
            r += 1
            subprocess.run("adb shell input keyevent 23 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
            sleep(1)
            c = "adb shell input text " + str(str_keypass)
            subprocess.run(c, shell=True, stdin=subprocess.PIPE, capture_output=True)
            sleep(1)
            subprocess.run("adb shell input keyevent 66 ", shell=True, stdin=subprocess.PIPE, capture_output=True)
            print('------Connecting to ' + str(ssid) + '------')
            sleep(20)
            print('------------- Attempt = ' + str(r))
            status = commonmethod.get_wifistatus(ssid, str_keypass, r)
            '''else:
                status = 'FAIL'
                print('-------------error' + str(r))
                print('-----FAIL-----' + str(r))'''
        return status

    @staticmethod
    def pingcheck():
        list_status = []
        logger.info('-------- Performing Ping Test for IPv4 --------')
        command4 = ["adb", "shell", "ping", "google.com"]
        ping4 = subprocess.Popen(command4, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        logger.info('-------- Performing Ping Test for IPv6 --------')
        command6 = ["adb", "shell", "ping6", "google.com"]
        ping6 = subprocess.Popen(command6, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        sleep(20)
        try:
            win32api.TerminateProcess(int(ping4._handle), -1)
        except pywintypes.error:
            print('--------- Ping 4 Process Already Closed ---------')
            # print(traceback.format_exc())
            pass
        out4, err4 = ping4.communicate()

        try:
            win32api.TerminateProcess(int(ping6._handle), -1)
        except pywintypes.error:
            print('--------- Ping 6 Process Already Closed ---------')
            # print(traceback.format_exc())
            pass
        out6, err6 = ping6.communicate()

        print('Output = ' + out4.decode())
        print('Error = ' + err4.decode())
        if 'unknown host' in str(err4.decode()) or 'Network is unreachable' in str(
                err4.decode()) or 'Destination Net Unreachable' in str(err4.decode()) or 'unknown host' in str(
                out4.decode()) or 'Network is unreachable' in str(out4.decode()) or 'Destination Net Unreachable' in str(
                out4.decode()) or len(out4.decode()) == 0:
            if '64 bytes' in str(out4.decode()):
                c = str(out4.decode()).count('Destination Net Unreachable')
                n = str(err4.decode()).count('Network is unreachable')
                b = str(out4.decode()).count('64 bytes')
                print(c, n, b)
                if (c > 10 or n > 10) and b < 15:
                    list_status.append('FAIL')
                    print('Ping Test Failed for IPv4')
                    logger.info('-------- Ping Test Failed for IPv4 --------')
                else:
                    list_status.append('PASS')
                    print('Ping Test Passed for IPv4')
                    logger.info('-------- Ping Test Passed for IPv4 --------')
            else:
                list_status.append('FAIL')
                print('Ping Test Failed for IPv4')
                logger.info('-------- Ping Test Failed for IPv4 --------')
        else:
            list_status.append('PASS')
            print('Ping Test Passed for IPv4')
            logger.info('-------- Ping Test Passed for IPv4 --------')

        print('Output = ' + out6.decode())
        print('Error = ' + err6.decode())
        if 'unknown host' in str(err6.decode()) or 'Network is unreachable' in str(
                err6.decode()) or 'Destination Net Unreachable' in str(err6.decode()) or 'unknown host' in str(
                out6.decode()) or 'Network is unreachable' in str(out6.decode()) or 'Destination Net Unreachable' in str(
                out6.decode()) or len(out6.decode()) == 0:
            if '64 bytes' in str(out6.decode()):
                c = str(out6.decode()).count('Destination Net Unreachable')
                n = str(err6.decode()).count('Network is unreachable')
                b = str(out6.decode()).count('64 bytes')
                print(c, n, b)
                if (c > 10 or n > 10) and b < 15:
                    list_status.append('FAIL')
                    print('Ping Test Failed for IPv6')
                    logger.info('-------- Ping Test Failed for IPv6 --------')
                else:
                    list_status.append('PASS')
                    print('Ping Test Passed for IPv6')
                    logger.info('-------- Ping Test Passed for IPv6 --------')
            else:
                list_status.append('FAIL')
                print('Ping Test Failed for IPv6')
                logger.info('-------- Ping Test Failed for IPv6 --------')
        else:
            list_status.append('PASS')
            print('Ping Test Passed for IPv6')
            logger.info('-------- Ping Test Passed for IPv6 --------')

        if 'FAIL' in list_status:
            return 'FAIL'
        else:
            return 'PASS'

    @staticmethod
    def getSSIDPassword():
        list_password = ['', '', '', '', '', '']
        infile = r"Logs/automation.log"

        with open(infile) as f:
            f = f.readlines()

        for line in f[::-1]:
            if 'SSID 1 Password' in line:
                temp = line.split(' ')
                list_password[0] = temp[8][:-1]
                break
        for line in f[::-1]:
            if 'SSID 2 Password' in line:
                temp = line.split(' ')
                # print(temp)
                list_password[1] = temp[8][:-1]
                break
        for line in f[::-1]:
            if 'SSID 3 Password' in line:
                temp = line.split(' ')
                list_password[2] = temp[8][:-1]
                break
        for line in f[::-1]:
            if 'SSID 4 Password' in line:
                temp = line.split(' ')
                list_password[3] = temp[8][:-1]
                break
        for line in f[::-1]:
            if 'SSID 5 Password' in line:
                temp = line.split(' ')
                list_password[4] = temp[8][:-1]
                break
        for line in f[::-1]:
            if 'SSID 6 Password' in line:
                temp = line.split(' ')
                list_password[5] = temp[8][:-1]
                break

        return list_password

    @staticmethod
    def getSSIDName():
        list_name = ['', '', '', '', '', '']
        infile = r"Logs/automation.log"

        with open(infile) as f:
            f = f.readlines()

        for line in f[::-1]:
            if 'SSID 1 Name' in line:
                list_name[0] = line[44:len(line) - 1]
                break
        for line in f[::-1]:
            if 'SSID 2 Name' in line:
                # print(temp)
                list_name[1] = line[44:len(line) - 1]
                break
        for line in f[::-1]:
            if 'SSID 3 Name' in line:
                list_name[2] = line[44:len(line) - 1]
                break
        for line in f[::-1]:
            if 'SSID 4 Name' in line:
                list_name[3] = line[44:len(line) - 1]
                break
        for line in f[::-1]:
            if 'SSID 5 Name' in line:
                list_name[4] = line[44:len(line) - 1]
                break
        for line in f[::-1]:
            if 'SSID 6 Name' in line:
                list_name[5] = line[44:len(line) - 1]
                break

        return list_name

    @staticmethod
    def getGHZ():
        ghz = ''
        g = open("window_dump.txt", 'r')
        g = str(g.read()).split("index=\"1\" text")
        for w in range(len(g)):
            if 'com.rjil.jiostbsetting:id/tv_item_ghz' in g[w]:
                ghz = g[w].split("resource-id")[0][2:].split('"')[0]
                break
        return ghz

    @staticmethod
    def connectWifiAndroid11(ssid, password, security, r):
        print('SSID = "'+ssid+'" | '+'Password = "'+password+'" | Security = "'+security+'"')
        time.sleep(15)
        print('---------------Wifi Disabled---------------')
        subprocess.run("adb shell cmd -w wifi set-wifi-enabled disabled", shell=True, stdin=subprocess.PIPE,
                       capture_output=True)
        sleep(5)
        print('---------------Wifi Enabled---------------')
        subprocess.run("adb shell cmd -w wifi set-wifi-enabled enabled", shell=True, stdin=subprocess.PIPE,
                       capture_output=True)
        sleep(15)
        print('---------------Wifi Scanning Available SSID---------------')
        str_ScanResult = subprocess.run("adb shell cmd -w wifi list-scan-results", shell=True, stdin=subprocess.PIPE,
                                        capture_output=True)
        sleep(5)
        print(str_ScanResult.stdout.decode())
        if ssid in str(str_ScanResult.stdout.decode()):
            logger.info('---------------Connecting SSID---------------')
            print('---------------Connecting SSID---------------')
            ssid_new = '"' + ssid + '"'
            password_new = '"' + password + '"'
            command = ['adb', 'shell', 'cmd', '-w', 'wifi', 'connect-network', str(ssid_new), str(security),
                       str(password_new)]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            print(stdout, stderr)
            '''str_Command = 'adb shell cmd -w wifi connect-network \\"' + str(ssid) + '\\" ' + str(
                security) + ' \\"' + str(password) + '\\" '
            subprocess.run(str_Command, shell=True, stdin=subprocess.PIPE, capture_output=True)'''
            sleep(15)
            str_WifiStatus = subprocess.run("adb shell cmd -w wifi status", shell=True, stdin=subprocess.PIPE,
                                            capture_output=True)
            sleep(5)
            string = str_WifiStatus.stdout.decode()
            print(string)
            pattern = '"[^"]*"'
            match = (re.search(pattern, string))
            try:
                a, b = match.span()
            except AttributeError:
                logger.info('-------------No SSID Connected-------------')
                print('-------------No SSID Connected-------------')
                return 'FAIL'
            str_ssidConnected = str(string[a + 1:b - 1])
            print("SSID = " + str_ssidConnected)
            a, b = string.find("successfulTxPackets:"), string.find("successfulTxPacketsPerSecond:")
            successfulTxPackets_old = int(string[a + 21:b - 1])
            if ssid == str_ssidConnected:
                status = commonmethod.pingcheck()
                if status == 'PASS':
                    logger.info('------------Ping Test Passed------------')
                    print('------------Ping Test Passed------------')
                    logger.info('-----------Playing YouTube for 60 seconds-----------')
                    print('-----------Playing YouTube for 60 seconds-----------')
                    subprocess.run(
                        "adb shell am start -a android.intent.action.VIEW -d \"https://www.youtube.com/watch?v=VVsC2fD1BjA&ab_channel=ScenicRelaxation\"",
                        shell=True, stdin=subprocess.PIPE, capture_output=True)
                    sleep(60)
                    subprocess.run("adb shell am force-stop com.google.android.youtube", shell=True, stdin=subprocess.PIPE,
                                   capture_output=True)
                    str_WifiStatus = subprocess.run("adb shell cmd -w wifi status", shell=True, stdin=subprocess.PIPE,
                                                    capture_output=True)
                    sleep(5)
                    string = str_WifiStatus.stdout.decode()
                    print(string)
                    a, b = string.find("successfulTxPackets:"), string.find("successfulTxPacketsPerSecond:")
                    successfulTxPackets_new = int(string[a + 21:b - 1])
                    logger.info("Before Playing YouTube successfulTxPackets = " + str(successfulTxPackets_old))
                    print("Before Playing YouTube successfulTxPackets = " + str(successfulTxPackets_old))
                    logger.info("After Playing YouTube successfulTxPackets = " + str(successfulTxPackets_new))
                    print("After Playing YouTube successfulTxPackets = " + str(successfulTxPackets_new))
                    if successfulTxPackets_new > successfulTxPackets_old + 500:
                        logger.info('------------' + str_ssidConnected + ' Connected------------')
                        print('------------' + str_ssidConnected + ' Connected------------')
                        logger.info('successfulTxPackets After Playing Youtube is greater than Before by more than 500, therefore Internet available.')
                        print('successfulTxPackets After Playing Youtube is greater than Before by more than 500, therefore Internet available.')
                        return 'Connected'
                    else:
                        logger.info('------------' + str_ssidConnected + ' Connected------------')
                        print('------------' + str_ssidConnected + ' Connected------------')
                        logger.info('successfulTxPackets After Playing Youtube is not greater than Before by more than 500, therefore Internet not available.')
                        print('successfulTxPackets After Playing Youtube is not greater than Before by more than 500, therefore Internet not available.')
                        return 'Internet'
                else:
                    logger.info('------------Ping Test Failed------------')
                    print('------------Ping Test Failed------------')
                    return 'Internet'
            else:
                logger.info('------------' + str_ssidConnected + ' Connected------------')
                print('------------' + str_ssidConnected + ' Connected------------')
                return 'FAIL'
        else:
            logger.info('----------------WIFI SSID Not Visible----------------')
            print('----------------WIFI SSID Not Visible----------------')
            return 'FAIL'

    @staticmethod
    def getWifiGHZAndroid11():
        try:
            str_WifiStatus = subprocess.run("adb shell cmd -w wifi status", shell=True, stdin=subprocess.PIPE,
                                            capture_output=True)
            sleep(5)
            string = str_WifiStatus.stdout.decode()
            print(string)
            a, b = string.find("Frequency: "), string.find("MHz, Net ID:")
            int_ghz = int(string[a + 11:b])
            print(int_ghz)
            if int_ghz < 3000:
                return '2.4GHz'
            else:
                return '5GHz'
        except ValueError:
            return '--'

    @staticmethod
    def ForgotAllNetwork():
        logger.info('All Saved Networks are Forget Started')
        list_networkid = []
        str_WifiStatus = subprocess.run("adb shell cmd -w wifi list-networks > WifiNetworks.txt", shell=True, stdin=subprocess.PIPE,
                                        capture_output=True)
        sleep(5)
        string = str_WifiStatus.stdout.decode()
        print('Dumped network list in WifiNetworks.txt')
        with open('WifiNetworks.txt', 'r') as reader:
            network_list = reader.readlines()
            for testdata in network_list:
                if 'No networks' in testdata:
                    print('No Saved Network Available')
                    logger.info('No Saved Network Available')
                    break
                get_network_id = testdata.split(' ')
                list_networkid.append(get_network_id[0])
        try:
            list_networkid.pop(0)
        except IndexError:
            pass
        print('Network ID\'s - ' + str(list_networkid))
        sleep(2)
        for i in list_networkid:
            print('Forgetting - ' + str(i))
            command = 'adb shell cmd -w wifi forget-network' + ' ' + str(i)
            subprocess.run(command, shell=True, stdin=subprocess.PIPE, capture_output=True)
            sleep(2)

        str_WifiStatus = subprocess.run("adb shell cmd -w wifi list-networks", shell=True,
                                        stdin=subprocess.PIPE,
                                        capture_output=True)
        string = str_WifiStatus.stdout.decode()
        if 'no networks' in string.lower():
            print('All Saved Networks are Cleared Successfully')
            logger.info('All Saved Networks are Cleared Successfully')
