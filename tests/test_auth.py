import pytest
from flask import g, session
from flaskr.db import get_db
from bs4 import BeautifulSoup as BS


def test_register(client, app):
    # Is status code OK
    assert client.get('/auth/register').status_code == 200
    # Post username and password of 'a'
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    # Ensure we go to the login site.
    assert 'http://localhost/auth/login' == response.headers['Location']

    # Test new user is in database.
    with app.app_context():
        assert get_db().execute(
            "select * from user where username = 'a'",
        ).fetchone() is not None

# pytest.mark.parametrize tells Pytest to run the same test function with
# different arguments


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data

# Test login to ensure it works.


def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


# Test logout to ensure it works.

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session

# Test account to ensure it works.


@pytest.mark.parametrize(('username', 'password'), (
    ('test', 'a'),
))
def test_account(auth, client, username, password):
    auth.login()

    responsePost = client.get('/auth/account')

    soup = BS(responsePost.data, features="html.parser")
    elem = soup.findAll('div', {'class': 'div__auth_display'})

    assert username in elem[0].text
