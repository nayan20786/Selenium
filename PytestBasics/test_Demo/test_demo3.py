import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_datafromfixture(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])
