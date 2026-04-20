import pytest


@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("Admin", "wrongpass"),
    ("wronguser", "admin123")
])
def test_login(username, password):
    print(f"Logging in with username: {username} and password: {password}")
    assert username == "Admin", "Username is incorrect"
    assert password == "admin123", "Password is incorrect"
