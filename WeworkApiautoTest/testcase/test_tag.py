from jsonpath import jsonpath
import pytest
import allure
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
path_yi = dirname(abspath(__file__))
sys.path.append(path_yi)

from apis.department import Department
from testcase.utils import Utils


# 生成测试报告(allure)
@allure.feature("标签管理测试")
class TestTag:

    def setup_class(self):
        # 获取通讯录管理的 token 参数
        conf_data = Utils.get_yaml_data("../data/conf.yaml")
        corpid = conf_data["corpid"]["hogwarts"]
        corpsecret = conf_data["secret"]["contact_secret"]
        # 实例化部门类
        self.department = Department(corpid, corpsecret)
        # # 开始之前清楚标签信息（不然容易出错）
        # self.department.clean_tag()
        # 准备数据
        self.tag_id = 12
        self.create_data = {
            "tagname": "UI",
            "tagid": 12
        }
        self.updata_data = {
            "tagid": 12,
            "tagname": "UI design"

        }

    @allure.story("标签场景测试用例")
    def test_tag_scene(self):
        """
        标签增删改查场景测试
        """
        # 创建标签
        with allure.step("创建标签"):
            self.department.create_tag(self.create_data)
        # 查询是否创建成功
        with allure.step("查询是否创建成功"):
            tag_info = self.department.get_tag_list()
            print(tag_info)
            # assert tag_info["taglist"][0]["tagname"] == "UI"
            # 通过jsonpath进行断言
            name_list = jsonpath(tag_info, "$..tagname")
            print(name_list)
            self.department.log_info(name_list)
            assert "UI" in name_list

        # 更新标签
        with allure.step("更新标签信息"):
            self.department.update_tag(self.updata_data)
        with allure.step("查询是标签否更新"):
            tag_info = self.department.get_tag_list()
            print(tag_info)
            # assert tag_info["taglist"][0]["tagname"] == "UI design"
            name_list = jsonpath(tag_info, "$..tagname")
            self.department.log_info(name_list)
            assert "UI design" in name_list

        # 删除标签
        with allure.step("删除标签信息"):
            self.department.delete_tag(self.tag_id)
        with allure.step("查询删除标签信息结果"):
            tag_info = self.department.get_tag_list()
            print(tag_info)
            assert len(tag_info["taglist"]) == 0
            # id_list = jsonpath(tag_info, "$..tagid")
            # print(id_list)
            # assert self.tag_id not in id_list


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
