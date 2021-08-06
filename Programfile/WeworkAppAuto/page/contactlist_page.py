"""通讯录列表页"""
from Programfile.WeworkAppAuto.page.add_member_page import AddMemeberPage
from Programfile.WeworkAppAuto.page.basepage import BasePage


class ContactListPage(BasePage):

    def click_addmember(self):
        # 点击添加成员
        self.swipe_find("添加成员", num=5).click()
        return AddMemeberPage(self.driver)