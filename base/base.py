from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseHundredYears:
    def __init__(self, driver):
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):  # 获取元素文本
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda a: a.find_element(*loc))

    def base_click(self, loc):  # 点击元素
        self.base_find(loc).click()

    def base_input(self, loc, value):  # 输入文本
        text = self.base_find(loc)
        text.clear()
        text.send_keys(value)

    def base_get_text(self, loc):  # 获取文本
        return self.base_find(loc).text

    def base_toast(self, msg):  # 获取toast消息
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        return self.base_find(loc).text
