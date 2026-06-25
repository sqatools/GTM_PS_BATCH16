import pytest
@pytest.mark.smoke
def test_smoke_1():
    assert 1 == 1
@pytest.mark.sanity
def test_smoke_2():
    assert 2 == 2
@pytest.mark.sanity 
@pytest.mark.smoke
def test_smoke_3():
    assert 3 == 4
@pytest.mark.regression
def test_smoke_4():
    assert 4 == 4
@pytest.mark.regression
def test_smoke_5():
    assert 5 == 5


