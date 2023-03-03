import time

from appium import webdriver

from page.__ini__ import platformName, platformVersion, automationName, deviceName, appPackage, appActivity, url


class GetDriver:
    driver = None
    quit_status = True

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            caps = {}
            caps["platformName"] = platformName
            caps["platformVersion"] = platformVersion
            caps['automationName'] = automationName
            caps["deviceName"] = deviceName
            caps["appPackage"] = appPackage
            caps["appActivity"] = appActivity
            cls.driver = webdriver.Remote(url, caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        time.sleep(5)
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def change_quit_status(cls, status):
        """修改退出方法状态方法"""
        cls._quit_status = status


