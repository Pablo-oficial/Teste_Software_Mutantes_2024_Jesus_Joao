# Pytest Setup Teardown Example

This repo contains the sample code for the article - [What is Setup and Teardown in Pytest? (Importance of a Clean Test Environment)](https://pytest-with-eric.com/pytest-best-practices/pytest-setup-teardown/)

This project is a simple example of how to use the `setup` and `teardown` methods in Pytest.

## Requirements

* Python 3.11.4

Please install the dependencies via the `requirements.txt` file using

```
pip install -r requirements.txt
```

If you don't have Pip installed please follow instructions online on how to do it.

## How To Run the Unit Tests

To run the Unit Tests, from the root of the repo run

```
# run tests normally
pytest -vv tests/unit/test_ip_checker.py  

#perform tests with line (node) coverage report
pytest -vv tests/unit/test_ip_checker.py --cov=src.ip_checker

# perform tests with branch coverage report
pytest -vv tests/unit/test_ip_checker.py --cov=src.ip_checker --cov-branch --cov-report html

#run tests with mutmut
mutmut run --paths-to-mutate=src/ip_checker.py
```

If you have any questions about the project please raise an Issue on GitHub.