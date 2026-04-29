import pytest


@pytest.fixture
def setup(): # This will run once before all the test cases in the module and is used for setup activities that are common to all test cases in the module
    print("Launch Browser")
    print("LogIn Successfully")
    print("Browse Products")
    yield
    print("LogOut Successfully") # This will run once after all the test cases in the module and is used for teardown activities that are common to all test cases in the module
    print("Close Browser") 