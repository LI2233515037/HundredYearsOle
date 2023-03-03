import time

from base.base import BaseHundredYears
from page.__ini__ import home_skips, home_my,existing_account_to_login


class PageHome(BaseHundredYears):
    def page_skip(self):  # 点击跳过
        self.base_click(home_skips)

    def page_home_mi(self):  # 点击我的
        self.base_click(home_my)
    def page_existing_account_to_login(self):
        time.sleep(3)
        self.base_click(existing_account_to_login)

    def page_home_portfolio_business(self):  # 组合业务方法
        self.page_skip()
        self.page_home_mi()
        self.page_existing_account_to_login()
