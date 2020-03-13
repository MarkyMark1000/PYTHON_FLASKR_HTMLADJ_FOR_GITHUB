import functools
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

# A view function is the code you write to respond to requests to your app.
# A Blueprint is a way to organize a group of related views and other code.

# This creates a Blueprint named 'auth'. Like the application object, the
# blueprint needs to know where it is defined, so __name__ is passed
# as the second argument. The url_prefix will be prepended to all the
# URLs associated with the blueprint.

# The blueprint needs to be imported from the create_app function in the
# flaskr package

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Create the register view

# Associate the URL /register with the register view function. When Flask
# receives a request to /auth/register, it will call the register view
# and use the return value as the response.


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # If we receive a form posted, then get the username and password
        # from the form.
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Validate the username and password and that the username and
        # password do not already exist in the db.
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        # If there is no error, then attempt to add the user into the database.
        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            # redirect url to login page.
            return redirect(url_for('auth.login'))

        # If there is an error or the redirect doesn't work for some reason,
        # show a flash error.   flash() stores messages that can be retrieved
        # when rendering the template.
        flash(error)

    # render_template() will render a template containing the HTML, which
    # you’ll write in the next step of the tutorial.
    return render_template('auth/register.html')

# Create the login view


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # If a login form is successfully posted, then get the username and
        # password from the form.
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Try to get the username fraom the database.
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # If the username does not exist, or the password is incorrect, fill
        # in the error form.
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # session is a dict that stores data across requests. When
            # validation succeeds, the user’s id is stored in a new session.
            # The data is stored in a cookie that is sent to the browser,
            # and the browser then sends it back with subsequent requests.
            # Flask securely signs the data so that it can’t be tampered with.
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        # If there is an error or the redirect doesn't work for some reason,
        # show a flash error.   flash() stores messages that can be retrieved
        # when rendering the template.
        flash(error)

    # render_template() will render a template containing the HTML, which
    # you’ll write in the next step of the tutorial.
    return render_template('auth/login.html')

# Now that the user’s id is stored in the session, it will be available on
# subsequent requests. At the beginning of each request, if a user is logged in
# their information should be loaded and made available to other views.

# bp.before_app_request() registers a function that runs before the view
# function, no matter what URL is requested.


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# To log out, you need to remove the user id from the session. Then
# load_logged_in_user won’t load a user on subsequent requests.


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Require Authentication in Other Views
# This decorator returns a new view function that wraps the original
# view it’s applied to


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

# The url_for() function generates the URL to a view based on a name and
# arguments. The name associated with a view is also called the endpoint, and
# by default it’s the same as the name of the view function.

# When using a blueprint, the name of the blueprint is prepended to the name
# of the function, so the endpoint for the login function you wrote above is
# 'auth.login' because you added it to the 'auth' blueprint.


def get_user(user_id):
    userData = get_db().execute(
        'SELECT username'
        ' FROM user'
        ' WHERE id = ?',
        (user_id,)
    ).fetchone()

    return userData

# Give the user the ability to update his/her details such as username


@bp.route('/account', methods=('GET', 'POST'))
@login_required
def account():
    # This should only be called when logged in, so assume user_id is valid
    user_id = session.get('user_id')

    # Get the username
    userData = get_user(user_id)

    return render_template('auth/account.html', userData=userData)
