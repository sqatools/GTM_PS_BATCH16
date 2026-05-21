import pytest


@pytest.fixture(scope="function", autouse=True)
def setup():
    print("Launch Browser")
    print("LogIn Successfully")
    print("Browse Products")
    yield
    print("Close Browser")