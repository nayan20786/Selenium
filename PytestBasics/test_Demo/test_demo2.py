import pytest


# convenient way of using fixtures

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_demo1(self):
        assert True

    def test_demo2(self):
        assert True

    def test_demo3(self):
        assert True

    def test_demo4(self):
        assert True


# not convenient: To individually go on every function and mention the fixtures


def testdemo4(setup):
    assert True


def testdemo5(setup):
    assert True
