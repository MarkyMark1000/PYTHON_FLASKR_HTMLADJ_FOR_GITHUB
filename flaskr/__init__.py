import os

from flask import Flask
from flaskr.global_funcs import get_ip


# Application Factory Function
def create_app(test_config=None):

    # create Flask app.   Tell Flask that config file is outside
    # of flaskr package.
    app = Flask(__name__, instance_relative_config=True)
    # Configure - set secret key for the project (OVERRIDE LATER ON)
    # and the database path.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Stop Cache of files.   Good, but it can make debugging difficult.
    # Idea for update dates here, but have not implemented yet.
    # https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config["CACHE_TYPE"] = "null"

    if test_config is None:
        # override default configuration with data from the config.py file.
        # It can be used to deploy a real secret key.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config passed in if test_config is None.
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # print out the ip address of the local host to make development
    # easy on mac
    strIP = get_ip()
    print("\n Local IP address used to access via wireless network:")
    print(" * Running on http://"+strIP+":5000/ (Press CTRL+ to quit)\n")
    print("\n Default Flask IP address:")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Used with the db registration of functions.
    from . import db
    db.init_app(app)

    # Import the blueprint.
    from . import auth
    app.register_blueprint(auth.bp)

    # Import the blog blueprint.
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
