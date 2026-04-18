import pytest

def test_smoke_case1():
    print("This is smoke case 1")
    n1 = 10
    n2 = 20
    assert n1 + n2 == 30, "Addition is incorrect"

def test_smoke_case2():
    print("This is smoke case 2")
    s1 = "Hello"
    s2 = "World"
    assert s1 + " " + s2 == "Hello World", "String concatenation is incorrect"  

def test_smoke_case3():
    print("This is smoke case 3")
    lst = [1, 2, 3, 4, 5]
    assert len(lst) == 5, "List length is incorrect"

def test_smoke_case4():
    print("This is smoke case 4")
    dct = {"a": 1, "b": 2, "c": 3}
    assert dct["a"] == 1, "Dictionary value is incorrect"   

def test_smoke_case5():
    print("This is smoke case 5")
    assert True, "This test should always pass" 

def test_smoke_case6():
    print("This is smoke case 6")
    assert False, "This test should always fail"    

    