from base.base import BaseHundredYears
from page.__ini__ import existing_account_to_login, username, password, button, user_nikename


class PageLoing(BaseHundredYears):

    def page_username(self, name):  # 输入账号
        self.base_input(username, name)

    def page_password(self, pwd):  # 输入用户密码
        self.base_input(password, pwd)

    def page_button(self):  # 点击登录
        self.base_click(button)

    def page_user_nikename(self):  # 获取登录用户名
        return self.base_get_text(user_nikename)

    def page_get_toast(self, msg):  # 获取toast信息
        return self.base_toast(msg)

    def page_login_portfolio_business(self, name, pwd):
        self.page_username(name)
        self.page_password(pwd)
        self.page_button()
