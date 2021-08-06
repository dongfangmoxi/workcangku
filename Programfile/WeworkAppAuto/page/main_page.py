"""
主页
"""
from appium.webdriver.common.mobileby import MobileBy

from Programfile.WeworkAppAuto.page.basepage import BasePage
from Programfile.WeworkAppAuto.page.contactlist_page import ContactListPage


class MainPage(BasePage):

    _address_list_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact(self):
        """点击通讯录"""
        self.find_and_click(*self._address_list_element)
        return ContactListPage(self.driver)
