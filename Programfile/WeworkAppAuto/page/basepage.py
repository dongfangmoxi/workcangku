"""
基类 用来存放最基本的方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    # 设置 logging，打印日志信息
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        """封装定位元素的方法"""
        logging.info('find')
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        """封装定位并点击的方法"""
        logging.info('find_and_click')
        return self.find(by, locator).click()

    def swipe_find(self, text, num=3):
        """
        封装一个滑动查找的方法
        :param text: 要查找的文字
        :param num: 自定义滑动的次数
        :return:
        """
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele
            except:
                print("未找到")
                size = self.driver.get_window_size()
                # 设置宽高
                width = size.get('width')
                height = size.get("height")

                startx = width / 2
                starty = height * 0.8
                endx = startx
                endy = height * 0.3
                duration = 2000  # 单位是ms

                self.driver.swipe(startx, starty, endx, endy, duration)

            if i == 2:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException()

    def back(self, num=3):
        for i in range(num):
            self.driver.back()
