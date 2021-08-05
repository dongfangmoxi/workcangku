"""接口信息描述，只关注业务，不需要断言
"""
# import requests
from jsonpath import jsonpath

from apis.wework import WeWork


class Department(WeWork):

    def create_tag(self, data):
        """
        创建标签
        :return:创建标签接口的响应
        """
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        """
        把接口信息封装到字典中，不需要requests
        """
        req = {
            "method": "post",
            "url": create_url,
            "json": data
        }
        r = self.send_api(req)
        # r = requests.request("post", url=create_url, json=data)
        return r.json()

    def update_tag(self, data):
        """
        更新标签名字
        :return: 更新标签名字的响应
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        req = {
            "method": "post",
            "url": url,
            "json": data
        }
        # r = requests.request("post", url=url, json=data)
        r = self.send_api(req)
        return r.json()

    def delete_tag(self, tag_id):
        """
        删除标签名字
        :return: 删除标签名字的响应
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "get",
            "url": url
        }
        # r = requests.request("get", url=url)
        r = self.send_api(req)
        return r.json()

    def get_tag_list(self):
        """
        获取标签列表
        :return: 获取标签列表的响应
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": url
        }
        # r = requests.request("get", url=url)
        r = self.send_api(req)
        return r.json()

    # def clean_tag(self):
    #     """
    #     清理已经存在的标签信息
    #     :return:
    #     """
    #     # 查询已经存在的标签信息
    #     tag_info = self.get_tag_list()
    #     # 提取标签信息列表
    #     tagid_list = jsonpath(tag_info, "$..tagid")
    #     # 如果 id为 1 的标签是最基础的不可以删除
    #     for i in tagid_list:
    #         if i != 1:
    #             # 删除标签接口信息
    #             self.delete_tag(i)
