# INTRO TO TEST DRIVEN DEVELOPMENT USING PYTHON
* TDD: ensures you build the "thing right"
* BDD: ensures you build the "right thing" (Behavoiural)

python -m unittest discover
- used to run unit test

# CREATING AND SETTING UP Virtual env
- Python3 -m venv venv
- . Venv/bin/activate

# Test insstallables
- pip install nose
- pip install pinocchio
- pip install coverage
- pip install -r requirements.txt

# Test Commands
- nosetests -v —with-spec —spec-color 
- coverage report -muse 
# NB:
- setup.cfg to minimize use of long commands for running test

- pip freeze > requirements.txt

# TEST FIXTURES
- Happy paths verify that a function returns positive outcomes when expected, while sad paths verify that a function responds to exceptions appropriately and without breaking. 

- Test fixtures establish a known initial state before and after each test. 

- Test fixtures are helpful for many testing situations such as creating mock objects and loading a database with a known set of data. 

- Test fixtures operate at three levels of specificity: 

- * Module 

- * Test case 

- * Test 