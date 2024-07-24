# Process for the Automation

Manual Testing of API
1) **Requirement**
   a) API Documentation - Google Goc, Confluence, Swagger, Word, Postman Documentation, ....
   b) When No API Documentation is available - Create high level basic document - Details of API's 
      which we want to Test
2) **Test Plan** - QA lead -> Google Excel or Google Doc or Confluence
3) **Test Cases** -> Google Sheets, Jira(TMT) , Test Link, Test Rail, Qase .......
4) **Postman** - Collections
5) **Variable, environment, Test Scripts** - to write the basic Test cases(Postman Automation)
6) **TEST Automation** -> Test Case -> 20 -> Automate them using 
   -> Python + Request + PyTest + Allure Report -> Proper Framework -> Regression Test suite 
   -> run via the Jenkins/Teamcity Daily - (Git)

