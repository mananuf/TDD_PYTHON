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

- nosetests -v —with-spec —spec-color 
- coverage report -muse 

- setup.cfg to minimize use of long commands for running test