import sys
import os
import time



sys.path.append(os.getcwd())
import pytest

from page.page_home import PageHome
from page.page_in import PageIn
from tool.gei_driver import GetDriver


class TestLogin(object):
    def setup_class(self):
        # self.home = PageIn().page_get_home().page_home_portfolio_business()
        self.login = PageIn()

    def teardown_class(self):
        GetDriver.quit_driver()

    # @pytest.fixture(autouse=True)
    # def goto_home(self):
    #     self.login.page_get_home().page_home_portfolio_business()


    @pytest.mark.parametrize("name, pwd,expected,success", [[15811221835, 123456, "CHONGMAN", True]])
    def test_home(self, name, pwd, expected, success):
        self.login.page_get_login().page_login_portfolio_business(name, pwd)

        if success:
            el = self.login.page_get_login().page_user_nikename()
            print("昵称是", el)
            assert el == expected
        else:
            err_msg = self.login.page_get_login().page_get_toast(expected)
            print(err_msg)
            assert err_msg == expected
