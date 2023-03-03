from page.page_home import PageHome
from page.page_login import PageLoing
from tool.gei_driver import GetDriver


class PageIn:
    def __init__(self):
        self.driver = GetDriver().get_driver()

    def page_get_home(self):
        return PageHome(self.driver)

    def page_get_login(self):
        return PageLoing(self.driver)
