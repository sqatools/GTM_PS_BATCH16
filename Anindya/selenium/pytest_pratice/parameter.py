import pytest

@pytest.mark.parametrize("username,password",[("Admin","admin123"),("ADMIN","PAWWSS")])
def test_1(username,password):
    print(f'the uername is {username} and the password is {password}')
    assert username == "Admin", f'the name is wrong'
    assert password == "admin123", f'the password is werong'
