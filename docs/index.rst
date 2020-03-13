============================================
FLASKR MICROBLOG TUTORIAL WITH ADJUSTED HTML
============================================

Overview
========

Tutorial
--------

This project is based upon the flaskr tutorial in the following location:
   https://flask.palletsprojects.com/en/1.0.x/tutorial/

The HTML, CSS and Javascript within the project has been adjusted into a new style that is more 
responsive to being viewed on a telephone.   
The appearance has been tested on Safari, Chrome, 
Firefox, Edge and Opera.   IE has been ignored and 
extensive testing using an external site such as browserstack has not been performed.

Warning:
--------

The default value for SECRET_KEY should be changed to some random bytes in production. Otherwise, 
attackers could use the public 'dev' key to modify the session cookie, or anything else that uses 
the secret key.

    python -c 'import os; print(os.urandom(16))'

    b'_5#y2L"F4Q8z\n\xec]/'

The tutorial specifically mentions that you can create a config.py file in the instance folder, which 
the factory will read from if it exists. Copy the generated value into it.

    venv/var/flaskr-instance/config.py
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

Additional Warning
------------------
In the make files I run flask with the --host=0.0.0.0 so that I can test the code easily 
on another device such as a phone.

Installation Guide
==================

Manual Installation
-------------------

- If it exists, remove the venv virtual environment directory using the following:
    - ``rm -rf venv      (mac)``
    - ``rmdir venv /s    (windows)``
- Recreate the virtual environment directory using the following:
    - Mac:
        - ``virtualenv --no-site-packages -p python3 venv``
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``pip install -r requirements.txt``
    - Windows:
        - ``virtualenv --no-site-packages -p python venv``
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``pip install -r requirements.txt``
- Note, you may need to install the app manually using:
    - ``pip install -e .``
- Create a new database the first time this project is used as follows:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``export FLASK_APP=./flaskr``
        - ``flask init-db``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``set FLASK_APP=flaskr``
        - ``flask init-db``
- If necessary, the html document in the docs directory can be rebuilt using:
    - Mac:
        - ``rm -rf ./docs/*.html``
        - ``rst2html ./docs/index.rst ./docs/index.html``
    - Windows:
        - ``del .\docs\*.html``
        - ``rst2html.py .\docs\index.rst .\docs\index.html``


MakeFile Installation (Mac, Linux or Unix)
------------------------------------------   
This project was written and tested on a mac and it has not been tested on Linux.

- To get help:
    - Run 'make' or 'make help' to get help on this project.
- It is sensible to reset the virtual environment so that it reflects the current requirements.txt file:
    - Run 'make venv' to build the virtual environment from requirements.txt.
- Note, you may need to install the app manually using:
    - ``pip install -e .``
- The first time that this project is installed, a new database will be needed:
    - Run 'make venv-build-db' to build the database.
- There isn't much supporting documentation, but it can be rebuilt using the following:
    - Run 'make venv-docs' to build /docs/index.html

    
Running the Application
=======================

Manual
------

- To run the app using the normal environment:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``export FLASK_APP=./flaskr``
        - ``flask run --host=0.0.0.0``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``set FLASK_APP=flaskr``
        - ``flask run --host=0.0.0.0``
    - Please note that using the host option makes it visible for testing on the local network/wifi.

- To run the app in the development environment:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``export FLASK_ENV=development``
        - ``export FLASK_APP=./flaskr``
        - ``flask run --host=0.0.0.0``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate```
        - ``set FLASK_ENV=development``
        - ``set FLASK_APP=flaskr``
        - ``flask run --host=0.0.0.0``
    - Please note that using the host option makes it visible for testing on the local network/wifi.

MakeFile
--------

- To run in a normal environemnt:
    - Run 'make venv-run' to run in the normal environment.
- To run in the development environment:
    - Run 'make venv-run-dev' to run in the development environment.

Testing the Application
=======================

Manual
------

- Depending upon if new packages have been installed and if you wish to keep them in the project, it may be worth rebuilding the virtual environment and requirements.txt file to ensure they are consistent:
    - To throw away any new packages and recreate the venv virtual environment from the requirements.txt file:
        - Mac:
            - ``rm -rf venv``
            - ``virtualenv --no-site-packages -p python3 venv``
            - ``deactivate or source deactivate``
            - ``source venv/bin/activate``
            - ``pip install -r requirements.txt``
        - Windows:
            - ``rmdir venv /s``
            - ``virtualenv --no-site-packages -p python venv``
            - ``deactivate or source deactivate``
            - ``.\venv\Scripts\activate``
            - ``pip install -r requirements.txt``
    - To recreate the requirements.txt file from the current venv virtual environment:
        - Mac:
            - ``rm -rf requirements.txt``
            - ``deactivate or source deactivate``
            - ``source venv/bin/activate``
            - ``pip freeze > requirements.txt``
        - Windows:
            - ``del requirements.txt``
            - ``deactivate or source deactivate``
            - ``.\venv\Scripts\activate``
            - ``pip freeze > requirements.txt``

- To run a basic test:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``pytest``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``pytest``

- To run a test showing which functions failed:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``pytest -v``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``pytest -v``

- To run a test showing the coverage of the test in a report:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``coverage run -m pytest``
        - ``coverage report``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``coverage run -m pytest``
        - ``coverage report``

- To run a test showing the coverage of the test in an html based report:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``coverage run -m pytest``
        - ``coverage html``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``coverage run -m pytest``
        - ``coverage html``

MakeFile
--------

- Depending upon if new packages have been installed and if you wish to keep them in the project, it may be worth rebuilding the virtual environment and requirements.txt file to ensure they are consistent:
    - To throw away any new packages and recreate the venv virtual environment from the requirements.txt file:
        - Run 'make venv' to build a new venv environment from existing requirements.txt file.
    - To recreate the requirements.txt file from the current venv virtual environment:
        - Run 'make venv-build-req' to build a new requirements.txt file from existing venv environment.

- To run a basic test:
    - Run 'make venv-test' to run test in venv virtual environment.

- To run a test showing which functions failed:
    - Run 'make venv-test-fail' to run test in venv virtual environment and display the functions.

- To run a test showing the coverage of the test in a report:
    - Run 'make venv-cov-report' to run test in venv virtual environment and display report.

- To run a test showing the coverage of the test in an html based report:
    - Run 'make venv-cov-html' to run test in venv virtual environment.

Test Coding Standards
=====================

Manual
------

- Test the code within the flaskr directory:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``pycodestyle --statistics ./flaskr/*.py``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``pycodestyle --statistics filename.py``
- Test the code within the tests directory:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``pycodestyle --statistics ./tests/*.py``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``pycodestyle --statistics filename.py``

MakeFile
--------

- Test the code within the flaskr directory:
    - Run 'make pystat-flaskr'

- Test the code within the tests directory:
    - Run 'make pystat-tests'

Cleanup
=======

Manual
------

- The flaskr app can become cluttered with a number of directories and files.   The following can be used to clean them up:
    - Mac:
        - ``rm -rf .pytest_cache``
        - ``rm -rf dist``
        - ``rm -rf build``
        - ``rm -rf **__pycache__**``
        - ``rm -rf flaskr/__pycache__``
        - ``rm -rf tests/__pycache__``
        - ``rm -rf flaskr.egg-info*``
        - ``rm -rf .coverage``
        - ``rm -rf ./htmlcov``
    - Windows:
        - ``rmdir /S .pytest_cache``
        - ``rmdir /S dist``
        - ``rmdir /S build``
        - ``rmdir /S flaskr\__pycache__``
        - ``rmdir /S tests\__pycache__``
        - ``rrmdir /S flaskr.egg-info``
        - ``del .coverage``
        - ``rmdir /S htmlcov``

- If you wish to remove the venv virtual environment directory:
    - ``rm -rf venv``
    - ``rmdir /S venv``

MakeFile
--------

- To clean files such as pytest_cache, dist etc:
    - Run 'make venv-clean'

- If you wish to remove the venv virtual environment directory:
    - Run 'make clean-venv'

Distribution
============

Manual
------

- The flask app uses a SECRET_KEY which is set in the __init__.py file.   This should be changed to some random bytes in production. Otherwise, attackers could use the public 'dev' key to modify the session cookie, or anything else that uses the secret key.
    - python -c 'import os; print(os.urandom(16))'
    - b'_5#y2L"F4Q8z\n\xec]/'

- Create the config.py file in the instance folder, which the factory will read from if it exists. Copy the generated value into it.
    - venv/var/flaskr-instance/config.py
    - SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

- To build a distribution file:
    - Mac:
        - ``deactivate or source deactivate``
        - ``source venv/bin/activate``
        - ``python3 setup.py bdist_wheel``
    - Windows:
        - ``deactivate or source deactivate``
        - ``.\venv\Scripts\activate``
        - ``python setup.py bdist_wheel``

Running in production
=====================

- When running publicly rather than in development, you should not use the built-in development server (flask run). The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure.

- Instead, use a production WSGI server. For example, to use Waitress, first install it in the virtual environment:

    - ``pip install waitress``

- You need to tell Waitress about your application, but it doesn’t use FLASK_APP like flask run does. You need to tell it to import and call the application factory to get an application object.

    - ``waitress-serve --call 'flaskr:create_app'``

    - ``Serving on http://0.0.0.0:8080``

- There are also many other ways to deploy an application.   Please see Deployment Options in the tutorial.