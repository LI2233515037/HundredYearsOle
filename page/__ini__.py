# caps参数
from selenium.webdriver.common.by import By

platformName = "Android"
platformVersion = "5.1"
deviceName = "192.168.56.101:5555"
automationName = "Uiautomator2"
appPackage = "com.yunmall.lc"
appActivity = "com.yunmall.ymctoc.ui.activity.GuideActivity"
url = 'http://127.0.0.1:4723/wd/hub'
"""首页"""
home_skips = By.ID, "com.yunmall.lc:id/view_mask"  # 跳过
home_my = By.ID, "com.yunmall.lc:id/tab_me"  # 我的

"""登录"""
existing_account_to_login = By.ID,"com.yunmall.lc:id/textView1"
username = By.ID, 'com.yunmall.lc:id/logon_account_textview'  # 用户名
password = By.ID, 'com.yunmall.lc:id/logon_password_textview'  # 密码
button = By.ID, "com.yunmall.lc:id/logon_button"  # 登录
user_nikename = By.ID,"com.yunmall.lc:id/tv_user_nikename"
