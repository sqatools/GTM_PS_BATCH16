
import pytest

@pytest.mark.parametrize("username,password",[("Admin","admin123"),("ADMIN","ADMIN344")])
def test_1(username,password):
    print(f'The name is {username} and the password is {password}')
    assert username == "Admin", "The username is incorrect"
    assert password == "admin123", "The password is incorrect"