import pytest 


@pytest.mark.parametrize("username, password",[
    ("Admin", "admin123"),
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("Admin", "wrongpass"),
    ("wronguser", "admin123"),
    ("Hello", "Boy")
])


def test_login(username, password):
    print(f"Logging in with username: {username} ans password: {password}")
    assert username == "Admin", "Username is inccorect"
    assert password == "admin123", "Password is incorrect"