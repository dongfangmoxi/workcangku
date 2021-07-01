import allure
import pytest
# def test_li():
import sys
from os.path import dirname, abspath

print(sys.path)
sys.path.insert(0, dirname(dirname(abspath(__file__))))
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
print(sys.path)
# path_yi = dirname(dirname(dirname(abspath(__file__))))
# sys.path.append(path_yi)

from GraduationProject.Webauto.package.mainpage import MainPage


# 生成测试报告(allure)
@allure.feature("日程管理测试")
class TestAddSchedule:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @allure.story("添加日程测试用例")
    @pytest.mark.parametrize("start_date, start_time, end_time, name",
                             [("2021年7月1日", "08:00", "09:00", "张馨羽"),
                              ("2021年7月2日", "09:00", "10:00", "张三")])
    def test_addschedule(self, start_date, start_time, end_time, name):
        # 链式调用,飞书日历主页-->添加日程-->日历主页
        with allure.step("查看是否创建成功"):
            ass = self.main.goto_schedule().add_schedule(start_date, start_time, end_time, name)
            print(ass)
            # 断言是否出现保存成功的toast
            assert ass == "保存成功"
