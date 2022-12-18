# here all the fixtures will be defined
import pytest


@pytest.fixture()
def dataLoad():
    return ["Michael", "CAt", "Orange.cat@catmail.com"]


@pytest.fixture()
def setup():
    print("I am executed first")
    yield
    print("I am cleanup guy")
