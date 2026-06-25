import pytest

@pytest.mark.regression
def test_1():
    assert 1 ==1 
@pytest.mark.sanity
@pytest.mark.regression
def test_2():
    assert 2 == 2
@pytest.mark.smoke
def test_3():
    
    assert 3==5
