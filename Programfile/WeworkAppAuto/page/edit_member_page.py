"""编辑成员页"""
from appium.webdriver.common.mobileby import MobileBy

from Programfile.WeworkAppAuto.page.basepage import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        """编辑成员点击保存"""
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        # self.driver.find_elements(MobileBy.XPATH, '//*[@text="必填"]')[1]
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from Programfile.WeworkAppAuto.page.add_member_page import AddMemeberPage
        return AddMemeberPage(self.driver)