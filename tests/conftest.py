import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

# Get the sql in the data.sql file into the variable _data_sql
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # tempfile.mkstemp() creates and opens a temporary file, returning the
    # file object and the path to it
    db_fd, db_path = tempfile.mkstemp()

    # The DATABASE path is overridden so it points to this temporary path
    # instead of the instance folder
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # Turn off caching
    app.config["CACHE_TYPE"] = "null"
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    # Initiate the database and insert the data.sql data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    # Return iterator of the app object.
    yield app

    # Close the file and delete the database.
    os.close(db_fd)
    os.unlink(db_path)

# The client fixture calls app.test_client() with the application object
# created by the app fixture. Tests will use the client to make requests
# to the application without running the server.


@pytest.fixture
def client(app):
    return app.test_client()

# The runner fixture is similar to client. app.test_cli_runner() creates
# a runner that can call the Click commands registered with the application.


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# For most of the views, a user needs to be logged in. The easiest way to do
# this in tests is to make a POST request to the login view with the client.
# Rather than writing that out every time, you can write a class with
# methods to do that, and use a fixture to pass it the client for each test.


class AuthActions(object):
    def __init__(self, client):
        self.client = client

    def login(self, username='test', password='test'):
        return self.client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self.client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)

# With the auth fixture, you can call auth.login() in a test to log in as
# the test user, which was inserted as part of the test data in the app
# fixture.

# The register view should render successfully on GET. On POST with valid form
# data, it should redirect to the login URL and the user’s data should be in
# the database. Invalid data should display error messages.
