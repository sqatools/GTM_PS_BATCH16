import pytest



@pytest.mark.smoke
def test_smoke_case1():
    print("This is smoke case 1")
    n1 = 10
    n2 = 20
    assert n1 + n2 == 30, "Addition is incorrect"

@pytest.mark.smoke
def test_smoke_case2():
    print("This is smoke case 2")
    s1 = "Hello"
    s2 = "World"
    assert s1 + " " + s2 == "Hello World", "String concatenation is incorrect"

@pytest.mark.smoke
def test_smoke_case3():
    print("This is smoke case 3")
    lst = [1, 2, 3, 4, 5]
    assert len(lst) == 5, "List length is incorrect"
    assert lst[0] == 1, "First element is incorrect"
    assert lst[-1] == 5, "Last element is incorrect"

@pytest.mark.sanity
@pytest.mark.smoke
def test_smoke_case4():
    print("This is smoke case 4")
    d = {"name": "Alice", "age": 30, "city": "New York"}
    assert d["name"] == "Alice", "Name value is incorrect"
    assert d["age"] == 30, "Age value is incorrect"
    assert d["city"] == "New York", "City value is incorrect"

@pytest.mark.sanity
def test_smoke_case5():
    print("This is smoke case 5")
    assert 5 > 3, "Comparison is incorrect"
    assert 2 < 4, "Comparison is incorrect"
    assert 10 >= 10, "Comparison is incorrect"
    assert 1 <= 2, "Comparison is incorrect"

@pytest.mark.sanity
def test_smoke_case6():
    print("This is smoke case 6")
    assert "pytest" in "pytest framework", "Substring check is incorrect"
    assert "hello" not in "world", "Substring check is incorrect"

@pytest.mark.regression
def test_smoke_case7():
    print("This is smoke case 7")
    assert len("pytest") == 6, "String length is incorrect"
    assert len([1, 2, 3]) == 3, "List length is incorrect"
    assert len({"a": 1, "b": 2}) == 2, "Dictionary length is incorrect"