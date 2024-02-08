from utilities.updateExcel import updateExcel
from utilities.outputVariables import *
import pytest
from selenium import common
# from selenium import webdriver
from testCases.Test_DeviceInfo import Test_DeviceInfo
from utilities.ReadTestData import Excel_Env


class Test_TR069_sanity:
    path = Excel_Env.getExcelPath()
    new_path = Excel_Env.getExcelNewPath()
    sheet_name = Excel_Env.getsheet_name()
    test_name = Excel_Env.gettest_name()

    @pytest.mark.sanity("last")
    @pytest.mark.device("last")
    @pytest.mark.complete("last")
    @pytest.mark.order("last")
    @pytest.mark.wifi("last")
    @pytest.mark.abc("last")
    def test_TR069_ACS_sanity(self, setup):
        try:
            self.di = Test_DeviceInfo(setup)
            list_deviceinfo = self.di.DeviceInfo()
            updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, list_deviceinfo)
        except (common.exceptions.NoSuchElementException, common.exceptions.WebDriverException, common.exceptions):
            updateExcel.writedata_all(self.path, self.new_path, self.test_name, self.sheet_name, list_output, list_row, ['', '', '', ''])