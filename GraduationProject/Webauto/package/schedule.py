import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from GraduationProject.Webauto.package.basepage import BasePage


class Schedule(BasePage):
    def add_schedule(self, start_date, start_time, end_time, name):
        from GraduationProject.Webauto.package.mainpage import MainPage
        # 输入标题
        self.find(By.XPATH, '//*[@placeholder="添加主题"]').send_keys("紧急会议")
        # 输入日期
        el1 = self.find(By.XPATH, '//*[@class="_date-select date-start"]/div[1]//input')
        el1.clear()
        el1.send_keys(start_date)
        el1.send_keys(Keys.ENTER)
        # 输入开始时间
        ele1 = self.find(By.XPATH, '//*[@class="_date-select date-start"]/div[2]//input')
        # 通过先点击再清除的操作输入内容，不然无法清除内容
        ele1.click()
        ele1.clear()
        ele1.send_keys(start_time)
        el1.send_keys(Keys.ENTER)
        # 输入结束时间
        ele2 = self.find(By.XPATH, '//*[@class="_date-select date-end"]/div[1]/div/input')
        ele2.click()
        ele2.clear()
        ele2.send_keys(end_time)
        ele2.send_keys(Keys.ENTER)
        time.sleep(6)
        # 添加联系人
        self.find(By.XPATH, '//*[@placeholder="添加联系人、群或邮箱"]').send_keys(name)
        # 添加描述
        self.find(By.XPATH, '//*[@id="magicdomid-1_1"]').send_keys("第三季度发展目标")
        self.find(By.CSS_SELECTOR, '[class^="larkc-btn btn-group--save"]').click()
        time.sleep(1)
        # 返回保存成功的结果以帮助断言
        result = self.find(By.XPATH, '//*[@class="larkc-toast-fadeindelay larkc-toast"]/div').text
        return result
        # return MainPage(self.driver)


