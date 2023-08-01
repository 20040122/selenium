import allure
import pytest


class Test:
    def test_01(self):
        print("test_01")

# 入口函数
if __name__ == '__main__':
    pytest.main(["-s","test_demo.py"])

class Test_01:
    # 函数级别方法操作
    def setup(self):
        print("setup_class")
    def teardown(self):
        print("teardown_class")
    def test_01(self):
        print("test_01")
    def test_02(self):
        print("test_02")

    # 类级别方法操作
class Test_02:
    def setup_class(cls):
        print("setup_class")
    def teardown_class(cls):
        print("teardown_class")
    def test_01(self):
        print("test_01")
    def test_02(self):
        print("test_02")
# 用例执行顺序
class Test_03:
    @pytest.mark.run(order=2)
    def test_01(self):
        print("test_01")
    @pytest.mark.run(order=1)
    def test_02(self):
        print("test_02")

# 用例执行失败重试
class Test_04:
    def test_a(self):
        assert 1==1

    def test_b(self):
        assert 1==2
        print("fail")
    #  pytest test_demo.py::Test_04 --reruns 3 --reruns-delay 1

# 跳过
class Test_05:
    def test_a(self):
        assert 1==1
    @pytest.mark.skip(reason="版本不支持")
    def test_b(self):
        assert 1==2
        print("fail")


#预期失败
class Test_06:
    def test_a(self):
        assert 1==1
    @pytest.mark.xfail(reason="版本不支持")
    def test_b(self):
        assert 1==2
        print("fail")


# 参数化,多个参数、单个参数
class Test_07:
    @pytest.mark.parametrize("a,b",[(1,2),(3,4)])
    def test_a(self,a,b):
        print(a+b)
    @pytest.mark.parametrize("a",[1,2,3,4])
    def test_b(self,a):
        print(a)


# fixture登陆操作
class Test_08:
    @pytest.fixture()
    def login(self):
        print("登陆操作")
    def test_a(self,login):
        print("test_a")
    def test_b(self):
        print("test_b")
    def test_c(self):
        print("test_c")

# 生成测试报告 pytest --alluredir=reports test_demo.py
# allure generate reports/ -o reports/html --clean

class Test_allure:
    # 严重级别
    @allure.severity(allure.severity_level.BLOCKER)
    # 标注功能
    @allure.feature("测试功能")
    def test_a(self):
        assert 1==1
    # 标注用例
    @allure.step("测试步骤001")
    def test_b(self):
        assert 1==2
        print("fail")