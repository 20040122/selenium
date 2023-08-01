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