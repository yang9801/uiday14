import allure


class Test002:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第一步")
    def test_001(self):
        print("\n test_001")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("第二步")
    def test_002(self):
        print("\n test_002")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("第三步")
    def test_003(self):
        print("\n test_003")

    @allure.severity(allure.severity_level.MINOR)
    @allure.step("第四步")
    def test_004(self):
        print("\n test_004")

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step("第五步")
    def test_005(self):
        print("\n test_005")
        assert False
