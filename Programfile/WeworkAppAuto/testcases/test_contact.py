"""管理测试用例"""

import allure
import pytest

from Programfile.WeworkAppAuto.page.app import App
from Programfile.WeworkAppAuto.util.contact import Contact


@allure.feature("管理联系人测试")
class TestContact:
    def setup_class(self):
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    @allure.story("添加联系人测试用例")
    @pytest.mark.parametrize("name,phonenum", Contact.get_yaml_data("../datas/name_data.yaml"))
    def test_addcontact(self, name, phonenum):
        # 链式调用，主页进入通讯录->添加成员->手动添加页面->编辑姓名手机号->保存
        with allure.step("查看是否添加成功"):
            result = self.main.goto_contact(). \
                click_addmember().click_addmember_menual(). \
                edit_member(name, phonenum).verify_toast()
            assert result
