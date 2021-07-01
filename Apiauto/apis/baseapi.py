import logging

import requests


class BaseApi:
    # 设置 logging，打印日志信息
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        """
        添加日志信息方法
        :param msg:
        :return: info 级别的日志
        """
        return logging.info(msg)

    def send_api(self, req):
        """
        对requests进行二次封装
        :param req:**req相当于对下面的req进行解包
        :return:接口响应结果
        """
        self.log_info("-----request data-----")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("-----request data-----")
        self.log_info(r.json())
        return r
