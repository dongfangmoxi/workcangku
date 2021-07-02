from selenium import webdriver
from selenium.webdriver.common.by import By

from GraduationProject.Webauto.package.basepage import BasePage
from GraduationProject.Webauto.package.schedule import Schedule


class MainPage(BasePage):
    _base_url = "https://rtqcex0fdr.feishu.cn/calendar/week"

    def goto_schedule(self):
        self.find_and_click(By.CSS_SELECTOR, '[class="larkc-svg-icon icon-add  "]')
        return Schedule(self.driver)

    # def get_schedule(self):
    #     result = self.find(By.XPATH, '//*[@class="larkc-toast-fadeindelay larkc-toast"]/div').text
    #     return result


