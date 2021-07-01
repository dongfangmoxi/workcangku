import logging

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    # # 设置 logging
    # fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # logging.getLogger().setLevel(0)
    # formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    # fileHandler.setFormatter(formatter)
    # logging.getLogger().addHandler(fileHandler)

    # def log_info(self, msg):
    #     """
    #     添加日志信息方法
    #     :param msg:
    #     :return: info 级别的日志
    #     """
    #     return logging.info(msg)

    _base_url = ""

    def __init__(self, driver: webdriver = None):
        if driver is None:
            # 避免driver重复初始化，第一次初始化的时候driver是空的，就进行初始化
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        ele: WebElement = self.find(by, locator)
        ele.click()
        return ele

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
