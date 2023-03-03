import sys
import os
import time

import pytest

sys.path.append(os.getcwd())
from page.page_in import PageIn
from tool.gei_driver import GetDriver


class TestHome(object):
    def setup_class(self):
        self.home = PageIn().page_get_home()

    def teardown_class(self):
        GetDriver.quit_driver()

    def test_home(self):
        time.sleep(3)
        self.home.page_home_portfolio_business()


