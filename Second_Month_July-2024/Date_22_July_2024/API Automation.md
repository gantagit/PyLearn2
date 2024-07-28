# API Automation Testing

HTTP fundamentals - API Testing
URL, Headers, Cookies, REST & SOAP
Status Code
Verify - TEST framework Expected Result == Actual Result

API Automation

1) How to make a Request
   a) **REQUEST - Python** -> (In Java - REST Assured)
   b) HTTP methods (GET, POST, PUT, PATCH, DELETE, OPTIONS)
2) How to Verify a Request
   a) Test Framework
   b) **PyTest** -> (In Java - TestNG)
3) Logs
4) How to run the code that which we have written
   a) Jenkins + GIT

API Automation Testing

# REQUEST Module & PyTest Module

# PyTest

* Install PyTest
* Create your first test
* Run multiple tests
* Assert that a certain exception is raised
* Group multiple tests in a class

# REQUEST

* Introduction
* Python Request Module
* The GET Request
* The Post Request
* Status Code
* JSON Response
* Response Header

How to Work with the PyTest?

- pip install pytest

- File name - test_name.py

- Test name - test_name_of_test():

- Assert - Actual Result == Expected Result.

How to run the PyTest?

- open cmd ->go the the folder - pytest

- run icon

PyTest Commands

- pytest -h

- To run all the testcases

- pytest

- To run specific testcase

- pytest ex02_July/22072024/test_Lab181.py

- To run specific testcase with pattern

- pytest -k "18"

- To run a specific marked Testcase

- Add a annotation @pytest.mark.regression

- pytest -m "regression" ex02_July/22072024/test_Lab182.py

How to see the Report of the PyTest Testcases?

- Make sure that allure commandline is installed

- Download the Node JS

- node -v

- npm install -g allure-commandline

- Verify that allure -> options

- Run your Pytestcase - pytest ex02_July/22072024/test_Lab183.py --alluredir=allure_result

- allure serve allure_result

