This is Python Selenium Repo

Note :
Most of the time i use shortcuts
To Commit (Ctrl+K) and Push(Ctrl+Shift+K)

To run the Current file - Shift+F10
F7 - (Step Into): Step into a function call or loop.
F8 - (Step Over): Step over a function call or loop, executing it without stepping into it.
F9 - (Resume): Resume execution until the next breakpoint or the end of the program.
Shift+F7 -  (Step Out): Step out of the current function.

To auto adjust indent
Ctrl+Alt+l

To Rename a file
Shift+F6


# IMPORTANT
1) PLEASE PRACTICE MORE & MORE
2) Go through separate recorded sessions on Web Fundamentals, Playwright & POSTMAN Special classes
![Postman Special Class.png](Second_Month_July-2024%2FDate_19_July_2024%2FPostman%20Special%20Class.png)



How to install pytest

How to install allure report

how to execute test cases using pytest

how to generate allure reports



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To run all test cases
pytest Second_Month_July-2024/Date_22_July_2024/test_Lab180.py --alluredir=allure_results/all_test_cases     

generate report for all the test cases
allure generate allure_results/all_test_cases -o allure_report/all --clean

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To run only smoke test cases
pytest -m "smoke" Second_Month_July-2024/Date_22_July_2024/test_Lab180.py --alluredir=allure_results/smoke    

generate report for only smoke test cases
allure generate allure_results/smoke -o allure_report/smoke --clean
              
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To run only sanity test cases
pytest -m "sanity" Second_Month_July-2024/Date_22_July_2024/test_Lab180.py --alluredir=allure_results/sanity   

generate report for only sanity test cases
allure generate allure_results/sanity -o allure_report/sanity --clean
              
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To run only regression test cases
 pytest -m "regression" Second_Month_July-2024/Date_22_July_2024/test_Lab180.py --alluredir=allure_results/regression     

generate report for only regression test cases
allure generate allure_results/regression -o allure_report/regression --clean
              
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++














