#Add any comments on this here

#Ensure the script is run as bash
SHELL:=/bin/bash

#Set help as the default for this makefile.
.DEFAULT: help

.PHONY: help

help:
	@echo ""
	@echo "PROJECT HELP:"
	@echo "make               	- this prints out the help for this makefile."
	@echo "make help          	- this prints out the help for this makefile."
	@echo "Setup:"
	@echo "make venv	    	- this deletes and recreates the venv virtual environment from requirements.txt"
	@echo "make venv-build-db   	- DANGER - rebuilds the sqllite database and may overwrite existing db."
	@echo "make venv-docs	    	- this deletes and recreates the html file in the docs directory using the index.rst file"
	@echo "Run:"
	@echo "make venv-run      	- runs the script in the venv virtual environment."
	@echo "make venv-run-dev    	- runs the dev script in the venv virtual environment."
	@echo "Testing:"
	@echo "make venv-test   	- Run the Test in the virtual environment."
	@echo "make venv-test-fail  	- Run the Test in the virtual environment displaying which funcs failed."
	@echo "make venv-cov-report	- Run the Test in the virtual environment using coverage and then display coverage report"
	@echo "make venv-cov-html	- Run the Test in the virtual environment using coverage and then build htmlcov directory."
	@echo "Code Standard:"
	@echo "make py-flaskr   	- Code standard for flaskr directory."
	@echo "make pystat-flaskr   	- Code standard statistics for flaskr directory."
	@echo "make py-tests   	- Code standard for tests directory."
	@echo "make pystat-tests   	- Code standard statistics for tests directory."
	@echo "Clean:"
	@echo "make venv-clean    	- Remove .pytest_cache, dist, __pycache__, flaskr.egg-info*, .coverage"
	@echo "make clean-venv    	- Remove venv virtual environment."
	@echo "Distribution:"
	@echo "make venv-build-req	- Rebuild requirements file from venv virtual environment."
	@echo "make venv-build-dist	- Builds a wheel distribution file in the dist directory."
	@echo ""

venv:
	@echo ""
	@echo "Remove the venv virtual environment and then re-create it. using the requirements.txt file."
	@echo ""
	rm -rf venv
	@echo ""
	virtualenv -p python3 venv
	@echo ""
	( source venv/bin/activate; pip install -r requirements.txt; )

venv-build-db:
	@echo ""
	@echo "Rebuilding the database."
	@echo ""
	@echo " 1 - Ensure a backup of the database is kept."
	@echo ""
	( [ ! -f ./instance/flaskr.sqlite ] || cp -i ./instance/flaskr.sqlite ./instance/flaskr_bup.sqlite )
	@echo ""
	@echo " 2 - Delete the existing database."
	@echo ""
	( rm -f  ./instance/flaskr.sqlite)
	@echo ""
	@echo " 3 - Rebuild the database."
	@echo ""
	( source venv/bin/activate; export FLASK_APP=./flaskr;flask init-db; )
	@echo ""

venv-docs:
	@echo ""
	@echo "Remove the documents and then recreate it using index.rst"
	@echo ""
	@echo ""
	rm -rf ./docs/*.html
	@echo ""
	( source venv/bin/activate; python3 ./venv/bin/rst2html.py ./docs/index.rst ./docs/index.html; )
	@echo ""

venv-run:
	@echo ""
	@echo "Running application using venv virtual environment."
	@echo ""
	( source venv/bin/activate; export FLASK_APP=./flaskr;flask run --host=0.0.0.0; )
	@echo ""

venv-run-dev:
	@echo ""
	@echo "Running dev application using venv virtual environment."
	@echo ""
	( source venv/bin/activate; export FLASK_ENV=development; export FLASK_APP=./flaskr;flask run --host=0.0.0.0; )
	@echo ""

venv-test:
	@echo ""
	@echo "Running test in venv virtual environment."
	@echo ""
	( source venv/bin/activate; pytest; )
	@echo ""

venv-test-fail:
	@echo ""
	@echo "Running and displaying failed test functions in venv virtual environment."
	@echo ""
	( source venv/bin/activate; pytest -v; )
	@echo ""

venv-cov-report:
	@echo ""
	@echo "Running test using coverage and then display report in venv virtual environment."
	@echo ""
	( source venv/bin/activate; coverage run -m pytest; coverage report)
	@echo ""

venv-cov-html:
	@echo ""
	@echo "Running test using coverage and then build htmlcov directory."
	@echo ""
	( source venv/bin/activate; coverage run -m pytest; coverage html;)
	@echo ""

py-flaskr:
	@echo ""
	@echo "Code standards for flaskr directory"
	@echo ""
	( source venv/bin/activate; pycodestyle ./flaskr/*.py;)
	@echo ""

pystat-flaskr:
	@echo ""
	@echo "Code standard statistics for flaskr directory"
	@echo ""
	( source venv/bin/activate; pycodestyle --statistics ./flaskr/*.py;)
	@echo ""

py-tests:
	@echo ""
	@echo "Code standards for tests directory"
	@echo ""
	( source venv/bin/activate; pycodestyle ./tests/*.py;)
	@echo ""

pystat-tests:
	@echo ""
	@echo "Code standard statistics for tests directory"
	@echo ""
	( source venv/bin/activate; pycodestyle --statistics ./tests/*.py;)
	@echo ""

venv-clean:
	@echo ""
	@echo "Remove .pytest_cache, dist, build, __pycache__, flaskr.egg-info*, .coverage"
	@echo ""
	rm -rf .pytest_cache
	@echo ""
	@echo ""
	rm -rf dist
	@echo ""
	rm -rf build
	@echo ""
	rm -rf **__pycache__**
	@echo ""
	@echo ""
	rm -rf flaskr/__pycache__
	@echo ""
	@echo ""
	rm -rf tests/__pycache__
	@echo ""
	@echo ""
	rm -rf flaskr.egg-info*
	@echo ""
	@echo ""
	rm -rf .coverage
	@echo ""
	@echo ""
	rm -rf ./htmlcov
	@echo ""

clean-venv:
	@echo ""
	@echo "Remove venv virtual environment directory"
	@echo ""
	rm -rf venv
	@echo ""

venv-build-req:
	@echo ""
	@echo "Rebuild requirements.txt from the venv virutal environment."
	@echo ""
	rm -rf requirements.txt
	@echo ""
	( source venv/bin/activate; pip freeze > requirements.txt; )
	@echo ""

venv-build-dist:
	@echo ""
	@echo "Build a wheel distribution file and add it to the dist directory."
	@echo ""
	( source venv/bin/activate; python3 setup.py bdist_wheel)
	@echo ""