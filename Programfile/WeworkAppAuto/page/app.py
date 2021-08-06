# app.py 启动app， 重启，关闭
from appium import webdriver


from Programfile.WeworkAppAuto.page.basepage import BasePage
from Programfile.WeworkAppAuto.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 复用driver ,提升执行测试用例的速度
            print("driver == None,创建driver")
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "True"
            caps["ensureWebviewsHavePages"] = True
            # 设置等待界面渲染完成的时间，提升速度
            caps['settings[waitForIdleTimeout]'] = 0
            # 等待adb命令超时
            caps['adbExecTimeout'] = 200000
            # 与server 建立连接，并且打开 caps 里面配置的页面LaunchSplashActivity
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待,在调用所有的find_element /find_elements方法的时候被激活
            self.driver.implicitly_wait(5)
        else:
            print("复用driver")
            # 启动app
            self.driver.launch_app()
        # 链式调用，紧接着调用类的内部函数
        return self

    def restart(self):
        # 关闭
        self.driver.close()
        # 启动app
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        """主页入口"""
        return MainPage(self.driver)