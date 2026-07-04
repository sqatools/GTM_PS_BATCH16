import pytest

@pytest.mark.regression
def test_1(new):
    assert 1 ==1 
@pytest.mark.sanity
@pytest.mark.regression
def test_2(new):
    assert 2 == 2
@pytest.mark.smoke
def test_3():
    
    assert 3==5
