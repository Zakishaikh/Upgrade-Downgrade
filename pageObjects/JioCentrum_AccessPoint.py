from time import sleep

from selenium.webdriver.common.by import By


class JioCentrum_AccessPoint:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(60)  # "tr[id=+str(i)+] td[class='gradeA sorting_1']"

    def JioCentrum_APStatus(self):  # //tr[@id='3']//td[@class='gradeA sorting_1']
        for i in range(1, 6):
            element = self.driver.find_element(By.XPATH, "//tr[@id='+str(i)+']//td[@class='gradeA sorting_1']")
            sleep(10)
            APStatus = element.get_attribute('innerHTML')
            print("AP " + str(i + 1) + "status ")
            print(APStatus)
