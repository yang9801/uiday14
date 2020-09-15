import allure
from selenium import webdriver


class Test001:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    @allure.step("第二步")
    def test001(self):
        print("\n test001")

    @allure.step("第一步")
    def test002(self):
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        print("\n 第一步的")
