import sys

import allure
from jsonpath import jsonpath
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
print(sys.path)
from GraduationProject.Apiauto.apis.event import Events


# 生成测试报告(allure)
@allure.feature("日程管理接口测试")
class TestEvent:
    def setup_class(self):
        """开始测试之前的准备数据"""
        # 实例化日程类
        self.events = Events()
        # 准备数据
        self.create_data = {
                "summary": "每周例会",
                "start_time": {
                    "timestamp": "1625205600",
                    "timezone": "Asia/Shanghai"
                },
                "end_time": {
                    "timestamp": "1625212800",
                    "timezone": "Asia/Shanghai"
                },
                "location": {
                    "name": "研发中心室",
                    "address": "陆家嘴"
                },
                "reminders": [
                    {
                        "minutes": 5
                    }
                ],

        }
        self.update_data = {
                "summary": "视频会议",
                "location": {
                    "name": "研发中心室",
                    "address": "南京路"
                }
        }
        self.event_id = '4422ace8-45e5-44a8-b151-214ca553b9f3_0'

    @allure.story("日程场景测试用例")
    def test_events(self):
        """日程增删改查场景测试"""
        #  创建日程
        with allure.step("创建日程"):
            events_data = self.events.create_event(self.create_data)
            # 打印返回数据
            print(events_data)
        with allure.step("查询是否创建日程成功"):
            event_summary = jsonpath(events_data, "$..summary")
            assert "每周例会" in event_summary
        # 获取日程列表
        with allure.step("获取日程列表"):
            event_lists = self.events.get_event()
            print(event_lists)
        with allure.step("查询是否获取日程成功"):
            event_id_list = jsonpath(event_lists, "$..event_id")
            print(event_id_list)
            assert self.event_id in event_id_list
        # 更新日程
        with allure.step("更新日程"):
            self.events.update_event(self.event_id, self.update_data)
        with allure.step("查询是否更新日程成功"):
            event_lists = self.events.get_event()
            update_summary = jsonpath(event_lists, "$..summary")
            assert "视频会议" in update_summary
        # 删除日程
        with allure.step("删除日程"):
            self.events.delete_event(self.event_id)
        with allure.step("查询是否删除日程成功"):
            event_lists = self.events.get_event()
            update_summary = jsonpath(event_lists, "$..summary")
            print(update_summary)
            assert "视频会议" not in update_summary


