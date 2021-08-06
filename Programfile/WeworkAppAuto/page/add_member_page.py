"""添加成员页"""
from appium.webdriver.common.mobileby import MobileBy

from Programfile.WeworkAppAuto.page.basepage import BasePage


class AddMemeberPage(BasePage):

    def click_addmember_menual(self):
        """点击手动输入添加"""
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from Programfile.WeworkAppAuto.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def verify_toast(self):
        """定位‘保存成功’toast"""
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return True