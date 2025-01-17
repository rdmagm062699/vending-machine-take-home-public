Vending Machine Take Home
====================

This application simulates a vending machine, the features implemented are defined [here](./exercise/README.md)

### Requirements
* Python 3.9.6
* Docker


### Assumptions 
* The vending machine only has enough room for 10 of each product
* When the main url is visited the vending machine will be reset and restocked
* Only one person will use the vending machine at a time


### Unit Tests
To run unit tests execute the following:
1. `pip install -r requirements_dev.txt`
1. `pytest` 


### Acceptance Tests
To run acceptance tests execute the following.  The first run will take a couple of minutes due to needing to build necessary docker images:
1. `./scripts/run_acceptance_tests_docker.sh`


### Run app
To run the app:
1. `pip install -r requirements.txt`
1. `cd src`
1. `flask run`
1. Browse to http://127.0.0.1:5000/
