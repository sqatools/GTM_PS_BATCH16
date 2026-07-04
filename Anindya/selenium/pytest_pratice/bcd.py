import pytest

def test_1(next):
    assert 1==1, "This test is passed"
    print("Done it")

def test2(next):
    assert 2==2, "Thisis failed test2"
    print("OK")


def test3():
    assert 3==4, "This is not passed"
    print("DERTJ")
